"""Put the opening movie of one ACE2 disc image on another (the "Glorious" opening on the Special Vocal Version).

  python swap_movie.py --target "<SVV or English ISO>" --source "<original 2006 ISO>" --out "<new ISO>"
  python swap_movie.py --target "<SVV or English ISO>" --source "<original 2006 ISO>" --in-place

The Special Vocal Version (SLPS-25829) opens with a vocal song; the original 2006 release (SLPS-25623) opens with
"Glorious". Both discs carry /MOVIE0/MOVIE001.PSS with exactly the same size (275,251,204 bytes), so the file is
replaced whole at its own extent: no other byte of the image changes and the ISO9660/UDF records stay valid. Works on
the untouched Special Vocal Version and on any image built from it (the English patch). The result is re-read and the
movie compared with the source before success is reported.

Standalone (Python 3.8+ standard library only) so players can run it without the build environment. The maintainer
also uses it the other way round (source = Special Vocal Version) to prepare the release patch (make_patch.py).
"""
import argparse, hashlib, shutil, struct, sys
from pathlib import Path

SECTOR = 2048
MOVIE = '/MOVIE0/MOVIE001.PSS'
EXECUTABLES = {'/SLPS_258.29': 'Special Vocal Version (SLPS-25829)', '/SLPS_256.23': 'original 2006 release (SLPS-25623)'}
BLOCK = 8 << 20


def iso_files(stream):
    """{'/MOVIE0/MOVIE001.PSS': {'offset', 'size'}} for every file of an ISO9660 image (same walk as ace2lib)."""
    stream.seek(16 * SECTOR)
    pvd = stream.read(SECTOR)
    if pvd[:7] != b'\x01CD001\x01':
        raise SystemExit('Not an ISO9660 image (expected a 2048-byte-sector PS2 DVD dump)')
    found = {}

    def walk(lba, size, parent):
        stream.seek(lba * SECTOR)
        data = stream.read(size)
        at = 0
        while at < len(data):
            length = data[at]
            if not length:
                at = (at // SECTOR + 1) * SECTOR
                continue
            record = data[at:at + length]
            name = record[33:33 + record[32]]
            if name not in (b'\0', b'\1'):
                full = parent + '/' + name.decode('ascii').split(';')[0]
                lba_, size_ = struct.unpack_from('<II', record, 2)[0], struct.unpack_from('<I', record, 10)[0]
                if record[25] & 2:
                    walk(lba_, size_, full)
                else:
                    found[full] = {'offset': lba_ * SECTOR, 'size': size_}
            at += length

    walk(struct.unpack_from('<I', pvd, 158)[0], struct.unpack_from('<I', pvd, 166)[0], '')
    return found


def describe(files):
    return next((v for k, v in EXECUTABLES.items() if k in files), 'unknown disc')


def extent_sha(stream, offset, size):
    d = hashlib.sha256(); stream.seek(offset); left = size
    while left:
        block = stream.read(min(BLOCK, left))
        if not block:
            raise SystemExit('Short read: the image is truncated')
        d.update(block); left -= len(block)
    return d.hexdigest()


def movie(path):
    """(record, disc description, sha256 of the movie) of an image."""
    if not Path(path).is_file():
        raise SystemExit('No such file: %s' % path)
    with Path(path).open('rb') as f:
        files = iso_files(f)
        if MOVIE not in files:
            raise SystemExit('%s has no %s: not an Another Century\'s Episode 2 disc' % (path, MOVIE))
        rec = files[MOVIE]
        return rec, describe(files), extent_sha(f, rec['offset'], rec['size'])


def image_sha(path, replace=None):
    """SHA-256 of a whole image; replace=(record, source image) hashes it as if that extent came from the source."""
    d = hashlib.sha256()
    with Path(path).open('rb') as f:
        if replace:
            rec, src_path = replace
            src_rec = movie(src_path)[0]
        pos = 0
        while True:
            block = f.read(BLOCK)
            if not block:
                break
            if replace:
                a, b = max(pos, rec['offset']), min(pos + len(block), rec['offset'] + rec['size'])
                if a < b:
                    with Path(src_path).open('rb') as s:
                        s.seek(src_rec['offset'] + a - rec['offset'])
                        block = block[:a - pos] + s.read(b - a) + block[b - pos:]
            d.update(block); pos += len(block)
    return d.hexdigest()


def swap(target, source, out=None):
    """Copy the movie of source into target (or into a copy of it at out). Returns the movie sha256."""
    t_rec, t_kind, t_sha = movie(target)
    s_rec, s_kind, s_sha = movie(source)
    print('target: %s\n  %s %s sha256 %s' % (target, t_kind, MOVIE, t_sha))
    print('source: %s\n  %s %s sha256 %s' % (source, s_kind, MOVIE, s_sha))
    if t_rec['size'] != s_rec['size']:
        raise SystemExit('Movie sizes differ (%d vs %d bytes): a whole-file swap would need a disc rebuild'
                         % (t_rec['size'], s_rec['size']))
    if out:
        out = Path(out)
        if out.exists():
            raise SystemExit('Output exists: %s' % out)
        print('copying target to', out, flush=True)
        shutil.copyfile(target, out)
        target = out
    if t_sha == s_sha:
        print('the target already has this movie; nothing to write')
        return s_sha
    print('writing', MOVIE, flush=True)
    with Path(source).open('rb') as s, Path(target).open('r+b') as t:
        s.seek(s_rec['offset']); t.seek(t_rec['offset']); left = s_rec['size']
        while left:
            block = s.read(min(BLOCK, left))
            t.write(block); left -= len(block)
    rec, _, got = movie(target)
    if rec != t_rec or got != s_sha:
        raise SystemExit('Verification failed: the movie on %s does not match the source' % target)
    print('PASS: %s on %s is now the one from %s (sha256 %s)' % (MOVIE, target, s_kind, got))
    return got


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--target', required=True, help='Special Vocal Version image (untouched or patched)')
    ap.add_argument('--source', required=True, help='image whose MOVIE001.PSS is copied (the original 2006 release)')
    where = ap.add_mutually_exclusive_group(required=True)
    where.add_argument('--out', help='write a new image (the target is left untouched)')
    where.add_argument('--in-place', action='store_true', help='overwrite the movie inside the target image')
    ap.add_argument('--sha', action='store_true', help='print the SHA-256 of the whole result (slow: reads ~3.6 GB)')
    args = ap.parse_args()
    swap(args.target, args.source, None if args.in_place else args.out)
    if args.sha:
        result = args.target if args.in_place else args.out
        print('image sha256', image_sha(result))


if __name__ == '__main__':
    main()

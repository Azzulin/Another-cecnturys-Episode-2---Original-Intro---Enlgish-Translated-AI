"""Make the public release patch of a build: an xdelta from the untouched Special Vocal Version to the English disc.

  python tools/ace2/make_patch.py --version 0.1.0 [--svv-opening] [--xdelta3 PATH]

Input: work/output/ACE2-EN-<version>.iso and its JSON report (build.py --write), already passed by audit_iso.py.
With --svv-opening: work/output/ACE2-EN-<version>-svv-opening.iso (build.py --svv-opening --write), for those
without the 2006 disc.
Output in work/release/:
  ACE2-EN-<version>.xdelta              Special Vocal Version -> English (Special Vocal opening)
  ACE2-EN-<version>-SHA256.txt          checksums of every input and output a player can check

The patch never carries the 2006 opening: the build's MOVIE001.PSS is put back to the Special Vocal one first
(swap_movie.py), so the patch holds only the translation (text tables and fonts) and the files the growth moved.
Players who own the original 2006 disc add "Glorious" with swap_movie.py, which rewrites that one extent: the result
is byte-identical to the build, whose SHA-256 is listed. Every step is checked: the patch is decoded again and
compared, and the Glorious SHA-256 is recomputed from the patched image plus the 2006 movie (when the 2006 disc is
in the root; a --svv-opening build is checked against its own SHA-256 instead).
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT, BASE, ORIGINAL_RELEASE, require
from swap_movie import MOVIE, movie, swap, image_sha

OUT = ROOT / 'work' / 'output'
RELEASE = ROOT / 'work' / 'release'
# source window large enough for the files that DATA.BIN's growth moved (xdelta3 default 64 MB is too small)
WINDOW = str(1 << 30)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--version', required=True)
    ap.add_argument('--svv-opening', action='store_true',
                    help='patch the build made with build.py --svv-opening (no 2006 disc needed)')
    ap.add_argument('--xdelta3', default=shutil.which('xdelta3') or 'xdelta3')
    args = ap.parse_args()
    require(BASE.is_file(), 'Missing the untouched Special Vocal Version: ' + str(BASE))
    have_2006 = ORIGINAL_RELEASE.is_file()
    require(have_2006 or args.svv_opening,
            'Missing the 2006 disc (%s): use a build made with --svv-opening and pass --svv-opening' % ORIGINAL_RELEASE)
    build = OUT / ('ACE2-EN-%s%s.iso' % (args.version, '-svv-opening' if args.svv_opening else ''))
    require(build.is_file(), 'Missing the build: ' + str(build))
    report = json.loads(build.with_suffix('.json').read_text(encoding='utf-8'))
    require(report.get('verified'), 'The build report is not verified: rebuild with build.py --write')
    RELEASE.mkdir(parents=True, exist_ok=True)
    plain = build if args.svv_opening else RELEASE / ('ACE2-EN-%s-svv-opening.iso' % args.version)
    patch = RELEASE / ('ACE2-EN-%s.xdelta' % args.version)
    check = RELEASE / ('ACE2-EN-%s-check.iso' % args.version)
    for p in (patch, check) if args.svv_opening else (plain, patch, check):
        require(not p.exists(), 'Output exists: ' + str(p))

    if args.svv_opening:
        print('1/4 build already has the Special Vocal opening:', build, flush=True)
    else:
        print('1/4 build with the Special Vocal opening', flush=True)
        swap(build, BASE, plain)
    print('2/4 xdelta3 encode (this takes a while)', flush=True)
    subprocess.run([args.xdelta3, '-e', '-9', '-B', WINDOW, '-s', str(BASE), str(plain), str(patch)], check=True)
    print('3/4 decode check', flush=True)
    subprocess.run([args.xdelta3, '-d', '-B', WINDOW, '-s', str(BASE), str(patch), str(check)], check=True)
    plain_sha, check_sha = image_sha(plain), image_sha(check)
    require(plain_sha == check_sha, 'Decoded image differs from the patched image')
    check.unlink()
    print('4/4 checksums', flush=True)
    if args.svv_opening:
        require(plain_sha == report['sha256'], 'Patched (%s) != build (%s)' % (plain_sha, report['sha256']))
    glorious_sha = None
    if have_2006:
        rec = movie(plain)[0]
        glorious_sha = image_sha(plain, (rec, ORIGINAL_RELEASE))
        if not args.svv_opening:
            require(glorious_sha == report['sha256'],
                    'Patched + Glorious (%s) != build (%s)' % (glorious_sha, report['sha256']))
    lines = [
        'Another Century\'s Episode 2 - English patch %s' % args.version,
        '',
        'Input (your disc)',
        '  %s  Another Century\'s Episode 2 - Special Vocal Version (Japan).iso  (SLPS-25829)' % image_sha(BASE),
    ]
    if have_2006:
        lines += [
            'Optional input for the "Glorious" opening',
            '  %s  Another Century\'s Episode 2 (Japan).iso  (SLPS-25623, 2006)' % image_sha(ORIGINAL_RELEASE),
        ]
    lines += [
        'Patch',
        '  %s  %s' % (image_sha(patch), patch.name),
        'Output after the patch (Special Vocal opening)',
        '  %s  ACE2-EN-%s.iso' % (plain_sha, args.version),
    ]
    if glorious_sha:
        lines += [
            'Output after swap_movie.py with the 2006 disc ("Glorious" opening)',
            '  %s  ACE2-EN-%s.iso' % (glorious_sha, args.version),
        ]
    lines += ['%s alone' % MOVIE, '  %s  Special Vocal Version' % movie(BASE)[2]]
    if have_2006:
        lines.append('  %s  original 2006 release' % movie(ORIGINAL_RELEASE)[2])
    sums = RELEASE / ('ACE2-EN-%s-SHA256.txt' % args.version)
    sums.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print('PASS: %s (%d bytes), %s' % (patch, patch.stat().st_size, sums.name))
    if not args.svv_opening:
        print('%s is only a check copy; delete it once the release is published.' % plain.name)


if __name__ == '__main__':
    main()

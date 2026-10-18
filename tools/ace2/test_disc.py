"""Disc writer tests (each writes a full 3.6 GB image to work/output/_test and deletes it afterwards).

  1. identity   no edits                          -> output SHA-256 == base SHA-256
  2. growth     every mission container rebuilt with a longer dialogue table (+DATA.BIN growth) and MOVIE001 swapped
                -> files after DATA.BIN move, ISO9660 and UDF agree on every extent, every other file is untouched
"""
import hashlib, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT, BASE, ORIGINAL_RELEASE, Disc, iso_files, mission_table, mission_relayout, require
from disc import write_disc, plan, file_digest

TEST = ROOT / 'work' / 'output' / '_test'
MOVIE = '/MOVIE0/MOVIE001.PSS'


def image_sha(path):
    d = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(8 << 20), b''):
            d.update(block)
    return d.hexdigest()


def udf_extents(path):
    import pycdlib
    u = pycdlib.PyCdlib(); u.open(str(path)); out = {}
    for parent, _, names in u.walk(udf_path='/'):
        for n in names:
            p = parent.rstrip('/') + '/' + n
            out[p.upper()] = u.get_record(udf_path=p).get_data_length()
    u.close()
    return out


def main():
    TEST.mkdir(parents=True, exist_ok=True)
    out = TEST / 'identity.iso'
    out.unlink(missing_ok=True)
    result = write_disc(BASE, out, {}, {})
    base_sha = image_sha(BASE)
    require(result['sha256'] == base_sha, 'Identity rebuild differs from base')
    out.unlink()
    print('PASS identity rebuild: SHA-256', base_sha, flush=True)

    disc = Disc(BASE)
    grown = {}
    for rid in disc.ids():
        if disc.index.by_id[rid][2] > 4 << 20:
            continue
        data = disc.get(rid)
        mt = mission_table(data)
        if mt:
            at, table = mt
            grown[rid] = mission_relayout(data, {at: table.rebuild({t: s + 'W' * 16 for t, s in table.rows.items()})})
    swaps = {MOVIE: (ORIGINAL_RELEASE, MOVIE)}
    print('plan:', {k: v for k, v in plan(BASE, grown, swaps).items() if k != 'changed_resources'}, flush=True)
    out = TEST / 'growth.iso'
    out.unlink(missing_ok=True)
    result = write_disc(BASE, out, grown, swaps)
    require(result['files_shifted_bytes'] > 0, 'Expected DATA.BIN to grow')
    with BASE.open('rb') as a, out.open('rb') as b, ORIGINAL_RELEASE.open('rb') as o:
        fa, fb, fo = iso_files(a), iso_files(b), iso_files(o)
        for name in fa:
            if name == '/DATA.BIN':
                continue
            src, rec = (o, fo[name]) if name == MOVIE else (a, fa[name])
            require(file_digest(src, rec['offset'], rec['size']) == file_digest(b, fb[name]['offset'], fb[name]['size']),
                    'File content changed: ' + name)
    udf = udf_extents(out)
    require(all(udf[k] == v['size'] for k, v in fb.items()), 'UDF and ISO9660 sizes disagree')
    new = Disc(out)
    for rid in disc.ids():
        if rid not in grown:
            require(disc.index.by_id[rid][2] == new.index.by_id[rid][2], 'Size changed for %d' % rid)
    for rid in list(grown)[:20]:
        require(mission_table(new.get(rid))[1].rows == mission_table(grown[rid])[1].rows, 'Rows differ in %d' % rid)
    new.close()
    out.unlink()
    print('PASS growth rebuild: %d containers grown, files shifted %d bytes, MOVIE001 swapped, ISO9660 = UDF'
          % (len(grown), result['files_shifted_bytes']))


if __name__ == '__main__':
    main()

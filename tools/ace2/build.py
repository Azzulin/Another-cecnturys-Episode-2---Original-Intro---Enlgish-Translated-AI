"""Build an English test ISO of ACE2 from the untouched Special Vocal Version disc.

  python tools/ace2/build.py --version 0.0.1            dry run (plans every change, writes nothing)
  python tools/ace2/build.py --version 0.0.1 --write    writes work/output/ACE2-EN-<version>.iso and a JSON report

Applies:
  text    work/translation/en/<table>.json rows with a non-empty "en" (keyed by the Japanese source), to every copy
          of the table found on the disc (textdb.py). Rows that fail validate.check_row stop the build.
  fonts   printable ASCII completed (fonts.py) in every font/atlas pair (2500/2000, 2501/2001) of the gameplay
          bundles 38000-38006 and the menu bundles 62050-62057
  movie   /MOVIE0/MOVIE001.PSS taken whole from the original 2006 disc (opening with "Glorious");
          --svv-opening keeps the Special Vocal opening (for those without the 2006 disc; swap_movie.py adds it later)
  exe     /SLPS_258.29 with the stack/heap boundary 256 KB higher, so the game's memory arena has room for the
          translation (exe.py; the only change to the executable)
Layout: see disc.py (DATA.BIN may grow; later files move into the empty disc tail; ISO9660 + UDF rewritten).
"""
import argparse, collections, hashlib, json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT, BASE, ORIGINAL_RELEASE, BASE_EXE, Disc, inner_entries, inner_rebuild, require
from textdb import discover, group, patch_resource, _split
from fonts import complete
from validate import check_row, check_counters
from disc import plan, write_disc
import exe

EN = ROOT / 'work' / 'translation' / 'en'
OUT = ROOT / 'work' / 'output'
MOVIE = '/MOVIE0/MOVIE001.PSS'
FONT_PAIRS = [(2500, 2000), (2501, 2001)]
# symbols that may be left out of a nearly full atlas (reported); translations should avoid them
RARE = r'#$@[\]^_`{|}~;*='


def load_translations():
    """{table: {jp: en}} for rows with an English text; raises on rows that fail validation."""
    out, problems = {}, []
    for path in sorted(EN.glob('*.json')):
        doc = json.loads(path.read_text(encoding='utf-8'))
        if 'rows' not in doc:
            continue
        rows = {}
        for r in doc['rows']:
            if not r.get('en'):
                continue
            for p in check_row(r['jp'], r['en'], doc['table']):
                problems.append('%s ids %s: %s' % (doc['table'], r['ids'], p))
            rows[r['jp']] = r['en']
        for p in check_counters(doc['table'], [(r['jp'], r.get('en')) for r in doc['rows']]):
            problems.append('%s: %s' % (doc['table'], p))
        if rows:
            out[doc['table']] = rows
    if problems:
        raise SystemExit('Validation failed:\n  ' + '\n  '.join(problems))
    return out


class Builder:
    def __init__(self, disc):
        self.disc = disc
        self.tr = load_translations()
        self.font_cache = {}
        self.report = {'fonts': [], 'tables': {}}

    def text(self):
        groups = group(discover(self.disc))
        name_of = {loc: name for name, members in groups.items() for loc, _ in members}
        rows_of = {loc: t.rows for name, members in groups.items() for loc, t in members}
        by_resource = collections.defaultdict(list)
        for loc, name in name_of.items():
            if name in self.tr:
                by_resource[_split(loc)[0]].append(loc)
        for name, rows in self.tr.items():
            require(name in groups, 'Translation for unknown table %s' % name)
            members = groups[name]
            jp_rows = {jp for _, t in members for jp in t.rows.values()}
            self.report['tables'][name] = {'translated': len(set(rows) & jp_rows), 'stale': len(set(rows) - jp_rows),
                                           'copies': len(members)}
        new = {}
        for rid, locs in sorted(by_resource.items()):
            data = self.disc.get(rid)
            out = patch_resource(data, locs, lambda loc: self.tr.get(name_of[loc], {}))
            if out != data:
                new[rid] = out
        return new

    def font(self, ccm, tex, where):
        key = hashlib.sha256(ccm + tex).hexdigest()
        if key not in self.font_cache:
            new_ccm, new_tex, r = complete(ccm, tex, optional=RARE)
            self.font_cache[key] = (new_ccm, new_tex)
            self.report['fonts'].append({'where': where, 'ttf': r['calibration']['ttf'], 'size': r['calibration']['size'],
                                         'generated': ''.join(r['generated']), 'cropped': ''.join(r['cropped']),
                                         'skipped': ''.join(r['skipped'])})
        return self.font_cache[key]

    def fonts(self, new):
        for rid in self.disc.ids():
            if not (38000 <= rid < 39000 or 62000 <= rid < 63000):
                continue
            data = new.get(rid) or self.disc.get(rid)
            rows = inner_entries(data)
            if not rows:
                continue
            parts = {e: data[a:b] for e, a, b in rows}
            replace = {}
            for f, t in FONT_PAIRS:
                if f in parts and t in parts:
                    replace[f], replace[t] = self.font(parts[f], parts[t], '%d/%d' % (rid, f))
            if replace:
                new[rid] = inner_rebuild(data, replace)
        return new


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--version', required=True)
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--svv-opening', action='store_true', help='keep the Special Vocal opening (no 2006 disc needed)')
    args = ap.parse_args()
    out = OUT / ('ACE2-EN-%s%s.iso' % (args.version, '-svv-opening' if args.svv_opening else ''))
    require(not out.exists(), 'Output exists: ' + str(out))
    disc = Disc(BASE)
    require(BASE_EXE in disc.files, 'Expected the Special Vocal Version disc (%s)' % BASE_EXE)
    b = Builder(disc)
    t = time.time()
    new = b.fonts(b.text())
    swaps = {} if args.svv_opening else {MOVIE: (ORIGINAL_RELEASE, MOVIE)}
    swaps[BASE_EXE] = exe.patch(exe.read_exe(disc))
    summary = dict(version=args.version, **plan(BASE, new, swaps))
    summary['tables'] = b.report['tables']
    summary['fonts'] = b.report['fonts']
    print(json.dumps({k: v for k, v in summary.items() if k != 'changed_resources'}, ensure_ascii=False, indent=1))
    print('%d resources changed (planned in %.0fs)' % (len(new), time.time() - t))
    if not args.write:
        print('DRY RUN: nothing written. Repeat with --write.')
        return
    print('Writing', out, flush=True)
    result = write_disc(BASE, out, new, swaps)
    summary.update(result, verified=True)
    out.with_suffix('.json').write_text(json.dumps(summary, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('PASS: extents, every file payload and every changed resource verified. SHA-256', result['sha256'])


if __name__ == '__main__':
    main()

"""Merge work/translation/en/_fill/<table>.json ({row index: english}) into <table>.json.

  python tools/ace2/merge_fill.py             merge every fill file (validation problems stop the merge)
  python tools/ace2/merge_fill.py --check     report only, write nothing

Each row is validated (validate.check_row) and its widest line is measured in pixels with the completed game font
(mission dialogue, unit names, HUD) or menu font (briefings, menus, system windows). A line wider than the widest
Japanese line of the same table is reported as WIDE; it is not an error, but it needs a look in the game.
"""
import argparse, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT, BASE, Disc, inner_get
from fonts import complete, FontMap, cp
from validate import check_row
from build import RARE

EN = ROOT / 'work' / 'translation' / 'en'
STRIP = re.compile(r'<[a-z]+\([^)]*\)>|#c\[[0-9A-Fa-f]{6}\]|#c|#i')
FONT_OF_KIND = {'mission': 'game', 'unit_names': 'game', 'hud': 'game'}
LIMITS = ROOT / 'work' / 'ui' / 'limits.json'


def limit_for(kind, jp_max):
    """Measured width limit of a text kind (work/ui/limits.json), else the widest Japanese line of the table."""
    try:
        return json.loads(LIMITS.read_text(encoding='utf-8'))[kind]['width']
    except (FileNotFoundError, KeyError, TypeError):
        return jp_max


def load_fonts():
    disc = Disc(BASE)
    out = {}
    for name, rid in (('game', 38000), ('menu', 62050)):
        bundle = disc.get(rid)
        out[name] = FontMap(complete(inner_get(bundle, 2500), inner_get(bundle, 2000), optional=RARE)[0])
    return out


def widths(fm, text):
    out = []
    for line in STRIP.sub('', text.replace('%d', '000').replace('%s', 'XXXXXX')).split('\n'):
        w = 0
        for ch in line:
            try:
                idx = fm.map.get(cp(ch))
            except UnicodeEncodeError:  # not in cp932 (em dash...): the validator reports it; measure as a full cell
                idx = None
            w += fm.height if idx is None else fm.records[idx][6]
        out.append(w)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    fonts = load_fonts()
    problems = 0
    for fill in sorted((EN / '_fill').glob('*.json')):
        name = fill.stem
        doc_path = EN / (name + '.json')
        doc = json.loads(doc_path.read_text(encoding='utf-8'))
        values = json.loads(fill.read_text(encoding='utf-8'))
        fm = fonts[FONT_OF_KIND.get(doc['kind'], 'menu')]
        jp_max = max(max(widths(fm, r['jp'])) for r in doc['rows'])
        limit = limit_for(doc['kind'], jp_max)
        wide = 0
        for key, en in values.items():
            i = int(key)
            if not 0 <= i < len(doc['rows']):
                print('INDEX %s[%s] out of range (%d rows)' % (name, key, len(doc['rows']))); problems += 1; continue
            row = doc['rows'][i]
            for p in check_row(row['jp'], en):
                print('ERROR %s[%d]: %s' % (name, i, p)); problems += 1
            ew, jw = max(widths(fm, en)), max(widths(fm, row['jp']))
            if ew > max(limit, jw):
                print('WIDE  %s[%d] %dpx (limit %d, row JP %d): %r' % (name, i, ew, limit, jw, en)); wide += 1
            row['en'] = en
        if not args.check and not problems:
            doc_path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('%s %s: %d rows, %d wide; width limit %dpx' % ('checked' if args.check else 'merged', name, len(values), wide, limit))
    if problems:
        raise SystemExit('%d problems: nothing merged for the failing tables' % problems)


if __name__ == '__main__':
    main()

"""Pixel widths of translated rows with the completed game/menu fonts (read-only; used for the 0.0.9 menu-label test).

  python tools/research/label_widths.py table menu3070 hud3013     every row: JP px, EN px, text
  python tools/research/label_widths.py over [141]                 one-line menu rows with JP <= px < EN (labels that
                                                                   may vanish; limit in work/ui/limits.json menu_label)
  python tools/research/label_widths.py try menu "Back to Menu" ... measure candidate texts (font: menu or game)
  python tools/research/label_widths.py source menu3070#8 ...      where a row comes from (agent batch or automatic
                                                                   row) and any reviewer fix already recorded

Run with PYTHONIOENCODING=utf-8 on Windows.
"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'ace2'))
from merge_fill import load_fonts, widths, EN, FONT_OF_KIND

TR = ROOT / 'work' / 'translation'


def px(fm, text):
    return max(widths(fm, text))


def table(names):
    fonts = load_fonts()
    for t in names:
        d = json.loads((EN / (t + '.json')).read_text(encoding='utf-8'))
        fm = fonts[FONT_OF_KIND.get(d['kind'], 'menu')]
        print('==', t, d['kind'], d.get('copies'))
        for i, r in enumerate(d['rows']):
            print('[%3d] jp %3d en %3d  %r  <- %r' % (i, px(fm, r['jp']), px(fm, r['en'] or r['jp']), r['en'], r['jp']))


def over(limit):
    fm = load_fonts()['menu']
    n = 0
    for p in sorted(EN.glob('menu*.json')):
        for i, r in enumerate(json.loads(p.read_text(encoding='utf-8'))['rows']):
            if not r.get('en') or '\n' in r['jp']:
                continue
            jw, ew = px(fm, r['jp']), px(fm, r['en'])
            if jw <= limit < ew:
                n += 1
                print('%s#%d jp %d en %d  %r <- %r' % (p.stem, i, jw, ew, r['en'], r['jp']))
    print(n, 'rows')


def try_texts(font, texts):
    fm = load_fonts()[font]
    for s in texts:
        print('%3d %s' % (px(fm, s), s))


def source(refs):
    where = {}
    for p in (TR / 'agent' / 'batches').glob('*.json'):
        for r in json.loads(p.read_text(encoding='utf-8'))['rows']:
            if r['ref'] in refs:
                where[r['ref']] = 'batch ' + p.stem
    for p in (TR / 'auto').glob('*.json'):
        if p.stem == 'overrides':
            continue
        for k, v in json.loads(p.read_text(encoding='utf-8'))['rows'].items():
            if k in refs:
                where.setdefault(k, 'auto %s %s' % (p.stem, v))
    fixes = json.loads((TR / 'agent' / 'reviewer_fixes.json').read_text(encoding='utf-8'))
    for r in refs:
        print(r, where.get(r, 'not in batches/auto (hand-filled _fill?)'),
              'fix:', [(lote, d[r]) for lote, d in fixes.items() if isinstance(d, dict) and r in d])


if __name__ == '__main__':
    mode, args = sys.argv[1], sys.argv[2:]
    if mode == 'table':
        table(args)
    elif mode == 'over':
        over(int(args[0]) if args else 141)
    elif mode == 'try':
        try_texts(args[0], args[1:])
    elif mode == 'source':
        source(args)
    else:
        raise SystemExit(__doc__)

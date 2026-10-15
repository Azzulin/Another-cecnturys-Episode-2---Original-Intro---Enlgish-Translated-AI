"""Re-break the lines of fill translations to fit a pixel width (layout only; the words are never changed).

  python tools/ace2/rewrap.py <table> [--width PX] [--lines N] [--write]

Width defaults to the widest Japanese line of the table, measured with the completed font (merge_fill.widths);
the line limit defaults to max(2, Japanese line count) per row. Rows that cannot fit are listed so the text can be
tightened by hand. Without --write nothing is changed.
"""
import argparse, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from merge_fill import EN, load_fonts, widths, FONT_OF_KIND, limit_for

TAG = re.compile(r'(<[a-z]+\([^)]*\)>)')


def wrap(fm, text, width, max_lines):
    """Greedy word wrap of the visible text; tags stay attached to the following/preceding word."""
    lead = re.match(r'^(?:<[a-z]+\([^)]*\)>)*', text).group()
    trail = re.search(r'(?:<[a-z]+\([^)]*\)>)*$', text[len(lead):]).group()
    body = text[len(lead):len(text) - len(trail)] if trail else text[len(lead):]
    if body.endswith('\n'):  # an intentional trailing break (sentence continues in the next row) is kept
        return None
    words = body.replace('\n', ' ').split(' ')
    lines, cur = [], ''
    for w in words:
        cand = (cur + ' ' + w) if cur else w
        if cur and max(widths(fm, cand)) > width:
            lines.append(cur); cur = w
        else:
            cur = cand
    lines.append(cur)
    if len(lines) > max_lines or any(max(widths(fm, l)) > width for l in lines):
        return None
    return lead + '\n'.join(lines) + trail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('table')
    ap.add_argument('--width', type=int)
    ap.add_argument('--lines', type=int)
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    doc = json.loads((EN / (args.table + '.json')).read_text(encoding='utf-8'))
    fill_path = EN / '_fill' / (args.table + '.json')
    fill = json.loads(fill_path.read_text(encoding='utf-8'))
    fm = load_fonts()[FONT_OF_KIND.get(doc['kind'], 'menu')]
    limit = args.width or limit_for(doc['kind'], max(max(widths(fm, r['jp'])) for r in doc['rows']))
    changed = failed = 0
    for key, en in fill.items():
        jp = doc['rows'][int(key)]['jp']
        if max(widths(fm, en)) <= limit:
            continue
        lines = args.lines or max(2, jp.count('\n') + 1)
        new = wrap(fm, en, limit, lines)
        if new is None:
            print('NO FIT %s[%s] (%dpx > %d, max %d lines): %r' % (args.table, key, max(widths(fm, en)), limit, lines, en)); failed += 1
        else:
            print('wrap   %s[%s]: %r' % (args.table, key, new)); fill[key] = new; changed += 1
    if args.write:
        fill_path.write_text(json.dumps(fill, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%s: width %dpx, %d re-wrapped, %d need manual tightening%s' % (args.table, limit, changed, failed, '' if args.write else ' (dry run)'))


if __name__ == '__main__':
    main()

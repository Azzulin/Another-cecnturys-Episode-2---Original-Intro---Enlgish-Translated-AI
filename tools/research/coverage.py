"""Coverage of the text tables: rows with English in _fill vs rows that need it (read-only)."""
import json, re, sys
from pathlib import Path
from collections import defaultdict
EN = Path(r'D:\Ace 2\work\translation\en')
OPS = json.loads(Path(r'D:\Ace 2\work\translation\operations.json').read_text(encoding='utf-8'))
JPN = re.compile(r'[\u3000-\u9fff\uff00-\uffef]')
STRIP = re.compile(r'<[a-z]+\([^)]*\)>|#c\[[0-9A-Fa-f]{6}\]|#c|#i|%[-0-9]*[ds]')
op_tables = {}
ops = OPS['operations'] if isinstance(OPS, dict) and 'operations' in OPS else OPS
def tables_of(op):
    s = set()
    def rec(x):
        if isinstance(x, str) and re.fullmatch(r'(brief|m)\d+', x): s.add(x)
        elif isinstance(x, dict): [rec(v) for v in x.values()]
        elif isinstance(x, list): [rec(v) for v in x]
    rec(op); return s
for i, op in enumerate(ops if isinstance(ops, list) else ops.values()):
    for t in tables_of(op): op_tables[t] = i + 1
def group(name, kind):
    if name in op_tables: return 'campanha'
    n = int(re.sub(r'\D', '', name) or 0)
    if kind == 'mission':
        if 6005 <= n <= 6010: return 'xa missoes extras'
        if 6302 <= n <= 6303: return 'xb tutorial'
        if 6320 <= n <= 6325: return 'xc flashbacks'
        return 'xd missoes curtas/sistema'
    if kind == 'brief': return 'briefings fora das ops'
    return kind
tot = defaultdict(lambda: [0, 0]); missing = defaultdict(list)
for p in sorted(EN.glob('*.json')):
    doc = json.loads(p.read_text(encoding='utf-8'))
    if 'rows' not in doc: continue
    fp = EN / '_fill' / p.name
    fill = json.loads(fp.read_text(encoding='utf-8')) if fp.exists() else {}
    g = group(p.stem, doc.get('kind'))
    for i, r in enumerate(doc['rows']):
        jp = r.get('jp') or ''
        if not JPN.search(STRIP.sub('', jp)): continue  # nothing to translate (empty, ASCII, codes only)
        tot[g][0] += 1
        if str(i) in fill: tot[g][1] += 1
        else: missing[g].append('%s#%d' % (p.stem, i))
for g, (n, d) in sorted(tot.items()):
    print('%-28s %5d / %5d  faltam %5d' % (g, d, n, n - d))
json.dump(missing, open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=0) if len(sys.argv) > 1 else None

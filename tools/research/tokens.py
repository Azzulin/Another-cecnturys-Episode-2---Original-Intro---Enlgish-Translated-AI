"""Survey control tokens across all text, and what mission sub-tables contain (research only)."""
import sys, collections, re
sys.path.insert(0, r"D:\Ace 2\tools\ace2")
from ace2lib import BASE, Disc, inner_entries, try_unpack, TextTable, mission_table, small_tables
d = Disc(BASE)
tags = collections.Counter(); other = collections.Counter(); subs = collections.defaultdict(collections.Counter)
TAG = re.compile(r'<([a-z]+)\(([^)]*)\)>')
def scan(text):
    for m in TAG.finditer(text): tags['<%s()>' % m.group(1)] += 1
    for m in re.finditer(r'#c\[[0-9A-Fa-f]+\]|#c|%[-0-9.]*[a-z%]|\[a-z]|[<>{}\[\]$@^]', TAG.sub('', text)): other[m.group()[:2] if m.group().startswith('#c[') else m.group()] += 1
    for ch in TAG.sub('', text):
        o = ord(ch)
        if 0x2460 <= o <= 0x24ff or 0x3200 <= o <= 0x33ff or 0x2190 <= o <= 0x21ff or ch in '○×△□': other['sym ' + ch] += 1
def walk(data, depth):
    mt = mission_table(data)
    if mt:
        for v in mt[1].rows.values(): scan(v)
        for sid, off, t in small_tables(data):
            subs[sid]['tables'] += 1
            for v in list(t.rows.values())[:2]: subs[sid][v] += 1
        return
    if data[:4] == b'\0\0\1\0':
        try:
            for v in TextTable(data).rows.values(): scan(v)
            return
        except (ValueError, UnicodeError): pass
    p = try_unpack(data) if depth < 4 else None
    if p is not None: walk(p, depth + 1); return
    r = inner_entries(data)
    if r and depth < 4:
        for e, a, b in r: walk(data[a:b], depth + 1)
for rid in d.ids():
    if d.index.by_id[rid][2] <= 64 << 20: walk(d.get(rid), 0)
print('TAGS', tags.most_common()); print('OTHER', other.most_common(80))
for sid, c in subs.items(): print('SUB', sid, c.most_common(8))

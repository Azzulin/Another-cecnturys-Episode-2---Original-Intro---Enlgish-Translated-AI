"""List every text table outside mission containers with its path and a sample (research only)."""
import sys, collections, re
sys.path.insert(0, r"D:\Ace 2\tools\ace2")
from ace2lib import BASE, Disc, inner_entries, try_unpack, TextTable, mission_table
JPC = re.compile(r'[\u3040-\u30ff\u4e00-\u9fff]')
d = Disc(BASE)
def walk(data, path, depth, out):
    if mission_table(data): return
    if data[:4] == b'\0\0\1\0':
        try: out.append((path, TextTable(data))); return
        except (ValueError, UnicodeError): pass
    p = try_unpack(data) if depth < 4 else None
    if p is not None: walk(p, path + ':lz', depth + 1, out); return
    r = inner_entries(data)
    if r and depth < 4:
        for e, a, b in r: walk(data[a:b], '%s/%d' % (path, e), depth + 1, out)
found = []
for rid in d.ids():
    if d.index.by_id[rid][2] > 64 << 20: continue
    walk(d.get(rid), str(rid), 0, found)
# group identical tables (copies)
groups = collections.OrderedDict()
for path, t in found:
    key = tuple(sorted(t.rows.items()))
    groups.setdefault(key, []).append(path)
print('tables', len(found), 'distinct', len(groups))
for key, paths in groups.items():
    rows = dict(key); jp = [v for v in rows.values() if JPC.search(v)]
    if not jp: continue
    sample = ' | '.join(v.replace('\n', '/')[:40] for v in jp[:3])
    print('%-40s x%-2d rows=%4d jp=%4d  %s' % (paths[0] + (' (+%s)' % ','.join(paths[1:4]) if len(paths) > 1 else ''), len(paths), len(rows), len(jp), sample[:120]))

"""Which mission containers exist on each disc, and how 6xxx and 42xxx variants relate."""
import sys, collections
sys.path.insert(0, r"D:\Ace 2\tools\ace2")
from ace2lib import BASE, ORIGINAL_RELEASE, Disc, mission_table
s, o = Disc(BASE), Disc(ORIGINAL_RELEASE)
def missions(d):
    return {r: mission_table(d.get(r)) for r in d.ids() if d.index.by_id[r][2] < 4 << 20 and mission_table(d.get(r))}
ms, mo = missions(s), missions(o)
ranges = lambda m: collections.Counter(r // 1000 for r in m)
print('SVV missions by range', ranges(ms)); print('ORIG missions by range', ranges(mo))
same_rows = diff_rows = 0; examples = []
for r in sorted(ms):
    if r < 7000 and r + 36000 in ms:
        a, b = ms[r][1].rows, ms[r + 36000][1].rows
        if a == b: same_rows += 1
        else:
            diff_rows += 1
            if len(examples) < 3:
                dk = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
                examples.append((r, len(dk), [(k, a.get(k), b.get(k)) for k in sorted(dk)[:3]]))
print('6xxx/42xxx pairs with identical rows', same_rows, 'different', diff_rows)
for e in examples: print(e)
# svv 6xxx vs orig 6xxx
eq = sum(1 for r in ms if r in mo and ms[r][1].rows == mo[r][1].rows)
print('SVV vs ORIG same id identical rows:', eq, 'of', len([r for r in ms if r in mo]))
only6 = [r for r in ms if r < 7000 and r + 36000 not in ms]; only42 = [r for r in ms if r >= 42000 and r - 36000 not in ms]
print('6xxx without 42xxx pair', only6[:20], '42xxx without pair', only42[:20])
print('other ranges', sorted(r for r in ms if not (6000 <= r < 7000 or 42000 <= r < 43000))[:40])

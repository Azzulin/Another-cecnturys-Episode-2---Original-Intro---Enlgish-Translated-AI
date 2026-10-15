"""Census of textures in DATA.BIN (read-only): walks every resource, unpacks LZSS, recurses into inner binders."""
import json, struct, sys, time
sys.path.insert(0, r'D:\Ace 2\tools\ace2')
from ace2lib import Disc, try_unpack, inner_entries, u32
BPP = {0: 32, 1: 24, 2: 16, 10: 16, 19: 8, 20: 4, 27: 8, 36: 4, 44: 4}
OUT = sys.argv[1]

def texinfo(b):
    if len(b) < 48: return None
    n, mode = u32(b, 4), u32(b, 12)
    tex0 = struct.unpack_from('<Q', b, 16)[0]
    psm = (tex0 >> 20) & 63; w = 1 << ((tex0 >> 26) & 15); h = 1 << ((tex0 >> 30) & 15)
    if psm not in BPP or mode not in (0, 1) or not (8 <= w <= 1024 and 8 <= h <= 1024): return None
    if n != w * h * BPP[psm] // 8 or 32 + n > len(b): return None
    return {'psm': psm, 'w': w, 'h': h, 'mode': mode, 'n': n, 'len': len(b)}

def walk(b, path, out, depth=0):
    t = texinfo(b)
    if t:
        out.append(dict(t, path=path)); return
    if b[:4] == b'TIM2':
        out.append({'tim2': True, 'path': path, 'len': len(b)}); return
    ents = inner_entries(b)
    if ents and depth < 4:
        for eid, a, e in ents:
            sub = b[a:e]
            p = try_unpack(sub)
            walk(p if p else sub, path + [eid], out, depth + 1)

d = Disc(); res = []; t0 = time.time()
for k, rid in enumerate(d.ids()):
    raw = d.get(rid)
    p = try_unpack(raw)
    walk(p if p else raw, [rid], res)
    if k % 500 == 0: print(k, rid, len(res), int(time.time() - t0), flush=True)
json.dump(res, open(OUT, 'w'), indent=0)
print('done', len(res), int(time.time() - t0))

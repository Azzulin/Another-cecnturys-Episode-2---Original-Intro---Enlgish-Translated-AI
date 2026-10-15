"""Decode census textures to PNG contact sheets (read-only on the disc)."""
import json, struct, sys
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, r'D:\Ace 2\tools\ace2')
from ace2lib import Disc, try_unpack, inner_entries, u32
from fonts import address4, address32
CT8 = [[0,4,16,20,32,36,48,52,2,6,18,22,34,38,50,54],[8,12,24,28,40,44,56,60,10,14,26,30,42,46,58,62],
       [33,37,1,5,49,53,17,21,35,39,3,7,51,55,19,23],[41,45,9,13,57,61,25,29,43,47,11,15,59,63,27,31],
       [96,100,112,116,64,68,80,84,98,102,114,118,66,70,82,86],[104,108,120,124,72,76,88,92,106,110,122,126,74,78,90,94],
       [65,69,81,85,97,101,113,117,67,71,83,87,99,103,115,119],[73,77,89,93,105,109,121,125,75,79,91,95,107,111,123,127],
       [128,132,144,148,160,164,176,180,130,134,146,150,162,166,178,182],[136,140,152,156,168,172,184,188,138,142,154,158,170,174,186,190],
       [161,165,129,133,177,181,145,149,163,167,131,135,179,183,147,151],[169,173,137,141,185,189,153,157,171,175,139,143,187,191,155,159],
       [224,228,240,244,192,196,208,212,226,230,242,246,194,198,210,214],[232,236,248,252,200,204,216,220,234,238,250,254,202,206,218,222],
       [193,197,209,213,225,229,241,245,195,199,211,215,227,231,243,247],[201,205,217,221,233,237,249,253,203,207,219,223,235,239,251,255]]
BT32 = [[0,1,4,5,16,17,20,21],[2,3,6,7,18,19,22,23],[8,9,12,13,24,25,28,29],[10,11,14,15,26,27,30,31]]
def address8(x, y, w):
    page = y // 64 * (w // 128) + x // 128
    block = BT32[y // 16 % 4][x // 16 % 8]
    return page * 8192 + block * 256 + CT8[y % 16][x % 16]

def get(d, path):
    b = d.get(path[0]); p = try_unpack(b); b = p or b
    for eid in path[1:]:
        a, e = next((a, e) for i, a, e in inner_entries(b) if i == eid)
        s = b[a:e]; p = try_unpack(s); b = p or s
    return b

def decode(t, b):
    w, h, psm, mode, n = t['w'], t['h'], t['psm'], t['mode'], t['n']
    raw = b[32:32 + n]
    if psm in (0, 1):
        if psm != 0: return None
        if mode == 1:
            vram = bytearray(n)
            for y in range(h):
                for x in range(w):
                    a = address32(x, y, w); s = (y * w + x) * 4; vram[a:a+4] = raw[s:s+4]
            raw = bytes(vram)  # best effort
        px = np.frombuffer(raw, np.uint8).reshape(h, w, 4).copy()
        px[..., 3] = np.minimum(255, px[..., 3].astype(int) * 2)
        return Image.fromarray(px, 'RGBA')
    if psm in (19, 20):
        bpp = 8 if psm == 19 else 4
        npal = 256 if bpp == 8 else 16
        pal = np.frombuffer(b[32 + n:32 + n + npal * 4], np.uint8)
        if len(pal) < npal * 4: return None
        pal = pal.reshape(npal, 4).copy()
        if bpp == 8:  # CSM1 swizzle
            pal = pal.reshape(8, 2, 2, 8, 4).transpose(0, 2, 1, 3, 4).reshape(256, 4)
        pal[:, 3] = np.minimum(255, pal[:, 3].astype(int) * 2)
        if mode == 0:
            if bpp == 8: idx = np.frombuffer(raw, np.uint8).reshape(h, w)
            else:
                q = np.frombuffer(raw, np.uint8); idx = np.stack([q & 15, q >> 4], -1).reshape(h, w)
        else:
            tw, th = (w // 2, h // 2) if bpp == 8 else (w // 2, h // 4)
            vram = bytearray(n)
            for y in range(th):
                for x in range(tw):
                    a = address32(x, y, tw); s = (y * tw + x) * 4; vram[a:a+4] = raw[s:s+4]
            idx = np.zeros((h, w), np.uint8)
            for y in range(h):
                for x in range(w):
                    if bpp == 8: idx[y, x] = vram[address8(x, y, w)]
                    else:
                        a = address4(x, y, w); idx[y, x] = (vram[a // 2] >> ((a & 1) * 4)) & 15
        return Image.fromarray(pal[idx], 'RGBA')
    return None

if __name__ == '__main__':
    census, outdir = json.load(open(sys.argv[1])), sys.argv[2]
    sel = [t for t in census if 'w' in t and (not sys.argv[3:] or str(t['path'][0]) in sys.argv[3].split(','))]
    d = Disc()
    for t in sel:
        try:
            img = decode(t, get(d, t['path']))
        except Exception as e:
            print('fail', t['path'], e); continue
        if img is None: continue
        bg = Image.new('RGBA', img.size, (40, 40, 60, 255)); bg.alpha_composite(img)
        bg.convert('RGB').save('%s/%s.png' % (outdir, '_'.join(map(str, t['path']))))
    print('ok', len(sel))

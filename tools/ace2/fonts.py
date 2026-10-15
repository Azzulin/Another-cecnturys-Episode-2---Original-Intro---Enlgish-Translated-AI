"""Complete printable ASCII in an ACE2 font (font map + 4-bit atlas) without touching any original glyph.

Adapted from the ACE1 tool (D:\\Ace 1\\tools\\ace1\\fonts.py). ACE2 fonts differ from ACE1's in two ways:
  - coverage lives in the palette luminance (every ink entry has alpha 128, grey 32..~180), not in the alpha;
  - every glyph carries a dark 1-px outline (the darkest opaque entry) around its ink, 4-connected (no diagonals).

Per code 0x20-0x7E:
  native ASCII glyph      -> kept as is
  fullwidth glyph exists  -> new record on the same pixels, cropped to ink+outline plus the native side bearing
                             (digits share one width so numbers stay tabular)
  nothing                 -> rendered from the TrueType face that best matches the native glyphs (picked by pixel
                             comparison among CANDIDATES, sized by the native cap height), quantized to the palette
                             ink levels, outlined like the natives and written into free atlas space
Record layout (24 bytes): 4 floats UV (l, t, r, b) + int16 (offset, width, advance, 0).
"""
import os, struct
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from ace2lib import u32, require, align

FONTS = Path(os.environ.get('ACE2_FONTS', r'C:\Windows\Fonts'))  # folder holding the CANDIDATES (Windows fonts)
CANDIDATES = ['CENTURY.TTF', 'times.ttf', 'georgia.ttf', 'YuGothR.ttc', 'YuGothM.ttc', 'YuGothB.ttc', 'msgothic.ttc',
              'arial.ttf', 'segoeui.ttf']
# fullwidth forms of these are em-sized or styled differently; draw them instead of cropping
FORCE_GENERATE = set('/~\'')
# Japanese fonts draw U+005C as a yen sign; take the backslash from a Latin font
LATIN_FALLBACK = {'\\': 'segoeui.ttf'}
PROBES = 'HEFTLIMNRkbdhlnmu'


# ---------------------------------------------------------------- GS texture codec (PCSX2 GSTables layout, as in ACE3)

def address4(x, y, width):
    page = y // 128 * (width // 128) + x // 128
    bx, by = x // 32 % 4, y // 16 % 8
    block = (bx & 1) * 2 + (bx & 2) * 4 + (by & 1) + (by & 2) * 2 + (by & 4) * 4
    column = ((x & 1) << 3) | ((x & 2) << 4) | ((((x >> 2) ^ (y >> 1) ^ (y >> 2)) & 1) << 6)
    column |= ((x & 24) >> 2) | ((y & 1) << 4) | ((y & 2) >> 1) | ((y & 4) << 5) | ((y & 8) << 5)
    return page * 16384 + block * 512 + column


def address32(x, y, width):
    page = y // 32 * (width // 64) + x // 64
    bx, by = x // 8 % 8, y // 8 % 4
    block = (bx & 1) + (bx & 2) * 2 + (bx & 4) * 4 + (by & 1) * 2 + (by & 2) * 4
    column = (x & 1) + (x & 6) * 2 + (y & 1) * 2 + (y & 6) * 8
    return (page * 2048 + block * 64 + column) * 4


class Atlas:
    """4-bit atlas (PSMT4 / PSMT4HH, linear or uploaded as swizzled PSMCT32) with a luminance-coded palette."""

    def __init__(self, tex):
        self.tex = bytes(tex)
        tex0 = struct.unpack_from('<Q', tex, 16)[0]
        self.psm = (tex0 >> 20) & 63
        self.w, self.h = 1 << ((tex0 >> 26) & 15), 1 << ((tex0 >> 30) & 15)
        self.mode, n = u32(tex, 12), u32(tex, 4)
        require(self.psm in (20, 44) and n == self.w * self.h // 2, 'Expected a 4-bit font atlas')
        require(self.mode in (0, 1), 'Unknown upload mode')
        self.palette = [tuple(tex[32 + n + i * 4:32 + n + i * 4 + 4]) for i in range(16)]
        raw = tex[32:32 + n]
        if self.mode == 0:
            px = np.frombuffer(raw, dtype=np.uint8)
            self.px = np.stack([px & 15, px >> 4], -1).reshape(self.h, self.w).copy()
        else:
            tw = self.w // 2
            vram = bytearray(n)
            for y in range(self.h // 4):
                for x in range(tw):
                    a = address32(x, y, tw); s = (y * tw + x) * 4
                    vram[a:a + 4] = raw[s:s + 4]
            self.px = np.zeros((self.h, self.w), dtype=np.uint8)
            for y in range(self.h):
                for x in range(self.w):
                    a = address4(x, y, self.w)
                    self.px[y, x] = (vram[a // 2] >> ((a & 1) * 4)) & 15
        used = set(np.unique(self.px).tolist())
        opaque = [i for i, c in enumerate(self.palette) if c[3] and i in used]
        require(opaque, 'Atlas has no opaque entries')
        lo = min(self.palette[i][0] for i in opaque)
        hi = max(self.palette[i][0] for i in opaque)
        self.transparent = next(i for i, c in enumerate(self.palette) if c[3] == 0)
        self.outline = min(opaque, key=lambda i: self.palette[i][0])
        # coverage of every palette entry (0 for transparent and outline)
        self.level = np.zeros(16, np.float32)
        self.inks = []
        for i in opaque:
            if i != self.outline:
                self.level[i] = (self.palette[i][0] - lo) / max(1, hi - lo)
                self.inks.append(i)

    def encode(self):
        n = self.w * self.h // 2
        if self.mode == 0:
            flat = self.px.reshape(-1)
            raw = (flat[0::2] | (flat[1::2] << 4)).astype(np.uint8).tobytes()
        else:
            vram = bytearray(n)
            for y in range(self.h):
                for x in range(self.w):
                    a = address4(x, y, self.w)
                    vram[a // 2] |= int(self.px[y, x]) << ((a & 1) * 4)
            tw = self.w // 2
            raw = bytearray(n)
            for y in range(self.h // 4):
                for x in range(tw):
                    s = address32(x, y, tw); t = (y * tw + x) * 4
                    raw[t:t + 4] = vram[s:s + 4]
            raw = bytes(raw)
        return self.tex[:32] + raw + self.tex[32 + n:]

    def coverage(self):
        return self.level[self.px]


# ---------------------------------------------------------------- font map

class FontMap:
    def __init__(self, data):
        require(data[:4] == b'\0\0\1\0', 'Not a font map')
        self.data = bytes(data)
        self.height = u32(data, 8)
        count, gcount, ranges, glyphs = struct.unpack_from('<HHII', data, 16)
        require(ranges == 32, 'Unexpected font map layout')
        self.map = {}
        for i in range(count):
            a, b, idx = struct.unpack_from('<III', data, ranges + i * 12)
            for c in range(a, b + 1):
                self.map[c] = idx + c - a
        self.records = [struct.unpack_from('<4f4h', data, glyphs + i * 24) for i in range(gcount)]
        self.tail = data[glyphs + gcount * 24:u32(data, 4)]
        require(not self.tail, 'Unexpected data after glyph records')

    def build(self, mapping, records):
        ranges = []
        for code, index in sorted(mapping.items()):
            if ranges and code == ranges[-1][1] + 1 and index == ranges[-1][2] + code - ranges[-1][0]:
                ranges[-1][1] = code
            else:
                ranges.append([code, code, index])
        out = bytearray(self.data[:32])
        for r in ranges:
            out.extend(struct.pack('<3I', *r))
        start = len(out)
        for r in records:
            out.extend(struct.pack('<4f4h', *r))
        struct.pack_into('<I', out, 4, len(out))
        struct.pack_into('<HH', out, 16, len(ranges), len(records))
        struct.pack_into('<I', out, 24, start)
        out.extend(bytes(align(len(out), 32) - len(out)))
        return bytes(out)


def cp(ch):
    return int.from_bytes(ch.encode('cp932'), 'big')


def fullwidth(ch):
    return '\u2019' if ch == "'" else ('\u3000' if ch == ' ' else chr(ord(ch) + 0xFEE0))


def ink(a, thr=0.12):
    ys, xs = np.where(a > thr)
    return (int(ys.min()), int(ys.max()), int(xs.min()), int(xs.max())) if len(ys) else None


def cell(fm, atlas, cov, index):
    l, t, r, b = fm.records[index][:4]
    x0, y0, x1, y1 = round(l * atlas.w), round(t * atlas.h), round(r * atlas.w), round(b * atlas.h)
    return cov[y0:y1, x0:x1]


def cell_px(fm, atlas, index):
    l, t, r, b = fm.records[index][:4]
    return atlas.px[round(t * atlas.h):round(b * atlas.h), round(l * atlas.w):round(r * atlas.w)]


def outline(mask):
    """4-connected 1-px ring around mask (the native outline shape)."""
    m = np.pad(mask, 1)
    ring = m[:-2, 1:-1] | m[2:, 1:-1] | m[1:-1, :-2] | m[1:-1, 2:]
    return ring & ~mask


# ---------------------------------------------------------------- rendering and calibration

class Renderer:
    def __init__(self, ttf, size, height, baseline):
        self.font = ImageFont.truetype(str(FONTS / ttf), size)
        self.ttf, self.size, self.height, self.baseline = ttf, size, height, baseline

    def glyph(self, ch):
        """(coverage HxW cell including side bearings, advance)."""
        adv = max(1, round(self.font.getlength(ch)))
        pad = self.height
        im = Image.new('L', (adv + 2 * pad, self.height), 0)
        ImageDraw.Draw(im).text((pad, self.baseline), ch, font=self.font, fill=255, anchor='ls')
        a = np.asarray(im, dtype=np.float32) / 255.0
        box = ink(a, 0.02)
        if box is None:
            return np.zeros((self.height, adv), np.float32), adv
        left, right = min(box[2], pad), max(box[3] + 1, pad + adv)
        return a[:, left:right], adv + (pad - left if left < pad else 0)


def native_cell(fm, atlas, cov, ch):
    for code in (ord(ch), cp(fullwidth(ch))):
        if code in fm.map:
            return cell(fm, atlas, cov, fm.map[code])
    return None


def compare(native, rendered):
    """Pixel distance between two coverage cells, aligned on the ink box (lower is better)."""
    bn, br = ink(native), ink(rendered)
    if bn is None or br is None:
        return 9.0
    a = native[bn[0]:bn[1] + 1, bn[2]:bn[3] + 1]
    b = rendered[br[0]:br[1] + 1, br[2]:br[3] + 1]
    h, w = max(a.shape[0], b.shape[0]), max(a.shape[1], b.shape[1])
    pa = np.zeros((h, w), np.float32); pa[h - a.shape[0]:, :a.shape[1]] = a
    pb = np.zeros((h, w), np.float32); pb[h - b.shape[0]:, :b.shape[1]] = b
    return float(np.abs(pa - pb).mean()) + 0.05 * (abs(a.shape[0] - b.shape[0]) + abs(a.shape[1] - b.shape[1]))


def calibrate(fm, atlas, cov, candidates=CANDIDATES):
    """Pick the TrueType face and size whose glyphs best match the native ones (cap height from the native 'H')."""
    probe = next(ch for ch in 'HEILTFNMKZXVW' if native_cell(fm, atlas, cov, ch) is not None)
    box = ink(native_cell(fm, atlas, cov, probe))
    cap, baseline = box[1] - box[0] + 1, box[1] + 1
    probes = [c for c in PROBES if native_cell(fm, atlas, cov, c) is not None]
    results = []
    for ttf in candidates:
        if not (FONTS / ttf).exists():
            continue
        size = min(range(fm.height // 2, fm.height * 2),
                   key=lambda s: abs((lambda b: b[1] - b[0] + 1)(ink(Renderer(ttf, s, fm.height, baseline).glyph(probe)[0])) - cap))
        r = Renderer(ttf, size, fm.height, baseline)
        score = float(np.mean([compare(native_cell(fm, atlas, cov, c), r.glyph(c)[0]) for c in probes]))
        results.append((score, ttf, size, r))
    results.sort(key=lambda x: x[0])
    best = results[0]
    return best[3], {'cap_height': cap, 'baseline': baseline, 'ttf': best[1], 'size': best[2],
                     'probes': ''.join(probes), 'scores': {t: round(s, 4) for s, t, _, _ in results}}


# ---------------------------------------------------------------- completion

def complete(ccm, tex, candidates=CANDIDATES, optional=''):
    """optional: characters that may be left out (reported) when the atlas has no room for them."""
    fm, atlas = FontMap(ccm), Atlas(tex)
    cov = atlas.coverage()
    renderer, calib = calibrate(fm, atlas, cov, candidates)
    H = fm.height
    inks = sorted(atlas.inks, key=lambda i: atlas.level[i])
    zero, ring = atlas.transparent, atlas.outline

    def to_bitmap(c):
        """Quantize coverage to the ink entries and add the native outline; 1-px transparent margin."""
        c = np.pad(c, ((0, 0), (1, 1)))
        mask = c > 0.08
        out = np.full(c.shape, zero, np.uint8)
        for y, x in zip(*np.where(mask)):
            out[y, x] = min(inks, key=lambda i: abs(atlas.level[i] - c[y, x]))
        out[outline(mask)] = ring
        return out

    # rects: union of every glyph rectangle; inked: every non-transparent pixel. A new cell may overlap the transparent
    # part of another cell, but no ink (its own or another's, +1 px guard) may fall inside a foreign rectangle.
    rects = np.zeros((atlas.h, atlas.w), bool)
    for rec in fm.records:
        x0, y0, x1, y1 = round(rec[0] * atlas.w), round(rec[1] * atlas.h), round(rec[2] * atlas.w), round(rec[3] * atlas.h)
        rects[y0:y1, x0:x1] = True
    inked = atlas.px != zero
    protected = rects | inked
    original_px = atlas.px.copy()

    def dilate(mask):
        m = np.pad(mask, 1)
        return (m[:-2, :-2] | m[:-2, 1:-1] | m[:-2, 2:] | m[1:-1, :-2] | m[1:-1, 1:-1] | m[1:-1, 2:] |
                m[2:, :-2] | m[2:, 1:-1] | m[2:, 2:])
    # Guard: keep 1 px between ink and foreign cells, unless the native layout already packs ink against foreign cells
    # (then the game evidently samples cells point-wise and the guard would only waste space).
    owner = -np.ones((atlas.h, atlas.w), int)
    for i, rec in enumerate(fm.records):
        owner[round(rec[1] * atlas.h):round(rec[3] * atlas.h), round(rec[0] * atlas.w):round(rec[2] * atlas.w)] = i
    touching = 0
    for i, rec in enumerate(fm.records):
        x0, y0, x1, y1 = round(rec[0] * atlas.w), round(rec[1] * atlas.h), round(rec[2] * atlas.w), round(rec[3] * atlas.h)
        ys, xs = slice(max(0, y0 - 1), min(atlas.h, y1 + 1)), slice(max(0, x0 - 1), min(atlas.w, x1 + 1))
        if (inked[ys, xs] & (owner[ys, xs] != i)).any():
            touching += 1
    grow = (lambda m: m) if touching else dilate
    guard_rects, guard_ink = grow(rects), grow(inked)

    # native side bearing: blank columns either side of ink+outline in native ASCII letters
    def body(px):
        cols = np.where((px != zero).any(axis=0))[0]
        return (int(cols[0]), int(cols[-1])) if len(cols) else None
    sides = []
    for c in map(chr, range(0x21, 0x7F)):
        if c.isalpha() and ord(c) in fm.map:
            px = cell_px(fm, atlas, fm.map[ord(c)]); b = body(px)
            if b:
                sides += [b[0], px.shape[1] - 1 - b[1]]
    native_bearing = max(0, round(float(np.median(sides)))) if sides else 1
    # new cells carry no blank bearing: the outline already separates letters (proportional Latin text)
    bearing = 0

    mapping, records = dict(fm.map), list(fm.records)
    report = {'calibration': calib, 'native_bearing': native_bearing, 'skipped': [], 'guard': 0 if touching else 1, 'native_touching': touching, 'native': [], 'cropped': [], 'generated': []}

    def place(bitmap):
        """Bottom-most, left-most position where the cell holds no foreign ink and its ink touches no foreign cell."""
        nonlocal rects, inked, guard_rects, guard_ink
        h, w = bitmap.shape
        own = bitmap != zero
        for y in range(atlas.h - h, -1, -1):
            band_ink, band_rect = guard_ink[y:y + h], guard_rects[y:y + h]
            bad = np.concatenate([[0], np.cumsum(band_ink.any(axis=0))])
            for x0 in np.where(bad[w:] - bad[:-w] == 0)[0]:
                if (band_rect[:, x0:x0 + w] & own).any():
                    continue
                atlas.px[y:y + h, x0:x0 + w] = bitmap
                rects[y:y + h, x0:x0 + w] = True
                inked[y:y + h, x0:x0 + w] |= bitmap != zero
                guard_rects, guard_ink = grow(rects), grow(inked)
                return x0, y
        raise ValueError('No free atlas space for a %dx%d glyph' % (w, h))

    def add_record(x, y, w, adv):
        records.append((x / atlas.w, y / atlas.h, (x + w) / atlas.w, (y + H) / atlas.h, 0, w, adv, 0))
        return len(records) - 1

    digit_width = None
    order = [c for c in range(0x20, 0x7F) if chr(c) not in optional] + [c for c in range(0x20, 0x7F) if chr(c) in optional]
    for code in order:
        ch = chr(code)
        if code in fm.map:
            report['native'].append(ch); continue
        if ch == ' ':
            adv = max(2, round(renderer.font.getlength(' ')))
            x, y = place(np.full((H, 1), zero, np.uint8))
            mapping[code] = add_record(x, y, 1, adv)
            report['generated'].append(' ')
            continue
        fw = cp(fullwidth(ch))
        if fw in fm.map and ch not in FORCE_GENERATE:
            src = fm.records[fm.map[fw]]
            px = cell_px(fm, atlas, fm.map[fw]); b = body(px)
            if b is None:
                mapping[code] = fm.map[fw]; continue
            x0 = round(src[0] * atlas.w)
            left, w = b[0], b[1] - b[0] + 1
            if ch.isdigit():
                if digit_width is None:
                    digit_width = max(body(cell_px(fm, atlas, fm.map[cp(fullwidth(d))]))[1] -
                                      body(cell_px(fm, atlas, fm.map[cp(fullwidth(d))]))[0] + 1
                                      for d in '0123456789' if cp(fullwidth(d)) in fm.map)
                left -= (digit_width - w) // 2
                w = digit_width
            left = max(0, left - bearing)
            w = min(px.shape[1] - left, w + 2 * bearing)
            records.append(((x0 + left) / atlas.w, src[1], (x0 + left + w) / atlas.w, src[3], 0, w, w, 0))
            mapping[code] = len(records) - 1
            report['cropped'].append(ch)
            continue
        if ch in LATIN_FALLBACK:
            c, adv = Renderer(LATIN_FALLBACK[ch], renderer.size, H, renderer.baseline).glyph(ch)
        else:
            c, adv = renderer.glyph(ch)
        bitmap = to_bitmap(c)
        bm = body(bitmap)
        # trim to ink+outline plus the native bearing
        bitmap = bitmap[:, max(0, bm[0] - bearing):bm[1] + 1 + bearing] if bm else bitmap
        try:
            x, y = place(bitmap)
        except ValueError:
            if ch not in optional:
                raise
            report['skipped'].append(ch); continue
        mapping[code] = add_record(x, y, bitmap.shape[1], bitmap.shape[1])
        report['generated'].append(ch)

    new_ccm = fm.build(mapping, records)
    new_tex = atlas.encode()
    # verification against the inputs
    check, check_atlas = FontMap(new_ccm), Atlas(new_tex)
    require(all(check.map[c] == i for c, i in fm.map.items()), 'Original lookup changed')
    require(check.records[:len(fm.records)] == fm.records, 'Original glyph records changed')
    require(all(c in check.map or chr(c) in report['skipped'] for c in range(0x20, 0x7F)), 'ASCII coverage incomplete')
    require((check_atlas.px[protected] == original_px[protected]).all(), 'Original glyph pixels changed')
    require((check_atlas.px == atlas.px).all(), 'Atlas round trip failed')
    require(len(new_tex) == len(tex) and new_tex[32 + atlas.w * atlas.h // 2:] == tex[32 + atlas.w * atlas.h // 2:],
            'Atlas size or palette changed')
    return new_ccm, new_tex, report


# ---------------------------------------------------------------- proof rendering from the final bytes

def proof(ccm, tex, lines, path, scale=2, mark_from=None, color=(255, 255, 255)):
    """Render lines with the font bytes as the game would (palette modulated by a text colour)."""
    fm, atlas = FontMap(ccm), Atlas(tex)
    rgba = np.array([c for c in atlas.palette], dtype=np.float32)
    H = fm.height
    look = lambda c: fm.map.get(cp(c), fm.map.get(0x8148))
    width = max([sum(fm.records[look(c)][6] for c in line) for line in lines] + [1]) + 16
    canvas = np.zeros((len(lines) * (H + 6) + 8, width, 3), np.float32)
    canvas[:] = (40, 70, 110)
    tint = np.array(color, np.float32) / 128.0
    for li, line in enumerate(lines):
        x, y = 8, 4 + li * (H + 6)
        for c in line:
            idx = look(c)
            l, t, r, b, off, w, adv, _ = fm.records[idx]
            x0, y0, x1, y1 = round(l * atlas.w), round(t * atlas.h), round(r * atlas.w), round(b * atlas.h)
            px = atlas.px[y0:y1, x0:x1]
            a = np.clip(rgba[px, 3:4] / 128.0, 0, 1)
            col = np.clip(rgba[px, :3] * tint, 0, 255)
            if mark_from is not None and idx >= mark_from:
                col = col * np.array([1.0, 0.7, 0.55])
            region = canvas[y:y + px.shape[0], x + off:x + off + px.shape[1]]
            region[:] = region * (1 - a[:region.shape[0], :region.shape[1]]) + col[:region.shape[0], :region.shape[1]] * a[:region.shape[0], :region.shape[1]]
            x += adv
    img = Image.fromarray(canvas.clip(0, 255).astype('uint8'))
    img.resize((img.width * scale, img.height * scale), Image.NEAREST).save(path)

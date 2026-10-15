"""Complete the fonts in memory and write proof images under work/proof/ (generated glyphs tinted orange).

  python tools/ace2/font_proof.py
"""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ace2lib import ROOT, BASE, Disc, inner_get
from fonts import complete, proof, FontMap

LINES = ["Mission start! Destroy all enemy units.", "Roger. I'm moving out, Kou. Quick, follow me!",
         "Jump, Quattro: just unique boxes (vexing).", "MEMORY CARD (8MB) slot 1: 90 KB free. 0123456789",
         'Press "X" to cancel; @ # $ & * + = / \\ ^ _ { | } ~ < > ? %', "The Gundam Unit 2 was stolen by Delaz Fleet."]
# (bundle, font map id, atlas id)
FONTS = {'game_2500': (38000, 2500, 2000), 'hud_2501': (38000, 2501, 2001),
         'menu_2500': (62050, 2500, 2000), 'game21_2500': (38002, 2500, 2000)}
# HUD atlas is nearly full: rarely needed symbols may be left out (HUD text avoids them)
RARE = r'#$@[\]^_`{|}~;*='
OPTIONAL = {'hud_2501': RARE, 'game21_2500': RARE}
OUT = ROOT / 'work' / 'proof'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    disc = Disc(BASE)
    for name, (rid, fid, tid) in FONTS.items():
        bundle = disc.get(rid)
        ccm, tex = inner_get(bundle, fid), inner_get(bundle, tid)
        t = time.time()
        new_ccm, new_tex, report = complete(ccm, tex, optional=OPTIONAL.get(name, ''))
        proof(new_ccm, new_tex, LINES, OUT / ('font_%s.png' % name), mark_from=len(FontMap(ccm).records))
        print(name, '%.0fs' % (time.time() - t), json.dumps(
            {k: (''.join(v) if isinstance(v, list) else v) for k, v in report.items()}, ensure_ascii=False))


if __name__ == '__main__':
    main()

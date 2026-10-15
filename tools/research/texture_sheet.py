import sys, glob, os, math
from PIL import Image, ImageDraw
src, out, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
files = sorted(glob.glob(os.path.join(src, prefix + '*.png')))
files = [f for f in files if not os.path.basename(f).endswith('_2000.png')]
T = 200; cols = 6; per = 36
for s in range(0, len(files), per):
    chunk = files[s:s + per]; rows = math.ceil(len(chunk) / cols)
    sheet = Image.new('RGB', (cols * T, rows * (T + 14)), (0, 0, 0)); dr = ImageDraw.Draw(sheet)
    for k, f in enumerate(chunk):
        im = Image.open(f); im.thumbnail((T, T))
        x, y = k % cols * T, k // cols * (T + 14)
        sheet.paste(im, (x, y + 14)); dr.text((x + 2, y), os.path.basename(f)[:-4], fill=(255, 255, 0))
    sheet.save('%s/%s_%02d.png' % (out, prefix.rstrip('_'), s // per))
print(len(files))

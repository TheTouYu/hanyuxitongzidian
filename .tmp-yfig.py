# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

SRC = r"D:\系统汉字\web\public\glyphs"
OUT = r"D:\系统汉字\intake\20261021-释银-字形.png"
f_h = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 28)
f_n = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 21)

def load(ch, h):
    d = os.path.join(SRC, ch)
    out = []
    for f in sorted(os.listdir(d)):
        if not f.endswith(".png"):
            continue
        im = Image.open(os.path.join(d, f)).convert("RGB")
        out.append(im.resize((int(im.width * h / im.height), h), Image.LANCZOS))
    return out

jin = load("金", 200)
gen = load("艮", 220)
GAP = 16
COLS = 8
rows = [jin[i:i + COLS] for i in range(0, len(jin), COLS)]

T1 = "金（形符 · 今部内二级字根）—— 象从土中冶炼出来的金属"
T2 = "艮（声符 · 勹部内二级字根）—— 从目从勹，象眼簾低垂、眼皮薄而凸起成边界"
probe = Image.new("RGB", (10, 10)); dp = ImageDraw.Draw(probe)
w_img = max(sum(i.width for i in r) + GAP * (len(r) - 1) for r in rows)
w_gen = sum(i.width for i in gen) + GAP * (len(gen) - 1)
w_txt = max(dp.textlength(s, font=f_h) for s in (T1, T2))
W = int(max(w_img, w_gen, w_txt)) + 90

y = 26
H = y + 46 + len(rows) * (200 + 8) + 24 + 46 + 220 + 46
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)

d.text((36, y), T1, font=f_h, fill=(25, 25, 25)); y += 46
for r in rows:
    x = 36
    for im in r:
        img.paste(im, (x, y)); x += im.width + GAP
    y += 200 + 8
y += 24
d.text((36, y), T2, font=f_h, fill=(25, 25, 25)); y += 46
x = 36
for im in gen:
    img.paste(im, (x, y)); x += im.width + GAP
y += 220 + 10
d.text((36, y), "银本身无古文字字形：金旁从「銀」起是后起形声，故取形符「金」与声符「艮」的字形代之。",
       font=f_n, fill=(118, 112, 106))
img.save(OUT)
print(OUT, img.size)


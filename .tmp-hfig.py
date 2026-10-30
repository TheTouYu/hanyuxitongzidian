# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

SRC = r"D:\系统汉字\web\public\glyphs"
OUT = r"D:\系统汉字\intake\20261021-释海-字形.png"
f_h = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 28)
f_n = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 21)
EXT = (".png", ".jpg", ".jpeg")

def load(ch, h):
    d = os.path.join(SRC, ch)
    out = []
    for f in sorted(os.listdir(d)):
        if f.lower().endswith(EXT):
            im = Image.open(os.path.join(d, f)).convert("RGB")
            out.append(im.resize((int(im.width * h / im.height), h), Image.LANCZOS))
    return out

shui = load("水", 200)
mei = load("每", 220)
GAP = 16
COLS = 8
rows = [shui[i:i + COLS] for i in range(0, len(shui), COLS)]
T1 = "水（形符 · 第 252 部「水部」部首字）—— 象众水并流"
T2 = "每（声符 · 母部内字根）—— 从花从女（母），梅花初文，取「母」的生育滋生义"
probe = Image.new("RGB", (10, 10)); dp = ImageDraw.Draw(probe)
W = int(max(max(sum(i.width for i in r) + GAP * (len(r) - 1) for r in rows),
            sum(i.width for i in mei) + GAP * (len(mei) - 1),
            dp.textlength(T1, font=f_h), dp.textlength(T2, font=f_h))) + 96
y = 26
H = y + 46 + len(rows) * (200 + 8) + 30 + 46 + 220 + 50
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)
d.text((36, y), T1, font=f_h, fill=(25, 25, 25)); y += 46
for r in rows:
    x = 36
    for im in r:
        img.paste(im, (x, y)); x += im.width + GAP
    y += 200 + 8
y += 26
d.text((36, y), T2, font=f_h, fill=(25, 25, 25)); y += 46
x = 36
for im in mei:
    img.paste(im, (x, y)); x += im.width + GAP
y += 220 + 12
d.text((36, y), "海本身无古文字字形（水旁「海」为后起形声），故取形符「水」与声符「每」的字形代之。",
       font=f_n, fill=(118, 112, 106))
img.save(OUT)
print(OUT, img.size)

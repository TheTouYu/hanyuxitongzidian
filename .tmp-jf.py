# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

SRC = r"D:\系统汉字\web\public\glyphs\見"
OUT = r"D:\系统汉字\intake\20261021-释见-字形.png"
f_h = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 28)
f_n = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 21)

files = sorted(f for f in os.listdir(SRC) if f.endswith(".png"))
ims = [Image.open(os.path.join(SRC, f)).convert("RGB") for f in files]
H = 210
ims = [i.resize((int(i.width * H / i.height), H), Image.LANCZOS) for i in ims]

GAP, COLS, M = 30, 8, 40
rows = [ims[i:i + COLS] for i in range(0, len(ims), COLS)]
roww = max(sum(i.width for i in r) + GAP * (len(r) - 1) for r in rows)
T1 = "見（第 136 部「臣部」内字族，本義从儿从臣（目））—— 象观看、观照"
T2 = "同部另有「覞」（第 303 部）：二見并立，为并视、注视"
W = int(max(roww, f_h.getlength(T1) if hasattr(f_h, "getlength") else 900)) + 2 * M
Hh = 26 + 46 + len(rows) * (H + 8) + 24 + 40 + 46
img = Image.new("RGB", (W, Hh), "white")
d = ImageDraw.Draw(img)
d.text((M, 24), T1, font=f_h, fill=(25, 25, 25))
y = 24 + 46
for r in rows:
    x = M
    for i in r:
        img.paste(i, (x, y))
        x += i.width + GAP
    y += H + 8
d.text((M, y + 12), T2, font=f_n, fill=(110, 104, 98))
d.text((M, y + 44), "「见」为「見」的简化字，本身无古文字字形，故取「見」的字形。", font=f_n, fill=(130, 124, 118))
img.save(OUT)
print(OUT, img.size, len(ims))

# -*- coding: utf-8 -*-
import json, io, os, sys, glob
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from PIL import Image, ImageDraw, ImageFont
C = r"D:\系统汉字\web\public\cards"
G = r"D:\系统汉字\web\public\glyphs\chars"
FONT = r"C:\Windows\Fonts\simsunb.ttf"
need = set()
for fn in glob.glob(os.path.join(C, "*.json")):
    if fn.endswith("index.json"):
        continue
    try:
        d = json.load(io.open(fn, encoding="utf-8"))
    except Exception:
        continue
    s = (d.get("head") or "") + d.get("char", "")
    for a in (d.get("aliases") or []):
        s += a
    for ch in s:
        if ord(ch) >= 0x20000:
            need.add(ch)
missing = [c for c in sorted(need) if not os.path.exists(os.path.join(G, f"{ord(c):x}.png"))]
print("need", len(need), "missing", len(missing))
if missing:
    font = ImageFont.truetype(FONT, 64)
    for ch in missing:
        img = Image.new("RGB", (72, 72), (255, 255, 255))
        dr = ImageDraw.Draw(img)
        dr.text((4, 0), ch, font=font, fill=(0, 0, 0))
        img.save(os.path.join(G, f"{ord(ch):x}.png"))
    print("rendered", len(missing))

# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFilter
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=r"D:\系统汉字\web\public\glyphs\photos\砨\01.jpg"
im=Image.open(src).convert("RGB").crop((25,140,600,410)); w,h=im.size
mask=Image.new("L",(w,h),0); d=ImageDraw.Draw(mask)
poly=[(34,246),(22,172),(58,133),(122,103),(202,75),(300,63),(398,75),(478,103),(538,133),(558,172),(545,246),(300,262)]
d.polygon(poly,fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(1.6))
out=im.convert("RGBA"); out.putalpha(mask)
out.save(r"D:\系统汉字\web\public\glyphs\photos\砨\01.png")
print("ok",out.size)
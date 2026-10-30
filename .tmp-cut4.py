# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFilter
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=r"D:\系统汉字\web\public\glyphs\photos\砨\01.jpg"
im=Image.open(src).convert("RGB").crop((25,140,600,410)); w,h=im.size
mask=Image.new("L",(w,h),0); d=ImageDraw.Draw(mask)
poly=[(36,232),(22,170),(58,132),(122,102),(202,74),(300,62),(398,74),(478,102),(538,132),(558,170),(542,232),(470,246),(380,250),(300,246),(220,250),(130,246)]
d.polygon(poly,fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(1.4))
out=im.convert("RGBA"); out.putalpha(mask)
out.save(r"D:\系统汉字\web\public\glyphs\photos\砨\01.png")
print("ok")
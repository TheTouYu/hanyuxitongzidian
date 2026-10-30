# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFilter
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=r"D:\系统汉字\web\public\glyphs\photos\砨\01.jpg"
im=Image.open(src).convert("RGB").crop((25,140,600,410)); w,h=im.size
mask=Image.new("L",(w,h),0); d=ImageDraw.Draw(mask)
poly=[(40,226),(24,168),(60,130),(124,100),(204,72),(300,60),(396,72),(476,100),(536,130),(556,168),(536,224),(470,232),(380,238),(300,232),(220,238),(130,232)]
d.polygon(poly,fill=255)
mask=mask.filter(ImageFilter.GaussianBlur(1.2))
out=im.convert("RGBA"); out.putalpha(mask)
out.save(r"D:\系统汉字\web\public\glyphs\photos\砨\01.png")
print("ok")
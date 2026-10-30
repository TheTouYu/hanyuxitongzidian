# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
src=r"D:\系统汉字\web\public\glyphs\photos\砨\01.jpg"
im=Image.open(src).convert("RGB").crop((25,140,600,410))
w,h=im.size
mask=Image.new("L",(w,h),0); d=ImageDraw.Draw(mask)
poly=[(30,250),(18,170),(55,130),(120,100),(200,72),(300,60),(400,72),(480,100),(540,130),(560,170),(548,250),(300,265)]
d.polygon(poly,fill=255)
white=Image.new("RGB",(w,h),(255,255,255))
out=Image.composite(im,white,mask)
out.save(r"D:\系统汉字\web\public\glyphs\photos\砨\01.png")
print("ok",out.size)
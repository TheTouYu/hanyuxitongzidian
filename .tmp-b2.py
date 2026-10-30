# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\或\01.png"
im=Image.open(p).convert("RGB"); w,h=im.size
cap="北京故宮的護城河"; strip=46
out=Image.new("RGB",(w,h+strip),"white"); out.paste(im,(0,0))
d=ImageDraw.Draw(out); f=ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",26)
tw=d.textlength(cap,font=f); d.text(((w-tw)/2,h+8),cap,font=f,fill=(90,70,50))
out.save(p); print("ok",out.size)
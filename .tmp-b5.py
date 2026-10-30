# -*- coding: utf-8 -*-
import sys,os
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos\蝦"
cap="蛤蟆"
f=ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",26)
for fn in os.listdir(P):
    p=os.path.join(P,fn); im=Image.open(p).convert("RGB")
    if im.height>im.width*1.6: continue
    w,h=im.size; strip=46
    out=Image.new("RGB",(w,h+strip),"white"); out.paste(im,(0,0))
    d=ImageDraw.Draw(out); tw=d.textlength(cap,font=f); d.text(((w-tw)/2,h+10),cap,font=f,fill=(90,70,50))
    out.save(p); print("burned",fn,out.size)
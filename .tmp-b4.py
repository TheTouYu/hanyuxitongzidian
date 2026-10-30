# -*- coding: utf-8 -*-
import sys,os
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
jobs=[("盉","01.png","西周伯定盉"),("盉","01.jpg","西周伯定盉"),("科","01.png","商代的龍紋斗"),("科","01.jpg","商代的龍紋斗"),("萪","01.png","海蔥"),("萪","01.jpg","海蔥")]
f=ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",24)
for ch,fn,cap in jobs:
    p=os.path.join(P,ch,fn)
    if not os.path.exists(p): continue
    im=Image.open(p).convert("RGB"); w,h=im.size
    if h>w*1.4: continue
    strip=42; out=Image.new("RGB",(w,h+strip),"white"); out.paste(im,(0,0))
    d=ImageDraw.Draw(out); tw=d.textlength(cap,font=f); d.text(((w-tw)/2,h+6),cap,font=f,fill=(90,70,50))
    out.save(p); print("burned",ch,fn)
# -*- coding: utf-8 -*-
import json,io,os,sys
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
p=os.path.join(C,"席.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="shengmu": s["text"]="x「续消」取「续」：席子鋪展開來，連綿不斷（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
cap="河姆渡文化葦席殘片（7000年前）"
dd=os.path.join(P,"席")
for f in os.listdir(dd):
    q=os.path.join(dd,f); im=Image.open(q).convert("RGB"); w,h=im.size; strip=44
    out=Image.new("RGB",(w,h+strip),"white"); out.paste(im,(0,0))
    dr=ImageDraw.Draw(out); ft=ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",24)
    tw=dr.textlength(cap,font=ft); dr.text(((w-tw)/2,h+8),cap,font=ft,fill=(90,70,50))
    out.save(q); print("burned",f,out.size)
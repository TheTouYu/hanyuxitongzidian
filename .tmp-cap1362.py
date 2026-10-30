# -*- coding: utf-8 -*-
import os,sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
emf=[];weird=[]
for root,ds,fs in os.walk(G):
    for f in fs:
        if not f.lower().endswith((".png",".jpg",".jpeg")): continue
        p=os.path.join(root,f)
        with open(p,"rb") as h: b=h.read(8)
        if b[:4] in (b"\x01\x00\x00\x00",) or b[:4]==b"\x20\x45\x4d\x46": emf.append(p)
        elif not (b[:4]==b"\x89PNG" or b[:2]==b"\xff\xd8" or b[:4]==b"GIF8"): weird.append((p,b[:4]))
print("EMF伪装",len(emf),"其他异常",len(weird))
for x in emf[:6]: print("EMF",x)
for x in weird[:6]: print("?",x)
# -*- coding: utf-8 -*-
import json,io,os,sys
from PIL import Image, ImageDraw, ImageFont
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
def blob(k):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: return parts[rid[0]].blob
b=blob(223)
d=os.path.join(P,"碬"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
tmp=os.path.join(d,"_raw.png"); open(tmp,"wb").write(b)
im=Image.open(tmp).convert("RGB"); os.remove(tmp)
# 白边裁剪
import numpy as np
a=np.array(im); mask=(a.min(axis=2)<235)
ys,xs=np.where(mask)
if len(xs): im=im.crop((max(xs.min()-6,0),max(ys.min()-6,0),min(xs.max()+7,im.width),min(ys.max()+7,im.height)))
w,h=im.size; strip=46
cap="▲良渚文化遺址礪石（5000年前）"
out=Image.new("RGB",(w,h+strip),(250,250,245)); out.paste(im,(0,0))
dr=ImageDraw.Draw(out); ft=ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",26)
tw=dr.textlength(cap,font=ft); dr.text(((w-tw)/2,h+10),cap,font=ft,fill=(60,60,90))
out.save(os.path.join(d,"01.png"))
ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=ix["photos"]; m["碬"]=["01.png"]
json.dump({"photos":m},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); cx=json.load(io.open(cp,encoding="utf-8")); c=cx["captions"]
c["碬"]=["良渚文化遺址礪石（5000年前）"]
json.dump({"captions":c},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("ok",out.size)
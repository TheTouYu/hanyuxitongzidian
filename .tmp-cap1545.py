# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
ip=os.path.join(P,"index.json"); cp=os.path.join(P,"captions.json")
j=json.load(io.open(ip,encoding="utf-8")); ph=j["photos"]
ca=json.load(io.open(cp,encoding="utf-8"))["captions"]
def put(ch,rid,cap):
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,ch); os.makedirs(D,exist_ok=True)
    for f in os.listdir(D): os.remove(os.path.join(D,f))
    fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
    ph[ch]=[fn]
    if cap: ca[ch]=[cap]
    else: ca.pop(ch,None)
    fp=os.path.join(C,ch+".json")
    if os.path.exists(fp):
        d=json.load(io.open(fp,encoding="utf-8")); d["photos"]=[fn]
        if cap: d["captions"]=[cap]
        else: d.pop("captions",None)
        json.dump(d,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    return fn,len(b),cap
print("齊",put("齊","rId220",None))
print("蠐",put("蠐","rId224","金龜子的幼蟲"))
json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":ca},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
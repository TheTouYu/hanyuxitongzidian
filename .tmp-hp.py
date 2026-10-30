# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
def grab(k):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: return parts[rid[0]].blob
b=grab(266)
# 红刺楤 -> 棫
src=os.path.join(P,"或","01.jpg"); dst=os.path.join(P,"棫"); os.makedirs(dst,exist_ok=True)
if os.path.exists(src): shutil.move(src, os.path.join(dst,"01.jpg"))
d=os.path.join(P,"或"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
ext="png" if b[:4]==b"\x89PNG" else "jpg"
open(os.path.join(d,"01."+ext),"wb").write(b)
ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=ix.get("photos") or ix
m["或"]=["01."+ext]; m["棫"]=["01.jpg"]
json.dump({"photos":m},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); cx=json.load(io.open(cp,encoding="utf-8")); c=cx.get("captions") or cx
c["或"]=["北京故宮的護城河"]; c["棫"]=["紅刺楤"]
json.dump({"captions":c},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("ok",ext,len(b))
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
P=r"D:\系统汉字\web\public\glyphs\photos"; G=r"D:\系统汉字\web\public\glyphs"
def grab(k):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: return parts[rid[0]].blob
ip=os.path.join(P,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); m=ix["photos"]
cp=os.path.join(P,"captions.json"); cx=json.load(io.open(cp,encoding="utf-8")); c=cx["captions"]
g=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=g["chars"]
for k,cap in ((361,"西周伯定盉"),(369,"商代的龍紋斗"),(376,"海蔥")):
    b=grab(k)
    if not b: print("no img",k); continue
    ext="png" if b[:4]==b"\x89PNG" else "jpg"
    # 归属：盉=盉, 科斗图=科, 海蔥=萪
    tgt={361:"盉",369:"科",376:"萪"}[k]
    d=os.path.join(P,tgt); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    fn="01."+ext; open(os.path.join(d,fn),"wb").write(b)
    m[tgt]=[fn]; c[tgt]=[cap]
    ch.setdefault(tgt,{})["photos"]=[{"file":fn,"caption":cap}]
    print("set",tgt,cap)
json.dump({"photos":m},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":c},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts; ps=doc.paragraphs
def grab(k,ch):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    n=0
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)<800: continue
                ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
                open(os.path.join(d,f"{n+1:02d}{ext}"),"wb").write(b); n+=1
    j=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch_map=j.get("chars") or j
    ch_map[ch]={"doc":"卷三 矢","files":[f"{ch}/{f}" for f in sorted(os.listdir(d))]}
    json.dump({"chars":ch_map},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    return n
print("印",grab(666,"印"))
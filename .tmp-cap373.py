# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
rid=None
for p in ps[602:606]:
    for el in p._p.iter():
        for a,v in el.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    pt=parts[v]
                    if hasattr(pt,'blob') and len(pt.blob)>8000: rid=v;break
                except KeyError: pass
        if rid: break
    if rid: break
print("rid",rid)
if rid:
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    P=r"D:\系统汉字\web\public\glyphs\photos"; d=os.path.join(P,"啇"); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"01"+ext),"wb").write(b)
    ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); k="photos" if "photos" in ix else None
    (ix[k] if k else ix)["啇"]=["01"+ext]
    cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))["captions"]
    cp["啇"]=["辣椒和脫落的蒂"]
    json.dump(ix,io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    json.dump({"captions":cp},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("saved",len(b))
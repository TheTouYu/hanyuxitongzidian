# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
def imgs(p):
    out=[]
    for el in p._p.iter():
        for a,v in el.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    pt=parts[v]
                    if hasattr(pt,'blob') and len(pt.blob)>8000: out.append(v)
                except KeyError: pass
    return out
rl=imgs(ps[725])
print("rid",rl)
if rl:
    b=parts[rl[0]].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    P=r"D:\系统汉字\web\public\glyphs\photos"; d=os.path.join(P,"屐"); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"01"+ext),"wb").write(b)
    ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); k="photos" if "photos" in ix else None
    (ix[k] if k else ix)["屐"]=["01"+ext]
    cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cp["captions"]["屐"]=["目前所發現的中國境內最早漆木屐（三國）"]
    json.dump(ix,io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    json.dump(cp,io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("saved",len(b))
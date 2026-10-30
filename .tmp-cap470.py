# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
P=r"D:\系统汉字\web\public\glyphs\photos"
targets={"汥":"rId479","鳷":"rId481","技":"rId483","䰙":"rId484"}
caps={}
for k in range(670,745):
    t=ps[k].text.strip()
    if t.startswith("▲"): caps[k]=t[1:].strip()
def cap_after(k):
    for j in (k+1,k+2,k+3):
        if j in caps: return caps[j]
    return ""
pos={}
for k in range(670,745):
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if (a.endswith("}embed") or a.endswith("}id")) and v in targets.values():
                pos[v]=k
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8"))
capj=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))
ph=idx.get("photos") or idx; cm=capj.get("captions") or capj
done=[]
for ch,rid in targets.items():
    if rid not in pos: print("miss",ch); continue
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else (".emf" if b[:4]==b"\x01\x00\x00\x00" else ".jpg")
    dst=os.path.join(P,ch); os.makedirs(dst,exist_ok=True)
    fn="01"+ext; open(os.path.join(dst,fn),"wb").write(b)
    ph[ch]=[fn]; c=cap_after(pos[rid])
    if c: cm[ch]=[c]
    done.append((ch,fn,len(b),c))
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
for d in done: print(d)
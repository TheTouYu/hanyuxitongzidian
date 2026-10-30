# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
seq=[]
for el in doc.paragraphs[343]._p.iter():
    t=el.tag.split("}")[-1]
    if t=="t": seq.append(("T",el.text or ""))
    elif t=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: seq.append(("I",rid[0]))
# assign by following label
assign=[]; pending=[]
for k,v in seq:
    if k=="I": pending.append(v)
    else:
        lab=None
        if "𦉜" in v: lab="甔"
        elif "瞻" in v: lab="瞻"
        elif "簷" in v or "檐" in v: lab="檐"
        elif "儋" in v: lab="儋"
        if lab and pending:
            for r in pending: assign.append((lab,r))
            pending=[]
if pending:
    for r in pending: assign.append(("詹",r))
from collections import OrderedDict
groups=OrderedDict()
for lab,r in assign: groups.setdefault(lab,[]).append(r)
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
for lab,rids in groups.items():
    d=os.path.join(G,lab); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    files=[]
    for i,rid in enumerate(rids):
        b=parts[rid].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
        fn="%02d.%s"%(i+1,ext); open(os.path.join(d,fn),"wb").write(b); files.append(lab+"/"+fn)
    e=ch.get(lab) or {"doc":"卷五  雁.docx","variants":[]}
    e["files"]=files; ch[lab]=e
    print(lab,len(files))
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
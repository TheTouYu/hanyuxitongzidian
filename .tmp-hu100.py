# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
buf=[]; n=0
for el in doc.paragraphs[74]._p.iter():
    tag=el.tag.split("}")[-1]
    if tag=="t": buf.append(el.text or "")
    elif tag=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            n+=1; buf.append("{{benyi/%02d.png}}"%n)
t="".join(buf).strip()
t=t.replace("本義：","",1).strip()
p=os.path.join(C,"乎.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="benyi": s["text"]=t; s["gdir"]="inline/乎"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(t[:120],"imgs",n)
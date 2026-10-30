# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
ID=os.path.join(G,"inline","兮","bianzheng"); os.makedirs(ID,exist_ok=True)
for f in os.listdir(ID): os.remove(os.path.join(ID,f))
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
out=[]; n=0
for k in (104,105):
    buf=[]
    for el in doc.paragraphs[k]._p.iter():
        tag=el.tag.split("}")[-1]
        if tag=="t": buf.append(el.text or "")
        elif tag=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; n+=1; fn="%02d.%s"%(n,kd(b))
                open(os.path.join(ID,fn),"wb").write(b); buf.append("{{bianzheng/%s}}"%fn)
    t="".join(buf).strip()
    if t.startswith("辯證："): t=t[3:].lstrip()
    out.append(t)
p=os.path.join(C,"兮.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="bianzheng": s["text"]="\n".join(out); s["gdir"]="inline/兮"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("imgs",n)
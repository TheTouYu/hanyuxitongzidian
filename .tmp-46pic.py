# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
def grab(k):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: return parts[rid[0]].blob
    return None
d=os.path.join(P,"乇"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
caps=[]
for i,k in enumerate((288,302),1):
    b=grab(k)
    if not b: continue
    ext="png" if b[:4]==b"\x89PNG" else "jpg"
    open(os.path.join(d,"%02d.%s"%(i,ext)),"wb").write(b)
    caps.append("三星堆小頂尊銅人（商）" if k==288 else "沙漠的駱駝隊")
x=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=x.setdefault("photos",{})
m["乇"]=[f for f in sorted(os.listdir(d))]
json.dump(x,io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
c=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); c.setdefault("captions",{})["乇"]=caps
json.dump(c,io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
# photos.js
pj=r"D:\系统汉字\web\public\photos.js"; s=io.open(pj,encoding="utf-8").read()
import re
s=re.sub(r'"乇":\s*\[[^\]]*\]\s*,?',"",s)
add='"乇": %s,'%json.dumps(m["乇"],ensure_ascii=False)
i=s.find("{")
s=s[:i+1]+add+s[i+1:]
open(pj,"w",encoding="utf-8",newline="\n").write(s)
print("photos",m["乇"],caps)
# -*- coding: utf-8 -*-
import json,io,os,re,sys
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
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
cur=None; found=[]
for k in range(674,735):
    t=ps[k].text.strip()
    m=pat.match(t)
    if m: cur=m.group(1)
    for r in imgs(ps[k]):
        cap=""
        for j in range(k+1,min(k+3,len(ps))):
            nt=ps[j].text.strip()
            if nt.startswith("▲"): cap=nt[1:].strip(); break
        found.append((cur,r,cap,len(parts[r].blob)))
print(len(found))
for f in found: print(f[0],f[1],f[3],f[2][:20])
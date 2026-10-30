import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx")
ps=[p.text.strip() for p in doc.paragraphs]
for k in range(402,422):
    t=ps[k]
    if t: print(k,t[:130])
for k in (393,394,396,397,398,399,400):
    print("---",k,ps[k][:200])
import re
for k in (390,392):
    n=sum(1 for el in doc.paragraphs[k]._p.iter() if el.tag.split("}")[-1]=="blip")
    print("imgs",k,n)
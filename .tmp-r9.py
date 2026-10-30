import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in d.paragraphs]
idx={}
for k,t in enumerate(ps):
    m=re.match(r"^(9|10)[.．]\s*(\S)部$",t)
    if m: idx[m.group(1)]=k
for no in ("9","10"):
    k=idx[no]; print("=====",ps[k])
    for t in ps[k+1:k+16]:
        if t: print(t[:120])
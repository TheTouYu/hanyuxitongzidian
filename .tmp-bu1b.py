import glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx")
ps=[p.text.strip() for p in d.paragraphs]
i=[k for k,t in enumerate(ps) if t.startswith("1.只")][0]
for k in range(i,i+42):
    if ps[k]: print(k,ps[k][:120])
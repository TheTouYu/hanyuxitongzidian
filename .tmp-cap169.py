import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx")
for i,p in enumerate(d.paragraphs):
    t=p.text.strip()
    if "訖" in t or "讫" in t: print(i,t[:120])
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
i=[k for k,t in enumerate(ps) if t.startswith("2.奚")][0]
for k in range(i,i+58):
    if ps[k]: print(k,ps[k][:130])
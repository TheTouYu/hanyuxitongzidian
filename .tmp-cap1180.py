import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷三  矢.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(314,345):
    if ps[k]: print(k,ps[k][:120])
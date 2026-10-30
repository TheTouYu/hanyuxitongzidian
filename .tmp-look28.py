import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一百  壽.docx"); ps=[p.text.strip() for p in d.paragraphs]
for i in range(246,min(330,len(ps))):
    if ps[i]: print(i,ps[i][:95])
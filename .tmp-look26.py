import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷九十九 且.docx"); ps=[p.text.strip() for p in d.paragraphs]
for i in range(202,260):
    if ps[i]: print(i,ps[i][:105])
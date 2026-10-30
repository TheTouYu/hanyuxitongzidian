from docx import Document
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=Document(r"D:\字谱智能体\卷二  㠯.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(70,120):
    if ps[k]: print(k,ps[k][:70])
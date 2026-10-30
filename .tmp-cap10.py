import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=d.paragraphs
for k in range(338,352):
    t=ps[k].text.strip()
    if t: print(k,t[:110])
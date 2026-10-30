import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=d.paragraphs
for i,p in enumerate(ps):
    t=p.text.strip()
    if "骨尺" in t: print(i,t[:60])
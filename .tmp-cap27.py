import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七十七  蛙.docx").paragraphs]
for k in range(545,561):
    if ps[k]: print(k,ps[k][:190])
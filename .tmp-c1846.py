import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\第八章  子.docx").paragraphs]
for k in range(309,330):
    if ps[k]: print(k,ps[k][:80])
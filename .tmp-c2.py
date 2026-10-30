from docx import Document
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\第二章  谷.docx").paragraphs]
for k in range(0,16):
    if ps[k]: print(k,ps[k][:90])
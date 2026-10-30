import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\系统汉字\..\字谱智能体\卷五  雁.docx").paragraphs] if False else [p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
for k in range(281,311):
    if ps[k]: print("==",k,ps[k])
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
for k in range(516,575):
    if k<len(ps) and ps[k]: print(k,ps[k][:150])
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
for k in range(208,212):
    print(k,"|",ps[k])
print("---rows 250-282---")
for k in range(250,283):
    if ps[k]: print(k,"|",ps[k][:80])
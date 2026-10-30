import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷五  雁.docx").paragraphs]
for k in list(range(204,213))+list(range(226,250)):
    if ps[k]: print(k,ps[k][:150])
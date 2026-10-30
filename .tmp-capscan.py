import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]
for k,t in enumerate(ps):
    if t.startswith("▲"): print(k,t[:70])
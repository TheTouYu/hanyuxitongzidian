import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
for k,t in enumerate(ps):
    if ("㳄" in t) and (k<700):
        print(k,t[:70])
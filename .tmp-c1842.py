import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六十五  鼻.docx").paragraphs]
for k,t in enumerate(ps):
    if t.startswith("389"): print(k,t[:40])
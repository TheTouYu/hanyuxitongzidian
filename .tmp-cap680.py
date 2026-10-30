import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for k in (154,155,156):
    print(k,repr(ps[k][:80]))
for k,p in enumerate(ps):
    if "荎" in p and k<158: print("荎行",k,p[:60])
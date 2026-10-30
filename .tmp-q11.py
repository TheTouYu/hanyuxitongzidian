import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
for k in range(9,120):
    if ps[k] and (ps[k].startswith(("①","②","③","④","⑤","本義","轉義","辯證","音源","字族","㠯部","台","巳","以")) or k<20): print(k,ps[k][:130])
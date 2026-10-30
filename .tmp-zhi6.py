import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
for k in range(124,175):
    if ps[k] and (ps[k].startswith(("①","②","③","④","本義","轉義","音源","字族","辯證")) or "耆" in ps[k] or "稽" in ps[k]):
        print(k,ps[k][:70])
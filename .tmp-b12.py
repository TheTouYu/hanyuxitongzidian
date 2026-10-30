import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷一  雞.docx").paragraphs]
for k,t in enumerate(ps[:118]):
    if t and (t.startswith("1.") or t.startswith("2.") or t.startswith(("①","②","③","④","⑤")) or t.startswith(("本義","轉義","辯證","音源","字族"))):
        print(k,t[:58])
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
for k in range(419,520):
    t=ps[k]
    if not t: continue
    if t.startswith(("①","②","③","④","字族")) or (len(t)>2 and t[0] not in "本轉辯音"):
        print(k,t[:80])
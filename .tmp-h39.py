# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
for k in range(28,96):
    t=ps[k]
    if not t: continue
    if k<45 or t.startswith(("本義","轉義","辯證","音源","字族")) or t[:1] in "①②③④⑤" or "《" in t[:30]:
        print(k,t[:70])
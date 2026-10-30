# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx")
ps=[p.text.strip() for p in d.paragraphs]
for k in range(400,414):
    if ps[k]: print(k,ps[k][:220])
print("---- 搜 本義 附近含祟 ----")
for k,t in enumerate(ps):
    if ("祟" in t and ("本義" in t or "从示从出" in t)) or t.startswith("本義") and k>406 and k<440:
        print(k,t[:220])
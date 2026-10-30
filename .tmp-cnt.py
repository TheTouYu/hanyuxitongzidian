# -*- coding: utf-8 -*-
import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
H="\u3400-\u9fff\U00020000-\U0002A6DF"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
rows=[]
for k in range(200,237):
    t=ps[k]
    m=re.match("^(["+H+"]+)",t)
    if m and ("《" in t): rows.append((k,m.group(1)))
print(len(rows))
print([r[1] for r in rows])
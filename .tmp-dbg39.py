# -*- coding: utf-8 -*-
import sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷六  鶴.docx").paragraphs]
pat=re.compile(r"^([^\sA-Za-z]+?)([A-Za-züǖǘǚǜ、，\s]+)《")
cur=None; n=0
for i in range(47,72):
    t=ps[i]
    if not t: continue
    if re.match(r"^[①②③④⑤]",t): cur=t[0]; print("H",cur); continue
    m=pat.match(t)
    if m: n+=1; print(cur,m.group(1)[:3],m.group(2)[:10])
    else: print("MISS",t[:24])
print("rows",n)
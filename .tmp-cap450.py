# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
rows=[]
for k in range(685,730):
    t=ps[k]
    if not t or t[0] in "①②③" or t.startswith(("字族","音源","本義","轉義","辯證","▲")): continue
    m=pat.match(t)
    if not m: print("skip",k,t[:20]); continue
    rows.append((m.group(1),[(k,t)]))
print("rows",len(rows), [r[0] for r in rows][:6])
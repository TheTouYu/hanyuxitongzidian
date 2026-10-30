# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
rows=[]
for k in range(685,730):
    t=ps[k]
    if not t or t[0] in "①②③" or t.startswith(("字族","音源","本義","轉義","辯證","▲")): continue
    m=pat.match(t)
    if not m: print("SKIP",k,t[:26]); continue
    rows.append((k,m.group(1),m.group(3) or "",m.group(4) if m.lastindex and m.lastindex>=4 else "",t))
print("entries",len(rows))
have={f[:-5] for f in os.listdir(C) if f.endswith(".json")}
miss=[r for r in rows if r[1] not in have]
print("missing",len(miss),[r[1] for r in miss])
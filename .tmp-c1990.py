# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
row=re.compile(r"^([^\s（(（]{1,3})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü、]+)\s*[《“]")
groups=[];cur=None
for k in range(746,792):
    t=ps[k]
    if not t: continue
    if re.match(r"^[①②③④⑤⑥]",t):
        cur={"title":t,"rows":[]}; groups.append(cur); continue
    m=row.match(t)
    if m and cur is not None:
        ch=m.group(1); py_=(m.group(4) or "").split("、")[0]
        cur["rows"].append([ch,py_,"",t])
print([(g["title"],len(g["rows"])) for g in groups])
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
line=ps[675]; body=line.split("：",1)[1]
parts=[x for x in body.split() if x]
heads=[];pars={}
for tok in parts:
    m=re.match(r"^([^\s（(《a-zA-Z]+)(（([^）]*)）)?$",tok)
    if not m: print("odd",tok); continue
    heads.append(m.group(1)); pars[m.group(1)]=m.group(3) or ""
have={f[:-5] for f in os.listdir(C) if f.endswith(".json") and f!="index.json"}
miss=[h for h in heads if h not in have]
print("族行条目",len(heads),"缺卡",len(miss),miss)
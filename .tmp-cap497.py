import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
body=ps[675].split("：",1)[1]
i=0;ents=[]
while i<len(body):
    ch=body[i]
    if ch in "（）": i+=1; continue
    par=""
    if i+1<len(body) and body[i+1]=="（":
        j=body.index("）",i); par=body[i+2:j]; i=j+1
    else: i+=1
    ents.append((ch,par))
have={f[:-5] for f in os.listdir(C) if f.endswith(".json") and f!="index.json"}
miss=[(c,p) for c,p in ents if c not in have]
print("条目",len(ents),"缺卡",len(miss))
print([c for c,_ in miss])
# -*- coding: utf-8 -*-
import os,sys,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
zero=[];small=[]
for root,ds,fs in os.walk(G):
    for f in fs:
        p=os.path.join(root,f); s=os.path.getsize(p)
        if s==0: zero.append(p)
        elif s<200: small.append((p,s))
print("零字节",len(zero),"超小",len(small))
for z in zero[:8]: print(z)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
miss=[]
for ch,v in list(chars.items()):
    for f in (v.get("files") or []):
        name=f.split("/")[-1]
        p=os.path.join(G,ch,name)
        if not os.path.exists(p): miss.append((ch,f))
print("索引有而盘上缺",len(miss))
for m in miss[:8]: print(m)
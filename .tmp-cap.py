# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
px=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); photos=px.get("photos") or px
cx=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); caps=cx.get("captions") or cx
ip=r"D:\系统汉字\web\public\glyphs\index.json"
g=json.load(io.open(ip,encoding="utf-8")); ch=g["chars"]
n=0
for k,pl in photos.items():
    if k not in ch: continue
    cl=caps.get(k) or []
    objs=[]
    for i,f in enumerate(pl):
        cap=cl[i] if i<len(cl) else ""
        objs.append({"file":f,"caption":cap})
    ch[k]["photos"]=objs; n+=1
json.dump({"chars":ch},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("converted",n)
# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
d=json.load(io.open(p,encoding="utf-8")); chars=d.get("chars") or d
n=0
for ch,e in chars.items():
    fs=e.get("files") or []
    nf=[f if "/" in f else ch+"/"+f for f in fs]
    if nf!=fs: e["files"]=nf; n+=1
json.dump({"chars":chars},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("normalized",n)
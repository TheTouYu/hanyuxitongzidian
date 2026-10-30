# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
files=["鴈/%02d.png"%(i+1) for i in range(7)]
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix.get("chars") or ix
e=ch.get("鴈") or {}
e["files"]=files
v=e.get("variants")
if isinstance(v,str): v=[v]
elif not isinstance(v,list): v=[]
if "雁" not in v: v.append("雁")
e["variants"]=v
ch["鴈"]=e
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
p=os.path.join(C,"鴈.json"); d=json.load(io.open(p,encoding="utf-8"))
d["bus"]=[{"num":35,"name":"厂"}]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok",e["files"],e["variants"],d["bus"])
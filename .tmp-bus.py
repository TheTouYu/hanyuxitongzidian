# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    b=d.get("bus")
    if isinstance(b,list):
        d["bus"]=(b[0] if b and isinstance(b[0],dict) else ({"num":int(b[0])} if b and str(b[0]).isdigit() else b))
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("normalized bus",n)
# 橐 字形：索引补登，清 𡇈
files=["橐/%02d.png"%(i+1) for i in range(10)]
gp=os.path.join(G,"index.json"); g=json.load(io.open(gp,encoding="utf-8")); ch=g["chars"]
ch.setdefault("橐",{})["files"]=files
ch.pop("𡇈",None)
json.dump({"chars":ch},io.open(gp,"w",encoding="utf-8"),ensure_ascii=False)
sd=os.path.join(G,"𡇈")
if os.path.isdir(sd): shutil.rmtree(sd)
print("glyph ok")
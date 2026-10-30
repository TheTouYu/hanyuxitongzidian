# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8"))
    if isinstance(d,list): continue
    if d.get("parent")=="靃":
        d["parent"]="霍"; n+=1
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
d=os.path.join(P,"靃")
if os.path.isdir(d): shutil.rmtree(d)
for name,key in (("index.json","photos"),("captions.json","captions")):
    fp=os.path.join(P,name); x=json.load(io.open(fp,encoding="utf-8")); m=x.get(key) or x
    m.pop("靃",None); m.pop("霍",None)
    json.dump({key:m},io.open(fp,"w",encoding="utf-8"),ensure_ascii=False)
print("reparented",n)
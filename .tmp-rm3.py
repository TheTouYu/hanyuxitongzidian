# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
d=os.path.join(P,"𤡓")
if os.path.isdir(d): shutil.rmtree(d); print("rm dir")
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    if "𤡓" in m: m.pop("𤡓"); print("clean",name)
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
g=r"D:\系统汉字\web\public\glyphs\index.json"; ch=json.load(io.open(g,encoding="utf-8"))["chars"]
if "𤡓" in ch: ch["𤡓"].pop("photos",None); print("clean glyphs idx")
json.dump({"chars":ch},io.open(g,"w",encoding="utf-8"),ensure_ascii=False)
print("禾 keeps",ch.get("禾",{}).get("photos"))
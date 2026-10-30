# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
src=os.path.join(P,"𧝔")
print("files",os.listdir(src) if os.path.isdir(src) else None)
if os.path.isdir(src):
    fs=sorted(os.listdir(src))
    if fs: shutil.copy(os.path.join(src,fs[0]), r"D:\系统汉字\.tmp-taogu.jpg")
    shutil.rmtree(src)
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    if "𧝔" in m: m.pop("𧝔"); print("cleaned",name)
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
if "𧝔" in gi.get("photos",{}): gi["photos"].pop("𧝔"); json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False); print("cleaned glyph idx")
print("ok")
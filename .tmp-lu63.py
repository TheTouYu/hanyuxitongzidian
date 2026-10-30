# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
cap="虎自後撲倒獵物"
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    m["虜"]=["01.jpg"] if key=="photos" else [cap]
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.setdefault("photos",{})["虜"]=[{"file":"photos/虜/01.jpg","caption":cap}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("ok")
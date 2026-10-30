# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
d=os.path.join(P,"藘"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
shutil.copy(r"D:\系统汉字\.tmp-p241.jpg", os.path.join(d,"01.jpg"))
cap="茹藘（茜草），莖葉密佈細刺"
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    m["藘"]=["01.jpg"] if key=="photos" else [cap]
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.setdefault("photos",{})["藘"]=[{"file":"photos/藘/01.jpg","caption":cap}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("ok")
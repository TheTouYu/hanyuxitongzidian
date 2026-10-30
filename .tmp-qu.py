# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
f=os.path.join(P,"蘧","01.png"); b=open(f,"rb").read(8); print("magic",b[:4])
name="01.png" if b[:4]==b"\x89PNG" else "01.jpg"
if name=="01.jpg": os.replace(f,os.path.join(P,"蘧","01.jpg"))
for p,key in ((os.path.join(P,"index.json"),"photos"),(os.path.join(P,"captions.json"),"captions")):
    x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    if key=="photos": m["蘧"]=[name]
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["photos"]["蘧"]=[{"file":"photos/蘧/"+name,"caption":"瞿麥"}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("ok",name)
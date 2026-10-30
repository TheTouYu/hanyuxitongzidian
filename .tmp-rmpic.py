# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
d=os.path.join(P,"𩒰")
if os.path.isdir(d): shutil.rmtree(d); print("removed dir")
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
    if "𩒰" in m: m.pop("𩒰"); print("cleaned",name)
    json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
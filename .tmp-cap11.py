# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\野"
f2=os.path.join(p,"02.jpg")
if os.path.exists(f2): os.remove(f2)
idx=r"D:\系统汉字\web\public\glyphs\photos\index.json"
d=json.load(io.open(idx,encoding="utf-8")); ph=d.get("photos") or d
ph["野"]=["01.jpg"]; json.dump({"photos":ph},io.open(idx,"w",encoding="utf-8"),ensure_ascii=False)
cp=r"D:\系统汉字\web\public\glyphs\photos\captions.json"
cap=json.load(io.open(cp,encoding="utf-8")); cap["野"]=["《野合圖》（東漢畫像石）"]
json.dump(cap,io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("野 ->",[f for f in os.listdir(p)])
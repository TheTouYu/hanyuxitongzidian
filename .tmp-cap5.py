# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\captions.json"
cap=json.load(io.open(p,encoding="utf-8"))
cap["士"]=["公牛"]
json.dump(cap,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
p2=r"D:\系统汉字\web\public\glyphs\photos\index.json"
d=json.load(io.open(p2,encoding="utf-8")); ph=d.get("photos") or d
print("士 in index:",ph.get("士"))
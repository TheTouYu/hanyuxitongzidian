# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
g=r"D:\系统汉字\web\public\glyphs"
p=g+r"\index.json"; d=json.load(io.open(p,encoding="utf-8"))
e=d["chars"].get("砨") or {}; e["photos"]=["01.png"]; d["chars"]["砨"]=e
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
pp=g+r"\photos\index.json"; x=json.load(io.open(pp,encoding="utf-8")); m=x.get("photos") or x
m["砨"]=["01.png"]; json.dump({"photos":m},io.open(pp,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")
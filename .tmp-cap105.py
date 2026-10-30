# -*- coding: utf-8 -*-
import json,io,sys,urllib.request
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\祟.json"
d=json.load(io.open(p,encoding="utf-8"))
d["aliases"]=["𣦅","𥘣","𥜱","𥚢","𥘈","𥘐"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
j=json.load(urllib.request.urlopen("http://127.0.0.1:8091/cards/%E7%A5%9F.json",timeout=6))
print("served groups:",[(g["title"],len(g["rows"])) for s in j["sections"] for g in (s.get("groups") or [])])
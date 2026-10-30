# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V=r"D:\系统汉字\web\public\variants.json"
v=json.load(io.open(V,encoding="utf-8"))
if isinstance(v,dict) and "variants" in v: v=v["variants"]
for s,t in (("夺","奪"),("𠔟","奪")):
    v.setdefault(s,[])
    if t not in v[s]: v[s]=[t]
json.dump(v,io.open(V,"w",encoding="utf-8"),ensure_ascii=False)
print("夺 ->",v["夺"])
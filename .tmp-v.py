# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V=r"D:\系统汉字\web\public\variants.json"
v=json.load(io.open(V,encoding="utf-8"))
if isinstance(v,dict) and "variants" in v: v=v["variants"]
v["只"]=["隻"]
json.dump(v,io.open(V,"w",encoding="utf-8"),ensure_ascii=False)
print("variants 只 ->",v["只"])
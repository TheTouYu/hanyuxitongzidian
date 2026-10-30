# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\妿.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="shengmu": s["text"]="ē「零聲母」不系：零聲母，緒論七組未列（照實）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\榷.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="shengmu":
        s["text"]="q「亲缺」取「亲」：連接兩岸的獨木橋（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\滊.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    print(s["key"],"|",(s.get("text") or "")[:90])
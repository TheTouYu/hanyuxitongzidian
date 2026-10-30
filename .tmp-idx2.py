# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print(type(d), len(d))
if isinstance(d,dict): print(list(d)[:5])
else:
    for x in d:
        if isinstance(x,dict) and x.get("c")=="戹": print("F:",x.get("f"))
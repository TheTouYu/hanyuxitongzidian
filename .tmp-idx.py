# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\index.json"
d=json.load(io.open(p,encoding="utf-8"))
rows=d if isinstance(d,list) else d.get("cards")
n=0
for r in rows:
    if "ch" in r: r.pop("ch"); n+=1
json.dump(rows,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("dropped ch:",n,"rows",len(rows))
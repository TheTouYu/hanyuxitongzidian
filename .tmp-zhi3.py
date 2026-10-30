# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\隻.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            g["rows"]=[[r["c"],r["p"],r["l"],r["g"]] if isinstance(r,dict) else r for r in g["rows"]]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(json.dumps(d["sections"][5]["groups"][1]["rows"][0],ensure_ascii=False)[:80])
# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\斤.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s.get("groups",[]):
            rows=g.get("rows",[])
            if rows and isinstance(rows[0],dict):
                g["rows"]=[[r.get("ch",""),r.get("py",""),r.get("lei",""),r.get("dian","")] for r in rows]
                print("converted",len(g["rows"]))
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
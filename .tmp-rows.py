# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"斤.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            g["rows"]=[[r["字"],r["读音"],r["类属"],r["落点"]] if isinstance(r,dict) else r for r in g["rows"]]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([[r[0],r[2]] for g in d["sections"][-2]["groups"] for r in g["rows"]][:4] if False else "ok")
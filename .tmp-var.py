# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards")
for p in (os.path.join(ROOT,"variants.json"), os.path.join(C,"variants.json")):
    if not os.path.exists(p): print("skip",p); continue
    d=json.load(io.open(p,encoding="utf-8"))
    d["虾"]=["蝦"]; d["虾蟆"]=["蝦蟆"] if False else d.get("虾蟆",[])
    if not d["虾蟆"]: d.pop("虾蟆")
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("updated",p, d.get("虾"))
p=os.path.join(C,"蝦.json"); c=json.load(io.open(p,encoding="utf-8"))
al=set(c.get("aliases") or []); al.add("虾"); c["aliases"]=sorted(al)
json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases",c["aliases"])
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"𪗟.json"); d=json.load(io.open(p,encoding="utf-8"))
print("head",d.get("head"),"al",d.get("aliases"))
al=set(d.get("aliases") or []); al.update(["齕","龁"]); d["aliases"]=sorted(al)
d["head"]=d.get("head") or "𪗟（齕）"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for ch in ("𥾨","氣","𧥷"):
    q=os.path.join(C,ch+".json"); e=json.load(io.open(q,encoding="utf-8"))
    a=set(e.get("aliases") or [])
    if ch=="𥾨": a.update(["紇","纥"])
    if ch=="氣": a.update(["气","餼","饩"])
    e["aliases"]=sorted(a); json.dump(e,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
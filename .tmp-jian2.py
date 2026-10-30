# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={"议":"議","仪":"儀","蚁":"蟻","牺":"犧","舣":"艤","义":"義"}
for simp,trad in M.items():
    p=os.path.join(C,trad+".json")
    if not os.path.exists(p): print("missing",trad); continue
    d=json.load(io.open(p,encoding="utf-8")); a=d.get("aliases") or []
    if simp not in a: a.append(simp)
    d["aliases"]=a; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for vp in (os.path.join(C,"variants.json"), r"D:\系统汉字\web\public\variants.json"):
    v={}
    if os.path.exists(vp):
        try: v=json.load(io.open(vp,encoding="utf-8"))
        except Exception: v={}
    for simp,trad in M.items():
        arr=v.get(simp) or []
        if trad not in arr: arr.append(trad)
        v[simp]=arr
    json.dump(v,io.open(vp,"w",encoding="utf-8"),ensure_ascii=False)
print("aliases ok")
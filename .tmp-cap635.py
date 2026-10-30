# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0; cards=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=False
    for s in d.get("sections",[]):
        if isinstance(s,dict) and isinstance(s.get("groups"),list):
            g0=len(s["groups"])
            s["groups"]=[g for g in s["groups"] if (g.get("rows") or [])]
            if len(s["groups"])!=g0: n+=g0-len(s["groups"]); ch=True
    if ch:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); cards+=1
print("删空组",n,"涉及卡",cards)
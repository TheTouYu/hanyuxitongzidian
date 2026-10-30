# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PRE=["本義：","轉義：","辯證：","音源：","釋義："]
ORDER=["shiyi","benyi","zhuanyi","bianzheng","yinyuan","shengmu","zizu","suoshujuan"]
n=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); chg=False
    for s in d.get("sections",[]):
        t=(s.get("text") or "").lstrip()
        for pre in PRE:
            if t.startswith(pre): s["text"]=t[len(pre):].lstrip(); chg=True; break
    secs=d.get("sections") or []
    if d.get("level")==3 and secs and secs[0].get("key")!="shiyi":
        secs.sort(key=lambda s: ORDER.index(s.get("key")) if s.get("key") in ORDER else 99); chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("fixed",n)
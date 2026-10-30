# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
FIX={"齭":"ch「刺持」取「刺」：齒被酸味所刺而傷（推）。",
     "乺":"s「失收」取「收」：刷聚塗料，收而復塗（推）。",
     "㫹":"sh「失收」取「收」：光收於物而後明（推）。"}
for ch,t in FIX.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
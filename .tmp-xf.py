# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
FIX={
 "掀":"x「续消」不系：聲符「欣」只標音，掀（舉也）不取欣義（照實）。",
 "𦜓":"x「续消」取「续」：新肉續生而微微凸起（推）。",
 "焮":"x「续消」取「消」：火氣熏灼，物隨而消（推）。",
 "惞":"x「续消」取「续」：喜意接續不絕（推）。",
 "俽":"x「续消」取「续」：欣喜相續（推）。"}
for ch,t in FIX.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=t
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=rf"{C}\𢑓.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        g=s["groups"][0]; rows=g["rows"]; g["rows"]=[r for r in rows if r[0] not in ("架","枷")]
        for i,r in enumerate(g["rows"]):
            if r[0]=="榢":
                g["rows"][i]=["榢（架枷）","jià","木","木名；一說即「架」之異體，《集韻》「架，或作榢」；家聲，取架屋義"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
q=rf"{C}\榢.json"
if os.path.exists(q):
    x=json.load(io.open(q,encoding="utf-8")); x["head"]="榢（架枷）"; x["aliases"]=["架","枷"]
    json.dump(x,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for f in ("架","枷"):
    fp=rf"{C}\{f}.json"
    if os.path.exists(fp):
        y=json.load(io.open(fp,encoding="utf-8")); y["hidden"]=True; y["trad"]="榢"
        y["aliases"]=["榢"]
        json.dump(y,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("merged 架枷 into 榢")
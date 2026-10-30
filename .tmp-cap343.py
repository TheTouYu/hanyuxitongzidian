# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cards={}
for f in glob.glob(C+r"\*.json"):
    b=os.path.basename(f)
    if b in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8")); cards[d.get("char")]=(f,d)
bus={c:d["bus"] for c,(f,d) in cards.items() if d.get("bus")}
n=0; miss=0
for c,(f,d) in cards.items():
    if d.get("bus"): continue
    p=d.get("parent") or ""; seen=set(); cur=p; got=None
    while cur and cur not in seen:
        seen.add(cur)
        if cur in bus: got=bus[cur][0]; break
        nxt=cards.get(cur)
        cur=(nxt[1].get("parent") if nxt else "")
    if got:
        d["bus"]=[{"num":got.get("num"),"name":got.get("name")}]
        json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    else: miss+=1
print("补 bus",n,"仍缺",miss)
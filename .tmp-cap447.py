# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(C+r"\variants.json",encoding="utf-8")); inv={}
for s,ts in V.items():
    for t in ts: inv.setdefault(t,[]).append(s)
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    fp=os.path.join(C,fn); d=json.load(io.open(fp,encoding="utf-8"))
    bus=d.get("bus")
    num=None
    if isinstance(bus,list) and bus and isinstance(bus[0],dict): num=bus[0].get("num")
    elif isinstance(bus,dict): num=bus.get("num")
    if num!=13: continue
    ch=d.get("char") or fn[:-5]
    al=set(d.get("aliases") or [])
    m=re.search(r"（(.+?)）",d.get("head") or "")
    if m: al.update(list(m.group(1)))
    if ch in inv: al.update(inv[ch]); d["simp"]=inv[ch][0]
    d["aliases"]=sorted(a for a in al if a and a!=ch)
    json.dump(d,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("更新",n)
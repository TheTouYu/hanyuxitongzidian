# -*- coding: utf-8 -*-
import json,io,os,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def num(bus):
    if isinstance(bus,dict): return bus.get("num")
    if isinstance(bus,list) and bus and isinstance(bus[0],dict): return bus[0].get("num")
    return None
n=0
for p in glob.glob(os.path.join(C,"*.json")):
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    if num(d.get("bus"))==48:
        for s in d.get("sections",[]):
            if s.get("key")=="suoshujuan":
                s.pop("text",None); s["links"]=[{"ch":"卷八虎","label":"卷八 虎"}]; n+=1
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("updated",n)
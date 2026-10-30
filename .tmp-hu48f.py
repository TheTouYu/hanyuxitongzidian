# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
def num(b):
    if isinstance(b,dict): return b.get("num")
    if isinstance(b,list) and b: return b[0].get("num")
for p in glob.glob(os.path.join(C,"*.json")):
    d=json.load(io.open(p,encoding="utf-8"))
    if not isinstance(d,dict): continue
    if num(d.get("bus"))==48 and not d.get("char"):
        d["char"]=d.get("id") or os.path.basename(p)[:-5]
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("char added",n)
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cards={}
for fn in os.listdir(C):
    if fn.endswith(".json") and fn!="index.json":
        try: d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
        except: continue
        if isinstance(d,dict): cards[d.get("char") or fn[:-5]]=d
par={ch:(d.get("parent") or "") for ch,d in cards.items()}
haskid={p for c,p in par.items() if p and p in cards and c!=p}
n=0; made=[]
for ch in haskid:
    d=cards[ch]
    if d.get("level")==1: continue
    if d.get("parent") and cards.get(d["parent"],{}).get("level")==1: want=2
    else: want=3
    if d.get("rootLevel")!=want:
        d["rootLevel"]=want; n+=1; made.append((ch,want))
        json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("新增字根标记",n,made[:12])
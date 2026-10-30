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
roots={ch for ch,d in cards.items() if d.get("level",0)>1 and any(s.get("key")=="zizu" for s in d.get("sections",[]))}
for ch,d in cards.items():
    for s in d.get("sections",[]):
        for l in (s.get("links") or []):
            if l.get("ch") and cards.get(l["ch"],{}).get("level",0)>1: roots.add(l["ch"])
n=0
for ch,d in cards.items():
    chg=False
    if d.get("level")==1:
        if d.get("rootLevel")!=1: d["rootLevel"]=1; chg=True
    elif ch in roots:
        par=cards.get(d.get("parent") or "",{})
        want=2 if par.get("level")==1 else 3
        if d.get("rootLevel")!=want: d["rootLevel"]=want; chg=True
    elif "rootLevel" in d:
        d.pop("rootLevel"); chg=True
    if chg:
        json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修正",n,"字根",len(roots))
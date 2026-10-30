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
kids={}
for ch,d in cards.items():
    p=d.get("parent") or ""
    if p and p in cards: kids.setdefault(p,[]).append(ch)
n=0; dropped=[]
for ch,ks in kids.items():
    d=cards[ch]
    if d.get("level")==1: continue
    if len(ks)>=3:
        want=2 if cards.get(d.get("parent") or "",{}).get("level")==1 else 3
        if d.get("rootLevel")!=want:
            d["rootLevel"]=want; n+=1
            json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    else:
        if d.get("rootLevel") and d.get("level")!=1:
            d.pop("rootLevel"); n+=1; dropped.append((ch,len(ks)))
            json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("调整",n,"降级",dropped)
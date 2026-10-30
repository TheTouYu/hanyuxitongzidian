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
links=set()
for ch,d in cards.items():
    p=d.get("parent") or ""
    if p and p in cards: kids.setdefault(p,[]).append(ch)
    for s in d.get("sections",[]):
        for l in (s.get("links") or []):
            if l.get("ch"): links.add(l["ch"])
n=0; log=[]
for ch,d in cards.items():
    lv=d.get("level",0)
    if lv==1:
        if d.get("rootLevel")!=1: d["rootLevel"]=1; n+=1
    elif lv==2:
        if d.get("rootLevel")!=2: d["rootLevel"]=2; n+=1; log.append((ch,2,"二级(原文)"))
    elif lv==3:
        cnt=len(kids.get(ch,[]))
        ok = ch in links or cnt>=3
        if ok:
            want=3
            if d.get("rootLevel")!=want: d["rootLevel"]=want; n+=1; log.append((ch,3,f"衍生{cnt}"))
        elif "rootLevel" in d:
            d.pop("rootLevel"); n+=1
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("改",n,log[:10])
print("二级",[c for c,d in cards.items() if d.get("level")==2])
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
links=set()
for ch,d in cards.items():
    for s in d.get("sections",[]):
        for l in (s.get("links") or []):
            if l.get("ch"): links.add(l["ch"])
keep={"㕞"}
n=0; removed=[]
for ch,d in cards.items():
    if d.get("level") in (2,1):
        # 原文所列二级/一级保持
        want=1 if d.get("level")==1 else 2
        if d.get("rootLevel")!=want: d["rootLevel"]=want; n+=1
    elif d.get("level")==3:
        if (ch in links) or (ch in keep):
            if d.get("rootLevel")!=3: d["rootLevel"]=3; n+=1
        elif "rootLevel" in d:
            d.pop("rootLevel"); n+=1; removed.append(ch)
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("改",n,"回落",removed[:10],"共",len(removed))
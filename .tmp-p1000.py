# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PRE={"benyi":["本義","本义"],"zhuanyi":["轉義","转义"],"bianzheng":["辯證","辩证"],
     "yinyuan":["音源"],"shengmu":["聲母擬態","声母拟态"],"shiyi":["釋義","释义"],"zizu":["字族衍義","字族衍义"]}
n=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); chg=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        if not t: continue
        for pre in PRE.get(s.get("key",""),[])+[s.get("label","")]:
            for mark in (pre+"：",pre+":"):
                if t.lstrip().startswith(mark):
                    t=re.sub(r"^\s*"+re.escape(mark)+r"\s*","",t,count=1); chg=True; break
        t2=t.replace("\n"+mark+"\n","\n") if False else t
        if chg: s["text"]=t
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards fixed",n)
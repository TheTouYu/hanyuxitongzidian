# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
LAT=re.compile(r"[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+$")
bad=[]
for fn in list(os.listdir(C)):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); chg=0
    for s in d.get("sections",[]):
        for g in s.get("groups",[]) or []:
            for r in g.get("rows",[]) or []:
                if r and isinstance(r[0],str) and LAT.search(r[0]):
                    r[0]=LAT.sub("",r[0]); chg+=1
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); bad.append((fn,chg))
print("fixed",bad)
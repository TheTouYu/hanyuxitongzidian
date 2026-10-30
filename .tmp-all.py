# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
ANN={"奪":"夺","䨥":"𩆀","愯":"𢥠悚聳","㸕":"攫","㨦":"㩳","䉟":"篧","篗":"𧤽籆籰𧤯䈅","𩹹":"鱯𩽕"}
n=0
for ch,ann in ANN.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    d["aliases"]=sorted(set([c for c in ann if c.strip() and c!=ch]))
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("aliases 全收",n)
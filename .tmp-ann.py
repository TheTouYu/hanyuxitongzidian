# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
ANN={"奪":"夺","𠔟":"","䨥":"𩆀","愯":"𢥠悚聳","𢊄":"","㸕":"攫","㨦":"㩳","䉟":"篧","篗":"𧤽籆籰𧤯䈅","𩹹":"鱯𩽕","𥻬":""}
def has(ch): return os.path.exists(os.path.join(C,ch+".json"))
n=0
for ch,ann in ANN.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    d["head"]=ch+("（"+ann+"）" if ann else "")
    al=[c for c in ann if c.strip() and not has(c) and c!=ch]
    d["aliases"]=sorted(set(al))
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    print(ch,"head=",d["head"],"aliases=",d["aliases"])
# 部头族表行也补括注
p=os.path.join(C,"隻.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            for r in g["rows"]:
                ch=r[0].split("（")[0].strip()
                if ch in ANN and ANN[ch]: r[0]=ch+"（"+ANN[ch]+"）"
                elif ch in ANN: r[0]=ch
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows updated",n)
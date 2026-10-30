# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"洓.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="shengmu":
        s["text"]="z「凿总」取「总」：水積而總聚，浸泡成漬（推）。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
bad=0; ex=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("key")!="shengmu": continue
        t=s.get("text","")
        if re.match(r"^[a-zA-Z]+\s*取「",t.strip()) and "」取「" not in t:
            bad+=1; ex.append((d.get("char"),t[:36]))
print("格式缺组名",bad)
for x in ex[:6]: print(x[0],x[1])
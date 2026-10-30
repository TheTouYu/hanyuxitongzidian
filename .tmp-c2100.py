# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"睪.json"),encoding="utf-8"))
FACE={0:("凿总","总","淘洗沉浮而總聚（推）"),1:("凿总","总","抽繹如絲之總（推）"),2:("凿总","总","釋放而總收（推）"),3:("凿总","总","訛字不取義（推）")}
Z="y「零聲母」不系：零聲母，緒論七組未列（照實）。"
gi=0; n=0
for g in d["sections"]:
    if g["key"]!="zizu": continue
    for grp in g["groups"]:
        for r in grp["rows"]:
            ch,py_=r[0],r[1]; p=os.path.join(C,ch+".json")
            if not os.path.exists(p): continue
            x=json.load(io.open(p,encoding="utf-8"))
            ini=re.sub(r"[^a-z]","",py_.lower())[:1] or "y"
            if ini in ("y","w",""): txt=Z
            else:
                grp_,face,why=FACE[gi]
                txt=f"{ini}「{grp_}」取「{face}」：{why}"
            for s in x["sections"]:
                if s["key"]=="shengmu": s["text"]=txt
            json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
        gi+=1
print("改",n)
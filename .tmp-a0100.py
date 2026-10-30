# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
FIX={"弔":["吊","𢎣","𢎨","𢎱"],"鈟":["釣","魡"],"䘟":["𧘨"],"𨑩":[]}
for ch,al in FIX.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    d["aliases"]=al
    h=d.get("head") or ch
    if ch=="弔": d["head"]="弔（吊𢎣𢎨𢎱）"
    if ch=="鈟": d["head"]="鈟（釣魡）"
    if ch=="䘟": d["head"]="䘟（𧘨）"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
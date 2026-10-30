# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; V=r"D:\系统汉字\web\public\variants.json"
v=json.load(io.open(V,encoding="utf-8")); v["薹"]="苔"; v["擡"]="抬"
json.dump(v,io.open(V,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
def upd(ch,simp):
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    d["simp"]=simp; al=set(d.get("aliases") or []); al.add(simp); al.discard(ch)
    d["aliases"]=sorted(al); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(ch,"simp",simp,"al",d["aliases"])
upd("薹","苔"); upd("擡","抬")
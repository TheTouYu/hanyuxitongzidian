# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
add={"檯":["台"],"擡":["抬"],"籉":[],"薹":[]}
for ch,al in add.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    cur=set(d.get("aliases") or []); cur.update(al); cur.discard(ch)
    d["aliases"]=sorted(cur)
    if al and len(al)==1: d["simp"]=al[0]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(ch,d["aliases"],d.get("simp"))
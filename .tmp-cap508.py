# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pref=("本義：","轉義：","辯證：","音源：","本义：","转义：","辩证：","音源：")
n1=n2=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=False
    for s in d.get("sections") or []:
        t=s.get("text") or ""
        for q in pref:
            if t.startswith(q): s["text"]=t[len(q):].lstrip(); ch=True; break
        for g in s.get("groups") or []:
            seen=set(); newrows=[]
            for r in g.get("rows") or []:
                if not r: continue
                r0=re.sub(r"（[^）]*）","",str(r[0])).strip()
                if not r0 or r0 in seen: continue
                seen.add(r0); r[0]=r0; newrows.append(r)
            if len(newrows)!=len(g.get("rows") or []): g["rows"]=newrows; ch=True
    if ch:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n1+=1
print("清理",n1)
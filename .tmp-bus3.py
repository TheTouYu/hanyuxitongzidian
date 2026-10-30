# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z.get("byName") or {}
num2name={v["no"]:k for k,v in by.items()}
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f not in ("index.json","variants.json"):
        try: cards[f[:-5]]=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
        except Exception: pass
def base(s): return re.split(r"[（(]",s or "")[0].strip()
def busnum(d):
    b=d.get("bus")
    if isinstance(b,list) and b and isinstance(b[0],dict): return b[0].get("num")
    if isinstance(b,dict): return b.get("num")
    return None
member={}
for pn,pd in cards.items():
    for s in pd.get("sections",[]):
        for g in (s.get("groups") or []):
            for r in (g.get("rows") or []):
                if r: member[base(r[0])]=pn
fixed=0; fail=0
for ch,d in cards.items():
    if d.get("level")!=3 or busnum(d): continue
    pn=member.get(ch) or d.get("parent") or ""
    n=None
    for c in (pn, base(pn)):
        if c in by: n=by[c]["no"]; break
        p=cards.get(c)
        if p and busnum(p): n=busnum(p); break
    if not n: fail+=1; continue
    d["bus"]=[{"num":n,"name":num2name.get(n,"")}]
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    fixed+=1
print("fixed",fixed,"fail",fail)
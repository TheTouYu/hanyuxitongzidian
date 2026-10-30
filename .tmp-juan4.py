# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
num2={}
for ch,v in (z.get("byName") or {}).items():
    n=v.get("no")
    if n and n not in num2: num2[n]=(v.get("juanNo"),v.get("juanName"))
def cn(n):
    d={1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十"}
    return d[n] if n<=10 else ("十"+d[n-10] if n<20 else (d[n//10]+"十" if n%10==0 else d[n//10]+"十"+d[n%10]))
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
added=0; fail=0
for ch,d in cards.items():
    if d.get("level")!=3: continue
    if any(s.get("key")=="suoshujuan" for s in d.get("sections",[])): continue
    p=cards.get(d.get("parent")) or cards.get(base(d.get("parent")))
    link=None
    if p:
        s0=[s for s in p.get("sections",[]) if s.get("key")=="suoshujuan"]
        if s0 and s0[0].get("links"): link=s0[0]["links"]
    if not link and p:
        n=busnum(p)
        if n and n in num2:
            jn,jname=num2[n]; link=[{"ch":"卷"+cn(jn)+jname,"label":"卷"+cn(jn)+" "+jname}]
    if not link:
        fail+=1; continue
    d["sections"].append({"key":"suoshujuan","label":"所属卷","links":link})
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    added+=1
print("added",added,"fail",fail)
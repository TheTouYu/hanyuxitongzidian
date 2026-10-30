# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
num2={}
for ch,v in (z.get("byName") or {}).items():
    n=v.get("no")
    if n and n not in num2: num2[n]=(v.get("juanNo"),v.get("juanName"))
def cn(n):
    d={1:"一",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十"}
    if n<=10: return d[n]
    if n<20: return "十"+d[n-10]
    if n%10==0: return d[n//10]+"十"
    return d[n//10]+"十"+d[n%10]
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f not in ("index.json","variants.json"):
        try: cards[f[:-5]]=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
        except Exception: pass
added=0; fail=[]
for ch,d in cards.items():
    if d.get("level")!=3: continue
    if any(s.get("key")=="suoshujuan" or s.get("label") in ("所属卷","所屬卷") for s in d.get("sections",[])): continue
    p=cards.get(d.get("parent"))
    n=(p.get("bus") or [{}])[0].get("num") if p else None
    if not n or n not in num2: fail.append(ch); continue
    jn,jname=num2[n]
    link={"ch":"卷"+cn(jn)+jname,"label":"卷"+cn(jn)+" "+jname}
    d.setdefault("sections",[]).append({"key":"suoshujuan","label":"所属卷","links":[link]})
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    added+=1
print("added",added,"fail",len(fail))
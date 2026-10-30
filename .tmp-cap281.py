# -*- coding: utf-8 -*-
import os,json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
BY=Z.get("byName",{}); JUAN={j.get("no"):j for j in Z.get("juan",[])}
def busname(d):
    b=d.get("bus")
    if isinstance(b,list) and b:
        x=b[0]; return (x.get("name") if isinstance(x,dict) else str(x)) or ""
    if isinstance(b,str): return b
    return ""
n=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    nm=busname(d)
    if not nm: continue
    e=BY.get(nm)
    if not e: continue
    jn=e.get("juanNo"); jname=e.get("juanName") or ""
    if not jn: continue
    cname=f"卷{jn}{jname}"; label=cname
    changed=False
    for s in d.get("sections",[]):
        if s.get("key") in ("suoshujuan","suoshu"):
            if not s.get("links"):
                s["links"]=[{"ch":cname,"label":label}]; s["key"]="suoshujuan"; s["label"]="所属卷"; changed=True
    if changed:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补所属卷链接",n)
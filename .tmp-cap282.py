# -*- coding: utf-8 -*-
import os,json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
BY=Z.get("byName",{})
D="零一二三四五六七八九"
def cn(n):
    n=int(n)
    if n<=10: return D[n] if n<10 else "十"
    if n<20: return "十"+D[n%10]
    if n<100:
        return D[n//10]+"十"+(D[n%10] if n%10 else "")
    return str(n)
def busname(d):
    b=d.get("bus")
    if isinstance(b,list) and b:
        x=b[0]; return (x.get("name") if isinstance(x,dict) else str(x)) or ""
    if isinstance(b,str): return b
    return ""
n=fix=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    nm=busname(d); e=BY.get(nm)
    chg=False
    if e and e.get("juanNo"):
        cname=f"卷{cn(e['juanNo'])}{e.get('juanName') or ''}"
        for s in d.get("sections",[]):
            if s.get("key") in ("suoshujuan","suoshu"):
                if not s.get("links") or s["links"][0].get("ch")!=cname:
                    s["links"]=[{"ch":cname,"label":cname}]; s["key"]="suoshujuan"; s["label"]="所属卷"; chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修正所属卷链接",n)
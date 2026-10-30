# -*- coding: utf-8 -*-
import json,sys,glob,os,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; kids={}
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    try: d=json.load(open(f,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    p=d.get("parent") or ""
    if p: kids.setdefault(p,[]).append(d)
def rows_for(par):
    out=[]
    for d in sorted(kids.get(par,[]),key=lambda x:x["char"]):
        if d.get("level")!=3: continue
        if (d.get("trad") or d["char"])!=d["char"]: continue
        sh=next((s["text"] for s in d["sections"] if s["key"] in ("shiyi","benyi")),"")
        m=re.match(r"从(.+?)"+par+r"聲：(.+)$",sh)
        lei,luo=(m.group(1),m.group(2)) if m else ("?",sh)
        out.append([d["char"],d.get("pinyin",""),lei,luo])
    return out
rows=rows_for("㤅")
for par,title in (("㤅","①均以「㤅（愛）」為聲旁"),("疑","①均以「疑」為聲旁"),("贛","①均以「贛」為聲旁")):
    fp=rf"{C}\{par}.json"; d=json.load(open(fp,encoding="utf-8")); rs=rows if par=="㤅" else rows_for(par)
    for s in d["sections"]:
        if s["key"]=="zizu":
            s["text"]=""; s["groups"]=[{"title":title,"note":"","rows":rs}] if rs else []
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
fa=rf"{C}\愛.json"
if os.path.exists(fa):
    d=json.load(open(fa,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="zizu":
            s["text"]=""; s["groups"]=[{"title":"①均以「愛」為聲旁（同㤅）","note":"","rows":rows}] if rows else []
    json.dump(d,open(fa,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("㤅",len(rows),"疑",len(rows_for("疑")),"贛",len(rows_for("贛")))
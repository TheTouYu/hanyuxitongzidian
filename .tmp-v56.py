# -*- coding: utf-8 -*-
import io,json,os,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    sec={s.get("key"):s for s in d.get("sections",[])}
    daoyu=sec.get("js_导语") or {"key":"daoyu","label":"导语","text":"","cites":[]}
    daoyu["key"]="daoyu"; daoyu["label"]="导语"
    if not daoyu.get("text"): daoyu["text"]="本卷总说见原稿卷首。"
    out=[]
    for k,lab in (("js_音源","音源"),("js_说物","说物"),("js_文化","文化")):
        s=sec.get(k) or {"key":k,"label":lab,"text":"","cites":[]}
        s["key"]=k; s["label"]=lab
        if s.get("text") or s.get("groups"): out.append(s)
    yx=sec.get("js_音系") or {"key":"js_音系","label":"音系","text":"","cites":[]}
    yx["key"]="js_音系"; yx["label"]="音系"
    grp=None
    for k,s in sec.items():
        if s.get("groups") and any("部目" in (g.get("title") or "") for g in s["groups"]): grp=s["groups"]
    if grp: yx["groups"]=grp
    if not yx.get("text"): yx["text"]="音系即本卷所属诸部（下表）。"
    out.append(yx)
    for k,s in sec.items():
        if k not in ("js_导语","js_音源","js_说物","js_文化","js_音系") and k not in [x["key"] for x in out]:
            out.append(s)
    d["sections"]=[daoyu]+out
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("卷卡重排",n)
d=json.load(io.open(C+r"\卷八虎.json",encoding="utf-8"))
print([ (s["key"],s["label"],bool(s.get("groups"))) for s in d["sections"]])
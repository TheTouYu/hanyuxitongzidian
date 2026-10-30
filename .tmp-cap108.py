# -*- coding: utf-8 -*-
import json,io,glob,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
have={os.path.basename(f)[:-5] for f in glob.glob(C+r"\*.json")}
idx=json.load(io.open(C+r"\index.json",encoding="utf-8"))
alias=set(a for x in idx for a in (x.get("a") or []))
made=[]
for fp in glob.glob(C+r"\*.json"):
    if fp.endswith("index.json"): continue
    d=json.load(io.open(fp,encoding="utf-8"))
    for s in d.get("sections",[]):
        for g in (s.get("groups") or []):
            for r in g.get("rows") or []:
                raw=str(r[0] or "").strip()
                if not raw or re.match(r"^\d+\.",raw) or raw.startswith("卷"): continue
                m=re.match(r"^([^（(]+)[（(]([^）)]*)[）)]$",raw); ch=m.group(1) if m else raw
                if ch in have or ch in alias: continue
                al=[c for c in (m.group(2) if m else "") if c.strip()]
                nd={"char":ch,"pinyin":r[1] if len(r)>1 else "","level":3,"parent":d.get("char",""),
                    "bus":d.get("bus") or [],"sections":[{"key":"shiyi","label":"释义","text":r[3] if len(r)>3 else "","cites":[]}]}
                if al: nd["head"]=raw; nd["aliases"]=al
                json.dump(nd,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
                have.add(ch); made.append(ch)
print("补卡",len(made))
print(made)
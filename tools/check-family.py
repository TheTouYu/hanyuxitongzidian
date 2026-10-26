# -*- coding: utf-8 -*-
import json,io,glob,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
have={os.path.basename(f)[:-5] for f in glob.glob(C+r"\*.json")}
idx=json.load(io.open(C+r"\index.json",encoding="utf-8"))
alias=set(a for x in idx for a in (x.get("a") or []))
miss={}
for fp in glob.glob(C+r"\*.json"):
    if fp.endswith("index.json"): continue
    try: d=json.load(io.open(fp,encoding="utf-8"))
    except: continue
    for s in d.get("sections",[]):
        for g in (s.get("groups") or []):
            for r in g.get("rows") or []:
                raw=str(r[0] or "").strip()
                if not raw or raw.startswith("（") or re.match(r"^\d+\.",raw) or raw.startswith("卷"): continue
                m=re.match(r"^([^（(]+)[（(]([^）)]*)[）)]$",raw); ch=m.group(1) if m else raw
                if ch in have or ch in alias: continue
                miss.setdefault(ch,fp)
print("真缺卡:",len(miss), list(miss)[:10])
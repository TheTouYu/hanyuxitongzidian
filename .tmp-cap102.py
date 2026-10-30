# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0
for fp in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if fp.endswith("index.json"): continue
    d=json.load(io.open(fp,encoding="utf-8")); ch=False
    for s in d.get("sections",[]):
        g=s.get("groups") or []
        if g and s.get("text"):
            t=s["text"].strip().rstrip("：:"); g0=(g[0].get("title") or "").strip().rstrip("：:")
            if t and (t==g0 or t in g0 or g0 in t):
                s["text"]=""; ch=True
    if ch:
        n+=1; json.dump(d,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cleared dup text in",n,"cards")
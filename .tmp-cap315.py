# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for p in glob.glob(os.path.join(C,"*.json")):
    if p.endswith("index.json"): continue
    d=json.load(io.open(p,encoding="utf-8")); secs=d["sections"]
    idx=[i for i,s in enumerate(secs) if s.get("key") in ("zigen","zixing") or "字形" in (s.get("label") or "")]
    if len(idx)<=1:
        if idx:
            s=secs[idx[0]]
            if not (s.get("text") or "").strip(): s["text"]="（字形库未收本字古文字形）"; n+=1
        continue
    keep=None
    for i in idx:
        if "gscroll" in (secs[i].get("text") or ""): keep=i; break
    if keep is None: keep=idx[0]
    for i in sorted(idx,reverse=True):
        if i!=keep: secs.pop(i)
    if not (secs[keep].get("text") or "").strip(): secs[keep]["text"]="（字形库未收本字古文字形）"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("去重字形栏",n)
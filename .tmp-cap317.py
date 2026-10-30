# -*- coding: utf-8 -*-
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for p in glob.glob(os.path.join(C,"*.json")):
    if p.endswith("index.json"): continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict) or "sections" not in d: continue
    secs=d["sections"]
    zx=[s for s in secs if s.get("key") in ("zigen","zixing") or "字形" in (s.get("label") or "")]
    if not zx: continue
    keep=next((s for s in zx if "gscroll" in (s.get("text") or "")), zx[0])
    if not (keep.get("text") or "").strip(): keep["text"]="（字形库未收本字古文字形）"
    out=[]
    for s in secs:
        if s in zx and s is not keep: continue
        out.append(s)
    d["sections"]=out
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("处理",n)
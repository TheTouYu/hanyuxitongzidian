# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0; moved=0
for f in glob.glob(C+r"\*.json"):
    b=f.split("\\")[-1]
    if b.startswith("卷") or b in ("index.json","variants.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    secs=d.get("sections") or []
    idx=[i for i,s in enumerate(secs) if (s.get("label") in ("所属卷",) or s.get("key") in ("suoshu","ssz","js_所属卷"))]
    if len(idx)>=1:
        keep=secs[idx[-1]]
        rest=[s for i,s in enumerate(secs) if i not in idx]
        new=rest+[keep]
        if new!=secs or len(idx)>1:
            d["sections"]=new; json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
            n+=1
            if len(idx)>1: moved+=1
print("整理所属卷",n,"多份合并",moved)
d=json.load(io.open(C+r"\奚.json",encoding="utf-8")); print([s["label"] for s in d["sections"]])
# -*- coding: utf-8 -*-
"""剥离卡文栏首的标签前缀（本義：/轉義：/辯證：/音源：/字族衍義：）。
用法: python tools/strip-labels.py [--dry]
"""
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
LAB=re.compile(r"^\s*(本義|本义|轉義|转义|辯證|辩证|音源|字族衍義|字族衍义)[：:]\s*")
dry="--dry" in sys.argv
n=0; files=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    ch=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        t2=LAB.sub("",t,count=1)
        if t2!=t: s["text"]=t2; ch=True
    if ch:
        files+=1
        if not dry: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("strip-labels:", files, "files" , "(dry)" if dry else "")
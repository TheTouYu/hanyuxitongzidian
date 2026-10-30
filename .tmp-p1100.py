# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PRE=["本義：","本义：","轉義：","转义：","辯證：","辩证：","音源：","聲母擬態：","声母拟态：","釋義：","释义：","字族衍義："]
bad=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    for s in d.get("sections",[]):
        t=(s.get("text") or "").lstrip()
        for p in PRE:
            if t.startswith(p): bad.append((d.get("char") or fn[:-5], s.get("key"), p)); break
print("残留前缀", len(bad)); print(bad[:10])
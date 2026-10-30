# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
MAP={**{n:("卷六鶴","卷六 鶴") for n in range(39,44)},**{n:("卷七斤","卷七 斤") for n in range(44,48)}}
fixed=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    bus=d.get("bus") or {}; num=bus.get("num") if isinstance(bus,dict) else None
    if num not in MAP: continue
    ch,label=MAP[num]
    sec=[s for s in d.get("sections",[]) if s.get("key")=="suoshujuan"]
    if sec:
        s=sec[0]; s["links"]=[{"ch":ch,"label":label}]; s["text"]=""
    else:
        d["sections"].append({"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":ch,"label":label}]})
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed.append(d.get("char"))
print(len(fixed),fixed[:12])
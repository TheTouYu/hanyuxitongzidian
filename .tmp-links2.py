# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; Z=r"D:\系统汉字\web\public\zigen.json"
z=json.load(io.open(Z,encoding="utf-8")); by=z.get("byName") or {}
name2num={k:(v.get("no"),v.get("juanName")) for k,v in by.items()}
MAP={**{n:("卷六鶴","卷六 鶴") for n in range(39,44)},**{n:("卷七斤","卷七 斤") for n in range(44,48)}}
fixed=[];miss=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    bus=d.get("bus") or {}; num=bus.get("num") if isinstance(bus,dict) else None
    if num is None:
        name=(bus.get("name") if isinstance(bus,dict) else None) or d.get("parent") or d.get("char")
        if name in name2num: num=name2num[name][0]
    if num not in MAP: continue
    ch,label=MAP[num]
    sec=[s for s in d.get("sections",[]) if s.get("key")=="suoshujuan"]
    if sec: s=sec[0]; s["links"]=[{"ch":ch,"label":label}]; s["text"]=""
    else: d["sections"].append({"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":ch,"label":label}]})
    if not isinstance(d.get("bus"),dict) or d["bus"].get("num") is None:
        d["bus"]={"num":num,"name":(bus.get("name") if isinstance(bus,dict) else None) or d.get("parent") or d.get("char")}
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed.append(d.get("char"))
print(len(fixed),"fixed;", fixed[:8])
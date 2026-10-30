# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cards={}
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if isinstance(d,dict) and d.get("char"): cards[d["char"]]=d
alias_owner={}
for ch,d in cards.items():
    for a in d.get("aliases") or []: alias_owner.setdefault(a,ch)
dups=[(ch,alias_owner[ch]) for ch in cards if ch in alias_owner and alias_owner[ch]!=ch]
print("dups",len(dups)); print(dups[:30])
for ch,owner in dups:
    o=cards[owner]; a=set(o.get("aliases") or []); a.add(ch); o["aliases"]=sorted(a)
    json.dump(o,io.open(os.path.join(C,owner+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    os.remove(os.path.join(C,ch+".json"))
print("merged",len(dups))
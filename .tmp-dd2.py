# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def load():
    cards={}
    for f in os.listdir(C):
        if not f.endswith(".json") or f in ("index.json","variants.json"): continue
        try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
        except Exception: continue
        if isinstance(d,dict) and d.get("char"): cards[d["char"]]=d
    return cards
cards=load()
owner={}
for ch,d in cards.items():
    for a in d.get("aliases") or []:
        owner.setdefault(a,ch)
merged=0; skipped=0
for ch in sorted(cards):
    if ch not in owner: continue
    o=owner[ch]
    if o==ch or ch not in cards or o not in cards: continue
    # 双方互指时，保留字头较“正”的一张（被更多卡引为别名者）——简单规则：保留 o
    d=cards[o]; a=set(d.get("aliases") or []); a.add(ch); d["aliases"]=sorted(a)
    json.dump(d,io.open(os.path.join(C,o+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    os.remove(os.path.join(C,ch+".json")); cards.pop(ch,None); merged+=1
print("merged",merged,"left",len(cards))
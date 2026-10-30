# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HAN=re.compile("[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]")
cards={}
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if isinstance(d,dict) and d.get("char"): cards[d["char"]]=d
fam=set(); parents=set(); erji=set()
for ch,d in cards.items():
    for s in d.get("sections",[]):
        if s.get("key")=="zizu":
            for g in s.get("groups",[]):
                for r in g.get("rows",[]):
                    m=HAN.match(str(r[0] if isinstance(r,list) and r else r))
                    if m: fam.add(m.group(0))
        if s.get("key")=="erji":
            for m in HAN.finditer(str(s.get("links") or "")+" "+str(s.get("text") or "")): erji.add(m.group(0))
    if d.get("parent"): parents.add(ch)
owner={}
for ch,d in cards.items():
    for a in d.get("aliases") or []: owner.setdefault(a,ch)
merged=[]
for ch in sorted(cards):
    if ch not in owner: continue
    o=owner[ch]
    if o==ch or o not in cards or ch not in cards: continue
    if ch in fam or ch in parents or ch in erji: continue   # 有独立条目/字族成员/二级字根，不并
    d=cards[o]; a=set(d.get("aliases") or []); a.add(ch); d["aliases"]=sorted(a)
    json.dump(d,io.open(os.path.join(C,o+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    os.remove(os.path.join(C,ch+".json")); cards.pop(ch,None); merged.append((ch,o))
print("merged",len(merged)); print(merged[:40])
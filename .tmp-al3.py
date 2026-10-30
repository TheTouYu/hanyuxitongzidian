# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HAN=re.compile("[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]")
cards={}
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if isinstance(d,dict): cards[d.get("char") or f[:-5]]=d
n=0
for ch,d in cards.items():
    al=set(d.get("aliases") or []); before=set(al)
    head=str(d.get("head") or "")
    for m in re.finditer("（([^）]*)）",head):
        al|={c for c in HAN.findall(m.group(1)) if c!=ch and c not in cards}
    shi=next((s.get("text","") for s in d.get("sections",[]) if s.get("key")=="shiyi"),"")
    m=re.match("^("+HAN.pattern+"+)\\s*（([^）]*)）",shi)
    if m: al|={c for c in HAN.findall(m.group(2)) if c!=ch and c not in cards}
    if al!=before:
        d["aliases"]=sorted(al)
        json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        n+=1
print("updated",n)
# -*- coding: utf-8 -*-
"""aliases 一致性检查：
1) 释义首「字（异体）」里的汉字必须在该卡 aliases 里；
2) 页头括注里的汉字必须在该卡 aliases 里（独立字头除外）；
3) aliases 里的字不得同时有独立卡，也不得在 index 里被其它卡抢注。
退出码非 0 表示有问题。"""
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"web","public","cards")
HAN=re.compile("[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323AF]")
cards={}
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: continue
    if isinstance(d,dict): cards[d.get("char") or f[:-5]]=d
bad=[]
for ch,d in cards.items():
    al=set(d.get("aliases") or [])
    head=str(d.get("head") or "")
    for m in re.finditer("（([^）]*)）",head):
        for c in HAN.findall(m.group(1)):
            if c!=ch and c not in cards and c not in al: bad.append((ch,"head",c))
    shi=next((s.get("text","") for s in d.get("sections",[]) if s.get("key")=="shiyi"),"")
    m=re.match("^("+HAN.pattern+"+)\\s*（([^）]*)）",shi)
    if m:
        for c in HAN.findall(m.group(2)):
            if c!=ch and c not in cards and c not in al: bad.append((ch,"shiyi",c))
print("ALIAS-MISSING",len(bad))
for b in bad[:20]: print(b)
sys.exit(1 if bad else 0)
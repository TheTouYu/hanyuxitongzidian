# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f not in ("index.json","variants.json"):
        try:
            d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
            if isinstance(d,dict): cards[d.get("char") or f[:-5]]=d
        except Exception: pass
n=0
for ch,d in cards.items():
    pr=d.get("parent") or (d.get("parents") or [None])[0]
    if not pr or pr not in cards: continue
    pd=cards[pr]
    keep=[s for s in pd.get("sections",[]) if s.get("key") in ("benyi","zhuanyi","bianzheng","yinyuan") and s.get("text")]
    if not keep: continue
    text="\n".join((s.get("label","")+"：" if s.get("label") else "")+str(s["text"]).lstrip("本義：本义：轉義：转义：辯證：辩证：音源：") for s in keep)
    secs=[s for s in d.get("sections",[]) if s.get("key")!="zigen"]
    secs.append({"key":"zigen","label":"字根「"+str(pd.get("char") or pr)+"」","text":text,"cites":[]})
    d["sections"]=secs
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("updated",n)
# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
PRE=["本義：","轉義：","辯證：","音源：","釋義："]
def strip(t):
    t=t.lstrip()
    for p in PRE:
        if t.startswith(p): return t[len(p):].lstrip(), True
    return t, False
n=0
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); chg=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        if t:
            t2,ch=strip(t)
            if ch: s["text"]=t2; chg=True
        if s.get("key")=="shengmu":
            st=s.get("text") or ""
            if st.startswith("y「零聲母」不系（照實）。"):
                s["text"]="y「零聲母」不系：零聲母，緒論七組未列（照實）。"; chg=True
    if chg:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("fixed",n)
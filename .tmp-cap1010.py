# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0; miss=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json",): continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or fn[:-5]
    head=d.get("head") or ""
    m=re.search(r"[（(]([^）)]*)[）)]",head)
    if not m: continue
    al=set(d.get("aliases") or [])
    add=[c for c in m.group(1) if "\u3400"<=c<="\u9fff" and len(c)==1 and c!=ch]
    before=len(al); al|=set(add)
    if len(al)!=before:
        d["aliases"]=sorted(al); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补别名卡数",n)
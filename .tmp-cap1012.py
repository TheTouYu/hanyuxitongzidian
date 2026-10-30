# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
print("尸 head:",json.load(io.open(os.path.join(C,"尸.json"),encoding="utf-8")).get("head"))
def ishan(c): return len(c)==1 and ("\u3400"<=c<="\u9fff" or "\U00020000"<=c<="\U0002FA1F")
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or fn[:-5]; head=d.get("head") or ""
    m=re.search(r"[（(]([^）)]*)[）)]",head)
    if not m: continue
    add=[c for c in m.group(1) if ishan(c) and c!=ch]
    if not add: continue
    al=set(d.get("aliases") or []); before=len(al); al|=set(add)
    if len(al)!=before:
        d["aliases"]=sorted(al); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补别名卡数",n)
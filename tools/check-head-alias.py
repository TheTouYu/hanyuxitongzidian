# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
files=[f for f in os.listdir(C) if f.endswith(".json") and f not in ("index.json","variants.json")]
CJK=re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002A6DF]")
bad=[]
for f in files:
    p=os.path.join(C,f); d=json.load(io.open(p,encoding="utf-8"))
    if isinstance(d,list): bad.append((f,"数组")); continue
    head=d.get("head") or ""; me=d.get("char") or f[:-5]
    m=re.search(r"[（(]([^）)]*)[）)]",head)
    if not m: continue
    al=set(d.get("aliases") or [])
    miss=[ch for ch in CJK.findall(m.group(1)) if ch!=me and ch not in al and not os.path.exists(os.path.join(C,ch+".json"))]
    if miss: bad.append((me,"".join(miss)))
print("HEAD-ALIAS-MISSING",len(bad),bad[:10])
sys.exit(1 if bad else 0)
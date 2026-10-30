# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(C+r"\variants.json",encoding="utf-8"))
idx=json.load(io.open(C+r"\index.json",encoding="utf-8"))
def hit(q): return any(x.get("c")==q or q in (x.get("a") or []) for x in idx)
miss=[s for s in V if not hit(s)]
print("索引",len(idx),"条；繁简表简字",len(V),"个；搜不到的简字",len(miss))
print("前50:", "".join(miss[:50]))
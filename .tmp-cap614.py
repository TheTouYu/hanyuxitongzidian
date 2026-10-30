# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"𧌌.json")
if os.path.exists(p):
    d=json.load(io.open(p,encoding="utf-8"))
    print({k:d.get(k) for k in ("char","head","pinyin","level","parent")})
    print([ (s.get("key"),s.get("text","")[:40]) for s in d.get("sections",[])])
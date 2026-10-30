# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(os.path.join(C,"variants.json"),encoding="utf-8"))
add={"龁":"齕","纥":"紇","饩":"餼","讫":"訖","鹡":"鶺","纥":"紇"}
for s,t in add.items():
    V.setdefault(s,[]); 
    if t not in V[s]: V[s].append(t)
json.dump(V,io.open(os.path.join(C,"variants.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for ch in ("𪗟","𥾨","氣","𧥷"):
    p=os.path.join(C,ch+".json")
    print(ch,os.path.exists(p))
# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\佀.json"
d=json.load(io.open(p,encoding="utf-8"))
d["simp"]="似"; d["aliases"]=sorted(set((d.get("aliases") or [])+["似"]))
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("佀 patched",d.get("simp"),d.get("aliases"))
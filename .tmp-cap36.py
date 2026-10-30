# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("灩","滟","𤅿","淡","淊","豔","豓","𡤩","艳"):
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["trad"]=ch
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("trad reset")
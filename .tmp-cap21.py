# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("𧧘","栬","𨋭","𡜆","脃"):
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["bus"]=[{"num":10,"name":"示"}]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("bus restored")
# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("攉",):
    p=r"D:\系统汉字\web\public\cards\%s.json"%ch
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu":
            s["text"]="h「豁活」取「活」：手反覆揮攉，往復而活（推）。"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("ok",ch)
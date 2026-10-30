# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
x=json.load(io.open(p,encoding="utf-8")); m=x.get("photos") or x
for ch in ("藘",):
    if ch in m: m.pop(ch); print("removed",ch)
json.dump({"photos":m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
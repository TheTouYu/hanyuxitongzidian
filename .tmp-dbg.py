# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\戹.json",encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            print(g.get("no"), g.get("title"), [r[0] for r in g["rows"]])
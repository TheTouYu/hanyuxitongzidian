# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
# 先建 char -> head 映射
head = {}
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn == "index.json":
        continue
    d = json.load(io.open(os.path.join(C, fn), encoding="utf-8"))
    h = d.get("head") or d.get("char")
    if h and "（" in h:
        head[d.get("char") or fn[:-5]] = h
n = 0
files = 0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn == "index.json":
        continue
    p = os.path.join(C, fn)
    d = json.load(io.open(p, encoding="utf-8"))
    hit = False
    for s in d.get("sections", []):
        for g in (s.get("groups") or []):
            for r in (g.get("rows") or []):
                if not r:
                    continue
                first = str(r[0])
                core = first.split("（")[0].strip()
                if "（" not in first and core in head:
                    r[0] = head[core]
                    hit = True
                    n += 1
    if hit:
        files += 1
        json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("filled", n, "cells in", files, "cards")

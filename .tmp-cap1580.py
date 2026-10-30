# -*- coding: utf-8 -*-
import json, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
PY = r"[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]{1,12}"
n = 0
files = 0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn == "index.json":
        continue
    p = os.path.join(C, fn)
    d = json.load(io.open(p, encoding="utf-8"))
    ch = d.get("char") or fn[:-5]
    hit = False
    for s in d.get("sections", []):
        t = s.get("text") or ""
        m = re.match(r"^" + re.escape(ch) + PY + r"\s*[：:]\s*", t)
        if m:
            s["text"] = t[m.end():]
            hit = True
            n += 1
    if hit:
        files += 1
        json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("stripped", n, "in", files, "cards")

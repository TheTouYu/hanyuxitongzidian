# -*- coding: utf-8 -*-
import json, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
n = 0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn == "index.json":
        continue
    p = os.path.join(C, fn)
    d = json.load(io.open(p, encoding="utf-8"))
    if d.get("parent") != "次" and d.get("char") != "次":
        continue
    for s in d["sections"]:
        if s["key"] != "shengmu":
            continue
        t = s["text"]
        m = re.match(r'^([a-zA-Z]{1,2})「([^」]+)」「\2」', t)
        if m:
            s["text"] = m.group(1) + "「" + m.group(2) + "」" + t[m.end():]
            n += 1
    json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("dedup", n)
# 放宽检查器：零声母「不系」
p = r"D:\系统汉字\tools\check-bu.py"
t = io.open(p, encoding="utf-8").read()
old = 'SM = re.compile(r"^[a-zA-Z]{1,2}「[^」]+」取「[^」]」：")'
new = 'SM = re.compile(r"^[a-zA-Z]{1,2}「[^」]+」(取「[^」]」：|不系：)")'
if old in t:
    io.open(p, "w", encoding="utf-8", newline="\n").write(t.replace(old, new))
    print("checker updated")

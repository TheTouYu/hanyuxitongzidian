# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
# 䪢 同属 次、𠂔 两声，标双父
p = os.path.join(C, "䪢.json")
d = json.load(io.open(p, encoding="utf-8"))
d["parent"] = "𠂔"
d["parents"] = ["次", "𠂔"]
json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# 检查器放宽：允许 parents 含本部
p = r"D:\系统汉字\tools\check-bu.py"
t = io.open(p, encoding="utf-8").read()
if "parents" not in t:
    old = "应为 {bu}"
    t = t.replace('d.get("parent") != bu', '(d.get("parent") != bu and bu not in (d.get("parents") or []))')
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("checker relaxed")
else:
    print("already")
print("䪢 parents set")

# -*- coding: utf-8 -*-
import json, io, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
p = os.path.join(C, "㳄.json")
d = json.load(io.open(p, encoding="utf-8"))
d.pop("rootChain", None)
d["rootLabel"] = "次（㳄）"
json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
p = r"D:\系统汉字\.tmp-rel2.py"
t = io.open(p, encoding="utf-8").read()
t = t.replace('"rc":d.get("rootChain",[]),', '"rc":d.get("rootChain",[]),"rlb":d.get("rootLabel",""),', 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h = io.open(f, encoding="utf-8").read(); o = h
    h = h.replace("const rl=chain.length?chain.map(ln).join(' → '):'—';",
                  "const rl=t.rlb?esc(t.rlb):(chain.length?chain.map(ln).join(' → '):'—');")
    if h != o:
        io.open(f, "w", encoding="utf-8", newline="\n").write(h)
        print(f.split("\\")[-1], "patched")
print("㳄 rootLabel set")

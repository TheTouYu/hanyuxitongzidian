# -*- coding: utf-8 -*-
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
p = C + r"\㳄.json"
d = json.load(io.open(p, encoding="utf-8"))
d.pop("rootLabel", None)
d["rootChain2"] = [{"ch": "欠", "label": "欠"}, {"ch": "㳄", "label": "次（㳄）"}]
json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
p = r"D:\系统汉字\.tmp-rel2.py"
t = io.open(p, encoding="utf-8").read()
t = t.replace('"rlb":d.get("rootLabel",""),', '"rlb":d.get("rootLabel",""),"rc2":d.get("rootChain2",[]),', 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(t)
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h = io.open(f, encoding="utf-8").read(); o = h
    h = h.replace("const rl=t.rlb?esc(t.rlb):(chain.length?chain.map(ln).join(' → '):'—');",
                  "const rl=t.rlb?esc(t.rlb):((t.rc2&&t.rc2.length)?t.rc2.map(o=>'<a data-c=\\\"'+esc(o.ch)+'\\\" style=\\\"color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer\\\">'+esc(o.label)+'</a>').join(' → '):(chain.length?chain.map(ln).join(' → '):'—'));")
    if h != o:
        io.open(f, "w", encoding="utf-8", newline="\n").write(h)
        print(f.split("\\")[-1], "patched")
print("ok")

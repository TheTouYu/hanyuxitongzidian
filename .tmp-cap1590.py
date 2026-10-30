# -*- coding: utf-8 -*-
import json, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
G = {"c":"刺持","ch":"刺持","z":"凿总","zh":"凿总","j":"聚决","q":"亲缺","x":"续消","s":"失收","sh":"失收",
     "t":"涂突","h":"豁活","l":"拢离","m":"蒙末","b":"闭剥","p":"拼辟","f":"附分","d":"囤动","n":"纳弄",
     "r":"柔锐","k":"口控","g":"隔估"}
n = 0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn == "index.json":
        continue
    p = os.path.join(C, fn)
    d = json.load(io.open(p, encoding="utf-8"))
    if d.get("parent") != "𠂔":
        continue
    for s in d.get("sections", []):
        if s.get("key") != "shengmu":
            continue
        t = s.get("text", "")
        if t.startswith("不取義"):
            s["text"] = t
            break
        m = re.match(r"^([a-zA-Z]{1,2})取「([^」]+)」", t)
        if m:
            letter = m.group(1).lower()
            s["text"] = letter + "「" + G.get(letter, "凿总") + "」取「" + m.group(2) + "」" + t[m.end():]
            n += 1
    json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("normalized", n)
p = r"D:\系统汉字\tools\check-bu.py"
t = io.open(p, encoding="utf-8").read()
old = 'SM = re.compile(r"^[a-zA-Z]{1,2}「[^」]+」(取「[^」]」：|不系：)")'
new = 'SM = re.compile(r"^([a-zA-Z]{1,2}「[^」]+」(取「[^」]」：|不系：)|不取義：)")'
if old in t:
    io.open(p, "w", encoding="utf-8", newline="\n").write(t.replace(old, new))
    print("checker updated")
else:
    print("checker pattern not found:", "SM = re.compile" in t)

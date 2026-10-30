# -*- coding: utf-8 -*-
import json, io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
C = r"D:\系统汉字\web\public\cards"
G = {"c":"刺持","z":"凿总","zh":"凿总","j":"聚决","q":"亲缺","x":"续消","s":"失收","f":"附分",
     "b":"闭剥","p":"拼辟","t":"涂突","h":"豁活","l":"拢离","m":"蒙末","d":"囤动","n":"纳弄","r":"柔锐","k":"口控","g":"隔估"}
n = 0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn == "index.json":
        continue
    p = os.path.join(C, fn)
    d = json.load(io.open(p, encoding="utf-8"))
    if d.get("parent") not in ("卽", "肥"):
        continue
    for s in d["sections"]:
        if s["key"] != "shengmu":
            continue
        t = s["text"]
        m = re.match(r"^([a-zA-Z]{1,2})取「([^」]+)」", t)
        if m:
            le = m.group(1).lower()
            s["text"] = le + "「" + G.get(le, "凿总") + "」取「" + m.group(2) + "」" + t[m.end():]
            n += 1
    json.dump(d, io.open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("normalized", n)

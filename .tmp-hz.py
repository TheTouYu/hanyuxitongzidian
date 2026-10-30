# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\畫.json"
d=json.load(io.open(p,encoding="utf-8"))
M={"劃":"刀","嫿":"女","繣":"糸","澅":"水","㗲":"口","㦎":"心","䐸":"肉","㩇":"手","𢄶":"巾","𨐶":"辛","𥊮":"目"}
for s in d["sections"]:
    if s.get("key")=="zizu":
        for g in s.get("groups",[]):
            for r in g.get("rows",[]):
                base=r[0].split("（")[0]
                if base in M: r[2]=M[base]
        print([ (r[0],r[2]) for r in s["groups"][0]["rows"] ])
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
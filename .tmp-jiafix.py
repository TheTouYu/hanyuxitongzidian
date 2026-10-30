# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"加.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            g["rows"]=[r for r in g["rows"] if re.match(r"^[\u3400-\u9fff\U00020000-\U0002A6DF]", r[0])]
            print(g.get("no"),len(g["rows"]))
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
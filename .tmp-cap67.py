# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            if g["title"].startswith("③"):
                g["rows"]=[["𩔧（類）","lèi","頁","《龍龕》：「𩔧，俗；類，正。音淚。」類，《玉篇》：「獸名、種類也、法也。」《集韻》：「偏頗也。」「似也。」"]]
print(open(p,encoding="utf-8").read().find("𩔧")>0)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
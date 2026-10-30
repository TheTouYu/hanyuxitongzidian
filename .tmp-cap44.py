# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\貍.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            for r in g["rows"]:
                if r[0]=="㦟":
                    r[3]="《玉篇》「慧也」聰明——原文只录「慧」，未言取貍何义，照录不推"
print("fixed 㦟")
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
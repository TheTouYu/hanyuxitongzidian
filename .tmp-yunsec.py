# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"彥.json"); d=json.load(io.open(p,encoding="utf-8"))
secs=d["sections"]
if not any(s.get("key")=="canzheng" for s in secs):
    secs.insert(len(secs)-1,{"key":"canzheng","label":"附：云","text":"彥所从「云」（郭店緇衣，戰國）——此形屬「云」，非彥字本身之形，故別出附此。","gimgs":["云/01.png"]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([s.get("label") for s in d["sections"]])
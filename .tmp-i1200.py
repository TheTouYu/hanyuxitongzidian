# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\弔.json"
d=json.load(io.open(p,encoding="utf-8"))
txt=("本義：象人身上纏著弋線之形。{{benyi/01.png}}指有線繩的箭，即弋；{{benyi/02.png}}指人。"
"弋線繩委于人，象意弋射出去後的回收。後或楷化作“吊”，《字彙》：“俗弔字。”可謂“鈟（diào）”的異文，《字彙》：“同釣。”《說文》：“釣，鉤魚。”")
for s in d["sections"]:
    if s.get("key")=="benyi":
        s["text"]=txt; s["gdir"]="inline/弔"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
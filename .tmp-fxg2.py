# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\匃.json"; d=json.load(open(p,encoding="utf-8"))
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g["rows"]:
            if r[0].startswith("𠣣"):
                r[2]=""
                r[3]="丐、匃本同，是匃的疊體寫法，強化乞求之狀（《字彙補》「與匄同。乞也」）"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
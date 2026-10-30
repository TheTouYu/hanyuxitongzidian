# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\匃.json"; d=json.load(open(p,encoding="utf-8"))
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g["rows"]:
            if r[0]=="鈣":
                r[2]="金（形旁）"
                r[3]="新拉丁 calx 的音譯：聲旁「丐」只記音、不取義；金旁定其為金屬——一種金屬元素，銀白色結晶，有延展性"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
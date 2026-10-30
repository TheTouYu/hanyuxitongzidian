# -*- coding: utf-8 -*-
import json,copy,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=rf"{C}\匃.json"; d=json.load(open(p,encoding="utf-8"))
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g["rows"]:
            if r[0].startswith("𠣣"):
                r[2]="匃（异体叠体）"
                r[3]="《字彙補》「與匄同。乞也」——匃的疊體寫法，強化乞求之狀"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 镜像卡 𠣣
base=json.load(open(p,encoding="utf-8")); m=copy.deepcopy(base)
m["char"]="𠣣"; m["trad"]="𠣣"; m["simp"]="匃"
for s in m["sections"]:
    if s["key"]=="benyi":
        s["text"]="字源依本字「匃」（𠣣為其疊體異體，強化乞求之狀）："+s["text"].split("：",1)[-1]
json.dump(m,open(rf"{C}\𠣣.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed + mirror 𠣣")
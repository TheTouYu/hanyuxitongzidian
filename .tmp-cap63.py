# -*- coding: utf-8 -*-
import re,io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open(r"D:\系统汉字\knowledge\hanzi-yinyuan\02b-shi-shi.md",encoding="utf-8").read()
m=re.search(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### 士部：家、嫁、稼、幏、榢一组表成家",t)
print("claim",m.group(1) if m else None)
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu": s["groups"][0]["title"]="①家、嫁、稼、幏、榢一组表成家"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
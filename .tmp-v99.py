# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8"))
    s0=len(d.get("sections") or [])
    d["sections"]=[s for s in d.get("sections",[]) if (s.get("label") or s.get("key")) not in ("所属卷","suoshu")]
    if len(d["sections"])!=s0:
        json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("卷卡删所属卷",n)
d=json.load(io.open(C+r"\卷一雞.json",encoding="utf-8")); print([s["label"] for s in d["sections"]])
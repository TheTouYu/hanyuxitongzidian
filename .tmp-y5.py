# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\巳.json"
d=json.load(io.open(p,encoding="utf-8"))
d["aliases"]=sorted(set((d.get("aliases") or [])+["已"]))
for s in d["sections"]:
    if s.get("key")=="benyi" and "「已」" not in s["text"]:
        s["text"]+="另「已」與「巳」隸變相混，古亦與「㠯」通作，檢索時以「已」可查到本卡。"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
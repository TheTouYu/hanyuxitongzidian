# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\兮.json"
d=json.load(io.open(p,encoding="utf-8"))
d["sections"]=[s for s in d["sections"] if s.get("key")!="cankao"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([s.get("key") for s in d["sections"]])
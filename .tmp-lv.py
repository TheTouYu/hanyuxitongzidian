# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\慮.json"
d=json.load(io.open(p,encoding="utf-8"))
d["level"]=3; d["parent"]="盧"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(d["char"],d["level"],d["parent"])
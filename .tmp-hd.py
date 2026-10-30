# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\橐.json"
d=json.load(io.open(p,encoding="utf-8"))
d["head"]="橐（槖𢅍𡇈）"
d["aliases"]=sorted({"槖","\U0002114D","\u3f08"} if False else {"槖","𢅍","𡇈"})
for s in d.get("sections",[]):
    pass
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(d["head"],d["aliases"])
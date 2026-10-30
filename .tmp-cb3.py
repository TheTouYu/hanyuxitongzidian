# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-bu.py"
t=io.open(p,encoding="utf-8").read()
old='        if d.get("parent") != parent and parent not in (d.get("parents") or []):'
new='        if d.get("parent") != parent and parent not in (d.get("parents") or []) and parent not in (d.get("multi") or []):'
print(old in t); io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
q=r"D:\系统汉字\web\public\cards\斫.json"
d=json.load(io.open(q,encoding="utf-8")); d.pop("multi",None); d["parents"]=["石","斤"]
json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
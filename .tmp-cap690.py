import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\芪.json",encoding="utf-8"))
print("芪 bus",d.get("bus"),"parent",d.get("parent"),"level",d.get("level"),"head",d.get("head"))
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print("idx芪",[x for x in idx if x.get("c")=="芪"])
print("矢 idx",[x for x in idx if x.get("c")=="矢"][:1])
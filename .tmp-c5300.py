import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\夷.json",encoding="utf-8"))
print("lv",d.get("level"),"parent",d.get("parent"),"rl",d.get("rootLevel"),"head",d.get("head"))
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for x in idx:
    if x.get("c")=="夷": print("idx",x)
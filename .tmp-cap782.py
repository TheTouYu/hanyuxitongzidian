import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\台.json",encoding="utf-8"))
print("head",d.get("head"),"aliases",d.get("aliases"),"parent",d.get("parent"))
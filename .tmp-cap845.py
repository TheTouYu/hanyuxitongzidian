import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
v=json.load(io.open(r"D:\系统汉字\web\public\variants.json",encoding="utf-8"))
print("variants 条数",len(v),"薹",v.get("薹"),"擡",v.get("擡"))
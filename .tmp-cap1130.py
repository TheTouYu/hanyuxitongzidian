import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\尸.json",encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="suoshujuan": print(s)
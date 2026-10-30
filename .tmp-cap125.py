import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\㠯.json",encoding="utf-8"))
print(json.dumps(d["sections"][-1],ensure_ascii=False)[:300])
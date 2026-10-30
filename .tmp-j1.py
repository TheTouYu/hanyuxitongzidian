import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\卷一雞.json",encoding="utf-8"))
print(json.dumps(d["sections"][0],ensure_ascii=False)[:200])
print(json.dumps(d["sections"][1]["groups"][0]["rows"][:2],ensure_ascii=False)[:200])
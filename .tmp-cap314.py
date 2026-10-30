import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\帝.json",encoding="utf-8"))
print([ (s["label"],len(s["text"])) for s in d["sections"]])
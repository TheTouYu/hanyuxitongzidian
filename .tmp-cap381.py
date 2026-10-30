import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("帝","啇"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print(ch,[(s["label"],s["text"][:12]) for s in d["sections"]][:4])
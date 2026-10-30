import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("帝","市","示"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print(ch,[(s["key"],bool(s.get("gimgs")),len(s.get("gimgs") or [])) for s in d["sections"]])
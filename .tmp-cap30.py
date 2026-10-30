import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("𧧘","𨋭"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print(ch,repr(d.get("char")),d.get("noRoot"),repr(d.get("pinyin")))
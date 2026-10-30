import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print(type(idx), len(idx))
for x in idx:
    if x.get("c") in ("𧧘","𨋭","栬","𡜆","脃"):
        print(repr(x.get("c")),[hex(ord(ch)) for ch in x.get("c")],x.get("lv"),x.get("pr"),x.get("a"))
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos\index.json"
ph=json.load(io.open(P,encoding="utf-8"))["photos"]
for ch in ("ㄗ","卽","肥","配","邑","印","氾"):
    print(ch,ph.get(ch))
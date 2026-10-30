import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ix=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8"))["photos"]
for c in ("睪","釋","擇","澤","鐸","鸅"):
    print(c,ix.get(c))
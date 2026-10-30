import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
try:
    import json,io
    d=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
    print("ok chars",len(d.get("chars",{})))
except Exception as e: print("BROKEN",e)
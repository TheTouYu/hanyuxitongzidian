import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
try:
    d=json.load(io.open(p,encoding="utf-8")); print("ok chars",len(d["chars"]),"has𦣞","𦣞" in d["chars"])
except Exception as e: print("broken",e)
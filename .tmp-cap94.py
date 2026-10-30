import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
print("ok",len(d["chars"]),"䒬",d["chars"]["䒬"]["files"])
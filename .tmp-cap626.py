import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
g=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
ch=g.get("chars",g)
for k in ("智","知"):
    print(k, ch.get(k))
for d in ("智","知"):
    p=rf"D:\系统汉字\web\public\glyphs\{d}"
    print(d, os.path.isdir(p) and sorted(os.listdir(p))[:6])
import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
g=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
ch=g.get("chars") or g
for k in ("質","质","斦"): print(k, (ch.get(k) or {}).get("files") and len(ch[k]["files"]))
t=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=t.find("GLYPH["); print(t[i-160:i+120].replace("\n"," ")[:320])
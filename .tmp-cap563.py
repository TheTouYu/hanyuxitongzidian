import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
g=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))
ch=g.get("chars") or g
print("字条",len(ch),"斦",ch.get("斦"),"質",len((ch.get("質") or {}).get("files") or []))
print(os.listdir(r"D:\系统汉字\web\public\glyphs\斦"))
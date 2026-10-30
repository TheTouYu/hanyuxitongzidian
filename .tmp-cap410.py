import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
gi=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))["chars"]
print("idx𦣞",gi.get("𦣞"))
d=r"D:\系统汉字\web\public\glyphs\𦣞"
print("dir", os.path.isdir(d) and len(os.listdir(d)))
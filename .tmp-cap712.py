import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
d=json.load(io.open(p,encoding="utf-8"))
print("keys",list(d.keys())[:5],"chars",len(d.get("chars",{})),"size",os.path.getsize(p))
print("到",d["chars"].get("到"))
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("GLYPH="); print(h[i-80:i+120].replace("\n"," "))
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
print(os.listdir(os.path.join(P,"啇")))
ix=json.load(io.open(P+r"\index.json",encoding="utf-8")); print(ix.get("photos",ix).get("啇"))
f=os.path.join(P,"啇",os.listdir(os.path.join(P,"啇"))[0])
print(open(f,"rb").read(4))
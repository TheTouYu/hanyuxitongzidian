import json,io,os,sys,hashlib
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
ix=json.load(io.open(P+r"\index.json",encoding="utf-8")); ph=ix.get("photos") or ix
for c in ("款","𨜿","祟","柰"):
    print(c, ph.get(c), os.path.isdir(P+os.sep+c) and sorted(os.listdir(P+os.sep+c)))
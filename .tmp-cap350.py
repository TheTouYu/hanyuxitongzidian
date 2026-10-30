import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
ix=json.load(io.open(P+r"\index.json",encoding="utf-8")); ph=ix.get("photos") or ix
cp=json.load(io.open(P+r"\captions.json",encoding="utf-8")).get("captions")
for c in ("蒂","帝","啇"):
    print(c, ph.get(c), os.path.isdir(P+os.sep+c) and sorted(os.listdir(P+os.sep+c)), cp.get(c))
import json,io,glob,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
P=r"D:\系统汉字\web\public\glyphs\photos"
ph=json.load(io.open(P+r"\index.json",encoding="utf-8")); ph=ph.get("photos") or ph
lv3=[c for c in ph if os.path.exists(C+os.sep+c+".json") and json.load(io.open(C+os.sep+c+".json",encoding="utf-8")).get("level")==3]
print("有图的 level3 卡:",len(lv3))
print(lv3[:25])
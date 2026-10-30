import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
p=C+r"\戠.json"; d=json.load(io.open(p,encoding="utf-8")); d["photos"]=["01.png"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
i=json.load(io.open(P+r"\index.json",encoding="utf-8")); ph=i.get("photos") or i; ph["戠"]=["01.png"]
json.dump({"photos":ph},io.open(P+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print("ok")
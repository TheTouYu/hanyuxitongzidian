import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
d=json.load(io.open(C+r"\弔.json",encoding="utf-8")); d["photos"]=["01.png"]
json.dump(d,io.open(C+r"\弔.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
i=json.load(io.open(P+r"\index.json",encoding="utf-8")); (i.get("photos") or i)["弔"]=["01.png"]
json.dump({"photos":(i.get("photos") or i)},io.open(P+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print("ok")
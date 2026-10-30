import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
cap=json.load(io.open(P+r"\captions.json",encoding="utf-8")); cm=cap.get("captions") or cap
cm["曳"]=["《弋射圖》局部（戰國）"]
json.dump({"captions":cm},io.open(P+r"\captions.json","w",encoding="utf-8"),ensure_ascii=False)
C=r"D:\系统汉字\web\public\cards\曳.json"
d=json.load(io.open(C,encoding="utf-8")); d["captions"]=["《弋射圖》局部（戰國）"]
json.dump(d,io.open(C,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("ok")
import io,json,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\卷八虎.json",encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for r in s["groups"][0]["rows"]: print(r[0],"|",r[2][:26],"|",r[3][:18])
PH=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8")); PH=PH.get("photos") or PH
print("photos for 卷八虎", len(PH.get("卷八虎",[])))
import json,io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\責.json",encoding="utf-8"))
print("責 photos",d.get("photos"),"captions",d.get("captions"))
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("photoBlock")
print(h[i:i+700])
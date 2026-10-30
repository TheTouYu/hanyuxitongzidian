import json,io,sys,urllib.request
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\帝.json",encoding="utf-8"))
print([s["label"] for s in d["sections"]])
t=urllib.request.urlopen("http://127.0.0.1:8091/test.html",timeout=5).read().decode("utf-8","replace")
print("page has filter fix:", "includes('gscroll')" in t)
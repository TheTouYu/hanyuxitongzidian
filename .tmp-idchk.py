import json,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
print("n",len(d))
for ch in ("㤅","旡","疑","贛","欠"):
    print(ch, any(x.get("c")==ch for x in d))
print(os.path.exists(r"D:\系统汉字\web\public\cards\㤅.json"))
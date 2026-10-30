import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
print("到",ph.get("到"), os.path.isdir(os.path.join(P,"到")) and os.listdir(os.path.join(P,"到")))
print("荎",ph.get("荎"))
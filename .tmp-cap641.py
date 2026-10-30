import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
for c in ("醫","翳"):
    print(c, os.listdir(os.path.join(P,c)))
cm=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cm.get("captions") or cm
print({k:cm.get(k) for k in ("醫","翳")})
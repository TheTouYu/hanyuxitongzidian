import json,io,subprocess,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
def load(p):
    d=json.load(io.open(p,encoding="utf-8")); return d.get("photos") or d, list(d.keys())
for p in (r"D:\系统汉字\web\public\glyphs\photos\index.json", r"D:\系统汉字\web\public\glyphs\photos\captions.json"):
    m,k=load(p); print(p.split("\\")[-1], len(m), k[:4])
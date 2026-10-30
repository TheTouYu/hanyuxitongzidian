import json,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ph=json.load(open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8"))
ph=ph.get("photos") or ph
for ch in "旨耆鳍鰭脂":
    print(ch,len(ph.get(ch,[]) or []))
print("dirs:", [d for d in os.listdir(r"D:\系统汉字\web\public\glyphs\photos") if d in ("旨","耆")])
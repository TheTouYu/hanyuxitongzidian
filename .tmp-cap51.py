import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ph=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8")).get("photos")
print("霾:",ph.get("霾"),"貍:",ph.get("貍"),"士:",ph.get("士"))
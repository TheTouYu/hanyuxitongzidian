import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ph=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8"))["photos"]
cp=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\captions.json",encoding="utf-8"))["captions"]
print("尸 photos",ph.get("尸"),"caps",cp.get("尸"))
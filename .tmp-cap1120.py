import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ph=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\index.json",encoding="utf-8"))["photos"]
print("尸",ph.get("尸"),"files",os.listdir(r"D:\系统汉字\web\public\glyphs\photos\尸"))
print("vol cards",[os.path.basename(x) for x in glob.glob(r"D:\系统汉字\web\public\cards\卷三*.json")])
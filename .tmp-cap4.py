import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("士","牡"):
    d=r"D:\系统汉字\web\public\glyphs\photos"+chr(92)+ch
    print(ch, os.listdir(d) if os.path.isdir(d) else None)
cap=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\captions.json",encoding="utf-8"))
print("士",cap.get("士"),"牡",cap.get("牡"))
import os,json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("士","野","牡"):
    d=os.path.join(r"D:\系统汉字\web\public\glyphs\photos",ch)
    print(ch, sorted(os.listdir(d)) if os.path.isdir(d) else None)
cap=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\captions.json",encoding="utf-8"))
for ch in ("士","野","牡"): print("cap",ch,cap.get(ch))
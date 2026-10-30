import io,json,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ["犬","秋","虎","虍","果","耳","門"]:
    p=os.path.join(C,ch+".json"); print(ch, os.path.exists(p))
d=json.load(io.open(os.path.join(C,"犬.json"),encoding="utf-8")) if os.path.exists(os.path.join(C,"犬.json")) else None
print("犬 level",d and d.get("level"),"bus",d and d.get("bus"))
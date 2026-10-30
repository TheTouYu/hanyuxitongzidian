import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("ㄗ","意"):
    d=json.load(io.open(C+"\\"+ch+".json",encoding="utf-8"))
    for s in d["sections"]:
        for g in (s.get("groups") or []):
            print(ch,g["title"],[r[0] for r in g["rows"]][:5])
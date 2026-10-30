import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("蒂","碲"):
    d=json.load(io.open(rf"{C}\{ch}.json",encoding="utf-8"))
    print(ch,"bus",d.get("bus"),"lv",d.get("level"),"paren",d.get("parent"))
    for s in d["sections"]: print("  ",s["label"],"|",(s.get("text") or "")[:60],"|links",s.get("links"))
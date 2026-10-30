import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("翄","衼","跂","支"):
    d=json.load(io.open(rf"{C}\{ch}.json",encoding="utf-8"))
    print(ch,"head",d.get("head"),"aliases",d.get("aliases"))
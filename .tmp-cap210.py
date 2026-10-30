import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
B=json.load(io.open(r"D:\系统汉字\.tmp-photoB.json",encoding="utf-8"))
for c in ("蒂","款","帝"):
    print(c,B["caps"].get(c))
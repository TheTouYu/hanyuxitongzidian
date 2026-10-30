import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("㑘","⿅"):
    try:
        d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
        print(ch, {k:d.get(k) for k in ("char","parent","bus","level")}, [s["key"] for s in d["sections"]])
    except Exception as e: print(ch,"err")
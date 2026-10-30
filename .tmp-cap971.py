import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
idx=json.load(io.open(r"D:\系统汉字\web\public\cards\index.json",encoding="utf-8"))
for ch in ("户","斤","方","氏","歹"):
    print(ch,[x for x in idx if x.get("c")==ch][:1])
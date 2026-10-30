import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("市","示","帝"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    s=[x for x in d["sections"] if x["key"] in ("suoshujuan","suoshu")]
    print(ch,[{k:v for k,v in x.items() if k!="cites"} for x in s])
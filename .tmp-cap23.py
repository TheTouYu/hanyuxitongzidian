import os,sys,json,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for p in ("兌","危","包","巵"):
    print(p, os.path.exists(os.path.join(C,p+".json")))
idx=json.load(io.open(os.path.join(C,"index.json"),encoding="utf-8"))["cards"]
for ch in ("𧧘","栬","𨋭","𡜆","脃"):
    print(ch, any(x.get("c")==ch for x in idx))
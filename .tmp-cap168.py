import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("讫","訖","迄"):
    print(ch,"card:",os.path.exists(os.path.join(C,ch+".json")))
idx=json.load(io.open(os.path.join(C,"index.json"),encoding="utf-8"))
for ch in ("讫","訖"):
    hit=[x for x in idx if x.get("c")==ch or ch in (x.get("a") or [])]
    print(ch,"idx:",hit[:1])
cm=json.load(io.open("D:\\系统汉字\\.tmp-charmap.json",encoding="utf-8")) if os.path.exists("D:\\系统汉字\\.tmp-charmap.json") else {}
print("charmap:",[k for k in cm if k in ("讫","訖")])
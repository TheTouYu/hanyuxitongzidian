import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=False
    for s in d.get("sections",[]):
        if s.get("key")=="shi": s["key"]="shiyi"; s["label"]="释义"; ch=True
    if ch:
        d["sections"].sort(key=lambda s:{"benyi":0,"benyi2":1,"zhuanyi":2,"bianzheng":3,"yinyuan":4,"shiyi":5,"shengmu":6,"zizu":7,"zigen":8}.get(s["key"],9))
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改为 shiyi 并排序",n)
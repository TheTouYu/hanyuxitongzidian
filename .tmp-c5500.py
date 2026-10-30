import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if d.get("level")==3 and d.get("parent") and not d.get("rootLevel"):
        bad.append(d.get("char"))
print("谐声字卡总数(level3)","例子",bad[:10])
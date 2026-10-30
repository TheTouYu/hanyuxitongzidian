import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
r3=[];bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if d.get("level")==3 and d.get("rootLevel"): r3.append(d.get("char"))
for ch in ("髟","赦","家","㕞"):
    d=json.load(io.open(os.path.join(C,ch+".json"),encoding="utf-8"))
    print(ch,"lv",d.get("level"),"rootLevel",d.get("rootLevel"))
print("三级字根共",len(r3),r3[:20])
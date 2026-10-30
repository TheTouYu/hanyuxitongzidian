import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
noal=0; heads=0; bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    head=d.get("head") or ""
    if "（" in head: heads+=1
    if not (d.get("aliases") or []):
        noal+=1
        if "（" in head: bad.append(fn[:-5])
print("有括注head",heads,"无别名卡",noal,"其中头带括注",len(bad),bad[:10])
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
hit=[k for k,v in cm.items() if any("春園" in x for x in (v if isinstance(v,list) else [v]))]
print("cap",hit)
for k in hit: print(k, os.listdir(os.path.join(P,k)))
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
print("矢:",ph.get("矢"),"知:",ph.get("知"))
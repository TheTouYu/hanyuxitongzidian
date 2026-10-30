# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
pat=re.compile(r"^(本義|本义|轉義|转义|辯證|辩证|音源|字族衍義|字族衍义|释义|釋義)\s*[：:]\s*")
n=0; changed=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); n+=1; dirty=False
    for s in d.get("sections") or []:
        t=s.get("text") or ""
        t2=pat.sub("",t)
        if t2!=t:
            s["text"]=t2; dirty=True
    if dirty:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); changed+=1
print("扫",n,"改",changed)
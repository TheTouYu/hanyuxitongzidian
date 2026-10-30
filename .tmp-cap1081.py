# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(os.path.join(C,"㕞.json"),encoding="utf-8")); d["rootLevel"]=3
json.dump(d,io.open(os.path.join(C,"㕞.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("㕞 ->",d["rootLevel"])
for fn in os.listdir(C):
    if fn.endswith(".json") and fn!="index.json":
        p=os.path.join(C,fn)
        try: c=json.load(io.open(p,encoding="utf-8"))
        except: continue
        ch=c.get("char") or fn[:-5]
        if any("\ue000"<=x<="\uf8ff" for x in ch) and "rootLevel" in c:
            c.pop("rootLevel"); json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("清私用区",repr(ch))
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
p=os.path.join(C,"兮.json"); d=json.load(io.open(p,encoding="utf-8"))
def files(ch): return sorted(os.listdir(os.path.join(G,ch)))
gi=[f"𠣬/{f}" for f in files("𠣬")]+[f"幵/{f}" for f in files("幵")]
for s in d["sections"]:
    if s.get("key")=="bianzheng": s["gimgs"]=gi
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(gi)
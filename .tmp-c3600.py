import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\曳.json"; d=json.load(io.open(p,encoding="utf-8")); n=0
for s in d["sections"]:
    for g in s.get("groups",[]) or []:
        for r in g.get("rows",[]) or []:
            if isinstance(r,list) and len(r)>=3 and r[0]=="䒶":
                r[2]=""; n+=1
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("改",n)
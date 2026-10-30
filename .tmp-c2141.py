import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\睪.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            if "形近字" in (g.get("title") or ""):
                g["rows"]=[]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("④组已清空（原文未列字）")
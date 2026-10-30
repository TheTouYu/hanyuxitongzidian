import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
bad=0; samples={}
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    for s in d.get("sections") or []:
        t=s.get("text") or ""
        if "拟态义一面" in t or "取一面：" in t: bad+=1; break
for ch in ("技","妓","䰙","枝","翄"):
    d=json.load(io.open(os.path.join(C,ch+".json"),encoding="utf-8"))
    print(ch, [s["text"] for s in d["sections"] if s["key"]=="shengmu"])
print("剩余占位",bad)
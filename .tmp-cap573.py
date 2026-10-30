import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if d.get("parent")!="斦": continue
    t=next((s["text"] for s in d["sections"] if s["key"]=="shiyi"),"")
    ok=t.startswith(d["char"])
    print("OK " if ok else "BAD",d["char"],"|",t[:24])
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-charmap.json"
if os.path.exists(p):
    m=json.load(io.open(p,encoding="utf-8"))
    print(type(m), len(m))
    k=list(m)[:3]; print([(x,m[x]) for x in k])
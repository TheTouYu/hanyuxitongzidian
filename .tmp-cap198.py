import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-charmap.json"
print("exists",os.path.exists(p))
if os.path.exists(p):
    m=json.load(io.open(p,encoding="utf-8"))
    print("keys",len(m))
    for ch in ("咺","㿩","䬞","伳","㞷","㠱"):
        v=m.get(ch)
        print(ch, (v.get("部名") if isinstance(v,dict) else v))
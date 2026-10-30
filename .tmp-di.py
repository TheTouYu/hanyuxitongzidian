import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\弟.json",encoding="utf-8"))
print("bus=",d.get("bus"),"keys=",list(d.keys()))
z=[x for x in d["sections"] if x.get("key")=="zizu"][0]
print(json.dumps(z,ensure_ascii=False)[:300])
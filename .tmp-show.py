import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(open(r"D:\系统汉字\web\public\cards\只.json",encoding="utf-8"))
print(json.dumps(d,ensure_ascii=False,indent=1)[:2600])
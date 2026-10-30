import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
print(type(d),len(d))
it=list(d.items())[:2] if isinstance(d,dict) else d[:2]
print(json.dumps(it,ensure_ascii=False)[:300])
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\帝.json",encoding="utf-8"))
for s in d["sections"]:
    if "二级" in (s.get("label") or "") or s.get("key")=="erji":
        print(json.dumps(s,ensure_ascii=False)[:500])
print("links",d.get("links"))
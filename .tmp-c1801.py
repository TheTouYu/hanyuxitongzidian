import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\ㄗ.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="erji":
        s["links"]=[{"ch":"卽","label":"卽"},{"ch":"肥","label":"肥"},{"ch":"配","label":"配"},{"ch":"邑","label":"邑"}]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ㄗ 二级链接补 配/邑")
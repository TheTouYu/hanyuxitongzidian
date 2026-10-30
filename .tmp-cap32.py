import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
a=json.load(io.open(rf"{C}\𧧘.json",encoding="utf-8"))
b=json.load(io.open(rf"{C}\栬.json",encoding="utf-8"))
print("diff keys",set(a)^set(b))
for k in a:
    if k=="sections": continue
    if a[k]!=b.get(k): print("diff",k,repr(a[k])[:60],"|",repr(b.get(k))[:60])
print("A secs",a["sections"]); print("B secs",b["sections"])
import sys,json,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
m=json.load(open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
print("charmap申:",m.get("申"))
t=open(r"D:\系统汉字\knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
for line in t.splitlines():
    if "申" in line: print("目录:",line[:120])
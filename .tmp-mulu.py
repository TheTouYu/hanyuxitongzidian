import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open(r"D:\系统汉字\knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
for m in re.finditer(r"^### (.+)$",t,re.M):
    s=m.group(1)
    if "第" in s and ("章" in s or "卷" in s): print(s)
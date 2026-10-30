import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
for m in re.finditer(r".{60}d\.head.{80}",h,re.S):
    print(repr(m.group(0)));print("---")
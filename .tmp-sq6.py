import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\index.html", r"D:\系统汉字\web\public\test.html"):
    t=io.open(f,encoding="utf-8").read()
    print("==",f.split("\\")[-1])
    for m in re.finditer(r"cards/index\.json[^'\"\)]*",t): print("  ",m.group(0))
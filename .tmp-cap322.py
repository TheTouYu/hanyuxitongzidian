import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
for m in re.finditer(r"esc\(s\.text\)",h):
    print(m.start(), h[max(0,m.start()-160):m.start()+80].replace("\n"," "))
    print("---")
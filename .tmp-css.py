import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
for m in re.finditer(r"\.([a-z-]*t(itle)?|h2)[^{]*\{[^}]*font-size[^}]*\}",h):
    print(m.group(0)[:120].replace("\n"," "))
print("---")
for m in re.finditer(r"font-size:\s*(\d+)px",h):
    pass
i=h.find("function open(")
print(h[i:i+260].replace("\n"," "))
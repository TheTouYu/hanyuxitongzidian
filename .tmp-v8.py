import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
print("zx count",h.count("${zx}"))
print("LKR uses",h.count("LKR(s)"))
i=h.find("${zx}")
print(h[i-160:i+40].replace("\n"," "))
j=h.find("${zx}${LKR(s)}")
print("inject at",j)
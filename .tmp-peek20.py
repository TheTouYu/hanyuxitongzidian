import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("const parentBlock")
print(h[i:i+520].replace("\n"," "))
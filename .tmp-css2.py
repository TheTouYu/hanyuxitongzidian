import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("b.num===0?")
print(h[i-420:i].replace("\n"," "))
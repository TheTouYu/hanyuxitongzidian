import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
print("smalt css:", ".smalt" in h)
i=h.find(".smalt"); print(h[i-60:i+120] if i>0 else "none")
print("sm( used:", h.count("sm("))
j=h.find("${sm("); print(h[j-80:j+80] if j>0 else "no sm call")
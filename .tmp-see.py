import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
s=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=s.find("function render")
print(s[i-200:i+900])
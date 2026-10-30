import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("const secHTML")
seg=h[i:i+1400]
print(seg[380:1200])
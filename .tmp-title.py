import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
s=s.replace("<title>查字测试台 · 系统汉语</title>","<title>系统汉语字典</title>",1)
s=s.replace("<h1>查字测试台 · 系统汉语</h1>","<h1>系统汉语字典</h1>",1)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("title:", "系统汉语字典" in s)
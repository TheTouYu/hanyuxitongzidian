import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
n=s.count("return in.innerHTML=`")
s=s.replace("return in.innerHTML=`","return `")
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("fixed",n)
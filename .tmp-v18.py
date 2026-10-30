import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
b=re.findall(r"<script[^>]*>(.*?)</script>",h,re.S)
for k,x in enumerate(b): io.open(rf"D:\系统汉字\.tmp-d{k}.js","w",encoding="utf-8").write(x)
print("ch in list:", "x.ch?('第'" in h or "x.ch" in h, "| header:", "d.chapter" in h)
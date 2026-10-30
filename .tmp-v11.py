import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find("const LKR="); print(h[i:i+170])
print("goCard assign", "window.goCard=open" in h)
b=re.findall(r"<script[^>]*>(.*?)</script>",h,re.S)
for k,x in enumerate(b): io.open(rf"D:\系统汉字\.tmp-c{k}.js","w",encoding="utf-8").write(x)
print("blocks",len(b))
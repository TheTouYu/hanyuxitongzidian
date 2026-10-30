import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
s=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
m=re.findall(r"<script>([\s\S]*?)</script>",s)
io.open(r"D:\系统汉字\.tmp-check.js","w",encoding="utf-8",newline="\n").write("\n".join(m))
print("scripts",len(m))
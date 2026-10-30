import sys,io,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
js=re.search(r"<script>([\s\S]*)</script>",t).group(1)
ls=js.splitlines()
for i in range(40,56): print(i,"|",ls[i][:260])
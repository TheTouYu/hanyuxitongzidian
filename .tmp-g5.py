import sys,io,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
t=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
js=re.search(r"<script>([\s\S]*)</script>",t).group(1)
for i,l in enumerate(js.splitlines()):
    if any(k in l for k in ["hasZX","strip","zx=","古文字字形"]): print(i,"|",l[:180])
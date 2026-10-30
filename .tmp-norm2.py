import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
s=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
for m in re.finditer(r"(const|function)\s+norm[^\n]*",s): print(m.group(0)[:200])
i=s.find("function match"); print("---"); print(s[i:i+320])
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\inline-glyphs.py"
t=io.open(p,encoding="utf-8").read()
t=t.replace("if not (1200 <= len(b) < 20000): continue","if not (80 <= len(b) < 20000): continue")
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("threshold 80")
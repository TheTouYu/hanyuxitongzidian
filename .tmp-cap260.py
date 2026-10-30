import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\inline-inline.py"
t=io.open(p,encoding="utf-8").read()
t=t.replace('out.append("{{%02d}}"%k)','out.append("{{%02d%s}}"%(k,ext))')
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("token with ext")
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
old="${d.noRoot?'':parentBlock}"
new="${(d.noRoot||(d.sections||[]).some(x=>String(x.label||'').startsWith('字根「')))?'':parentBlock}"
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("ok")
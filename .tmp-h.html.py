import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
old="return `<div class=\"sec\"><h3>${esc(s.label||s.key)}</h3>"
new="return (s.html?`<div class=\"sec rootbox\"><h3>${esc(s.label||s.key)}</h3>${s.html}</div>`:null)||`<div class=\"sec\"><h3>${esc(s.label||s.key)}</h3>"
assert old in t, "pattern not found"
t=t.replace(old,new,1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("client ok")
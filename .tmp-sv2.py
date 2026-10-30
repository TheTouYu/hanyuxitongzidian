import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
t=t.replace("const _hasZigen=(d.sections||[]).some(x=>x.key==='zigen'||String(x.label||'').startsWith('字根「'));",
            "const _hasZigen=(d.sections||[]).some(x=>['zigen','rootembed'].includes(x.key)||String(x.label||'').startsWith('字根「'));")
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("server ok")
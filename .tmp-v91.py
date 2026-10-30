import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=0
    a='<h4>${esc(g.title)}</h4>'
    b='${g.title?\'<h4>\'+esc(g.title)+\'</h4>\':\'\'}'
    if a in h: h=h.replace(a,b); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="(g.header||['字','读音','类属','取义落点'])"
new="(g.header||((g.rows&&g.rows[0]&&String(g.rows[0][0]).slice(-1)==='部')?['部目','字根','中心义','字族']:['字','读音','类属','取义落点']))"
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=h.count(old)
    h=h.replace(old,new); io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    print(f.split("\\")[-1],"repl",n)
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const chain=[];let p=t.pr;let guard=0;",
                "const chain=[];let p=(t.lv>1&&t.pr)?t.pr:t.n;let guard=0;")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"patched")
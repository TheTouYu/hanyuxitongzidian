import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const rl=chain.length?chain.slice().reverse().map(ln).join(' → '):'—';",
                "const rl=chain.length?chain.map(ln).join(' → '):'—';")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"patched")
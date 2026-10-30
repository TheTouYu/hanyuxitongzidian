import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const rootLink = (d.level===2 && d.parent) ?",
                "const rootLink = (d.level===2 && d.parent && !(opt&&opt.embed)) ?")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
print("done")
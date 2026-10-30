import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="${grp(s)}${tbl(s)}<p>${esc(s.text)}</p>${zx}"
new="${grp(s)}${tbl(s)}<p>${esc(s.text)}</p>${zx}${LKR(s)}"
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched body",f)
    else:
        print("pattern not found",f)
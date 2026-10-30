import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(p,encoding="utf-8").read()
    if "s.gimgs" in h: print(p.split("\\")[-1],"already"); continue
    old="${zx}${LKR(s)}"
    new="${zx}${(s.gimgs||[]).map(f=>`<img class=\"gin\" src=\"glyphs/${f}\">`).join('')}${LKR(s)}"
    if old in h:
        h=h.replace(old,new,1)
        if ".gin{" not in h: h=h.replace("</style>",".gin{height:1.6em;vertical-align:-0.4em;margin:0 3px;border:1px solid #eee}</style>",1)
        io.open(p,"w",encoding="utf-8",newline="\n").write(h); print(p.split("\\")[-1],"patched")
    else: print(p.split("\\")[-1],"MISS")
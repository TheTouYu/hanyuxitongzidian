import io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const p=await pr.json(); if(p&&p.sections)p.sections=p.sections.filter(s=>s.label!=='所属卷');",
                "const p=await pr.json(); if(p&&p.sections){p.sections=p.sections.filter(s=>s.label!=='所属卷');p.level=3;}")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
print("ok")
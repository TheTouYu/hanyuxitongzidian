import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const p=await pr.json();"
new="const p=await pr.json(); if(p&&p.sections)p.sections=p.sections.filter(s=>s.label!=='所属卷');"
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=h.count(old); h=h.replace(old,new)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)
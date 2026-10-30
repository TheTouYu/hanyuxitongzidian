import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=0
    a="const secs=(d.sections||[]).filter(s=>!isZX(s))"
    b="const ss=(d.sections||[]).find(s=>s.label==='所属卷'); const secs=(d.sections||[]).filter(s=>!isZX(s)&&s.label!=='所属卷')"
    if a in h: h=h.replace(a,b,1); n+=1
    c="${rootLink}${parentBlock}"
    d=("${rootLink}${parentBlock}${ss?'<div class=\"sec\"><h3>所属卷</h3>'+LKR(ss)+'</div>':''}")
    if c in h: h=h.replace(c,d,1); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)
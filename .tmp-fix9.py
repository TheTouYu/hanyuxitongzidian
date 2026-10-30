import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
t=t.replace("const secs=(d.sections||[]).map(s=>{ if(isZX(s)) hasZX=true;","const secs=(d.sections||[]).filter(s=>!isZX(s)).map(s=>{ if(isZX(s)) hasZX=true;",1)
t=t.replace("const zx=(isZX(s)&&!s.__s)?strip:''; if(zx) s.__s=1;","const zx='';",1)
t=t.replace("<div class=\"bu\">${lvlTag}第${esc(String(b.num||'?'))}部 ${esc(b.name||'')}</div></div>${secs}","<div class=\"bu\">${lvlTag}第${esc(String(b.num||'?'))}部 ${esc(b.name||'')}</div></div>${strip}${secs}",1)
io.open(p,"w",encoding="utf-8").write(t)
print("ok", t.count("${strip}${secs}"))
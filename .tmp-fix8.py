import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
t=t.replace("let hasZX=false;","let hasZX=false;const isZX=s=>s.key==='zigen'||s.key==='zixing'||/字形/.test(s.label||'');",1)
t=t.replace("if(s.key==='zixing'||/古文字字形/.test(s.label||'')) hasZX=true;","if(isZX(s)) hasZX=true;",1)
t=t.replace("const zx=(s.key==='zixing'||/古文字字形/.test(s.label||''))?strip:'';","const zx=(isZX(s)&&!s.__s)?strip:''; if(zx) s.__s=1;",1)
io.open(p,"w",encoding="utf-8").write(t)
print("patched")
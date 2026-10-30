import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
# 索引 pr 恢复为 parent（二级字根也要显示上级）
p=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace('"pr":(d.get("char") if d.get("level")==2 else d.get("parent",""))','"pr":d.get("parent","")',1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
# 页面：二级字根链条＝上级→自身
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    old="const chain=[];let p=(t.rc&&t.rc.length)?t.rc[t.rc.length-1]:((t.lv===2)?t.pr:((t.lv>2&&t.pr)?t.pr:t.n));let guard=0;"
    new="const chain=[];let p=(t.rc&&t.rc.length)?t.rc[t.rc.length-1]:((t.lv>=2&&t.pr)?t.pr:t.n);let guard=0;"
    h=h.replace(old,new)
    old2="if(t.rc&&t.rc.length)chain.length=0,(t.rc).forEach(x=>chain.push(x));"
    new2="if(t.rc&&t.rc.length)chain.length=0,(t.rc).forEach(x=>chain.push(x));else if(t.lv===2)chain.push(t.c);"
    h=h.replace(old2,new2)
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    tt=os.path.join(tempfile.gettempdir(),"chk30.js"); io.open(tt,"w",encoding="utf-8").write(js)
    print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",tt],capture_output=True,text=True).returncode)
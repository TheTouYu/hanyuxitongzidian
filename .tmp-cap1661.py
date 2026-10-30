import io,re,sys,tempfile,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
n=0
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("esc(d.head||d.cname||ch)","esc2(d.head||d.cname||ch)")
    if h!=o:
        n+=h.count("esc2(d.head")
        io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk26.js"); io.open(t,"w",encoding="utf-8").write(js)
    print(os.path.basename(f),"rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
print("replaced",n)
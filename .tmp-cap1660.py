import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("${esc(d.head||d.cname||ch)}","${esc2(d.head||d.cname||ch)}")
    h=h.replace("${esc(d.head||ch)}","${esc2(d.head||ch)}")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    import tempfile,subprocess,os
    t=os.path.join(tempfile.gettempdir(),"chk25.js"); io.open(t,"w",encoding="utf-8").write(js)
    print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
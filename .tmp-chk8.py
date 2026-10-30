import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    m=re.findall(r"<script>(.*?)</script>",h,re.S)
    js="\n;\n".join(m)
    p=os.path.join(tempfile.gettempdir(),"chk.js"); io.open(p,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
    print(f.split("\\")[-1],"rc",r.returncode,(r.stderr or "")[:120])
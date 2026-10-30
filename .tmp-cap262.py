import io,re,sys,subprocess,os,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
node=r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe"
for p in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(p,encoding="utf-8").read()
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk40.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([node,"--check",t],capture_output=True,text=True)
    print(os.path.basename(p),"rc",r.returncode, (r.stderr or "")[:80])
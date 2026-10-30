import io,sys,re,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    t=io.open(f,encoding="utf-8").read(); o=t
    t=t.replace("const al=(it&&it.a&&it.a.length)?('（'+it.a.join('/')+'）'):'';",
                "const as=(it&&it.a||[]).filter(x=>x!==(it?it.c:ch));const al=as.length?('（'+as.join('/')+'）'):'';")
    t=t.replace("names.map(famln).join('')","names.map(famln).join('')")
    if t!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(t); print(os.path.basename(f),"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",t,re.S))
    p=os.path.join(tempfile.gettempdir(),"chk.json.check.js"); io.open(p,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
    print("rc",r.returncode, r.stderr[:80])
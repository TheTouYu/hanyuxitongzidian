import io,sys,re,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read(); o=h
print("head uses:", h.count("d.head"))
h=h.replace("esc(d.head||d.cname||ch)","sm(d.head||d.cname||ch)")
h=h.replace("esc(x.head||x.cname||x.c)","sm(x.head||x.cname||x.c)")
if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk70.js"); io.open(t,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
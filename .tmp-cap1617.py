import io,re,sys,tempfile,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk22.js"); io.open(t,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
print("rc",r.returncode)
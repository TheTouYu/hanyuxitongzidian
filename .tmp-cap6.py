import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read()
h=h.replace("fetch('glyphs/photos/captions.json')","fetch('glyphs/photos/captions.json?v='+Date.now())",1)
io.open(f,"w",encoding="utf-8",newline="\n").write(h)
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
p=os.path.join(tempfile.gettempdir(),"chk14.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("rc",r.returncode)
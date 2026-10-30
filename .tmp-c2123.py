import io,sys,re,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read(); o=h
h=h.replace(".chead .ch .smalt{font-size:.55em;color:#7a6a55;letter-spacing:0}",
            ".smalt{font-size:.55em;color:#7a6a55;letter-spacing:0;font-weight:400}")
if h==o:
    h=h.replace("</style>",".smalt{font-size:.55em;color:#7a6a55;letter-spacing:0;font-weight:400}\n</style>",1)
io.open(f,"w",encoding="utf-8",newline="\n").write(h)
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk71.js"); io.open(t,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
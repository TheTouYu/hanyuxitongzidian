import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"
h=io.open(f,encoding="utf-8").read(); o=h
h=h.replace("const GGRP=s=>{if(!s.groups||!s.groups.length)return '';return s.groups.map",
            "const GGRP=s=>{if(!s.groups||!s.groups.length)return '';return (s.text?'<p class=\"gnote\">'+esc(s.text)+'</p>':'')+s.groups.map",1)
h=h.replace("const TTBL=s=>{", "const TTBL=s=>{",1)
if h!=o:
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("GGRP patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk50.js"); io.open(t,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
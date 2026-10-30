import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"
h=io.open(f,encoding="utf-8").read(); o=h
if "function sm(" not in h:
    h=h.replace("const GGRP=", "function sm(s){return esc2(s).replace(/（[^）]{1,12}）/g,m=>'<span class=\"smalt\">'+m+'</span>');}\nconst GGRP=",1)
h=h.replace(".chead .ch{font-size:26px;line-height:1}", ".chead .ch{font-size:26px;line-height:1}.chead .ch .smalt{font-size:.55em;color:#7a6a55;letter-spacing:0}",1)
h=h.replace("esc2(d.head||d.cname||ch)","sm(d.head||d.cname||ch)")
if h!=o:
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk44.js"); io.open(t,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
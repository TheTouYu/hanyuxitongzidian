# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
snippet="<script>document.addEventListener('error',function(e){var t=e.target;if(!t||t.tagName!=='IMG')return;var f=t.closest('figure');if(f){f.parentNode.removeChild(f);}else{t.style.display='none';}},true);</script>"
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if "tagName!=='IMG'" in h: print(os.path.basename(f),"已有"); continue
    h=h.replace("</body>",snippet+"\n</body>",1) if "</body>" in h else h+snippet
    io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk_err.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print(os.path.basename(f),"patched rc",r.returncode)
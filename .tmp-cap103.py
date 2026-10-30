# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="${s.text?('<p style=\"text-indent:2em\">'+esc(s.text)"
new="${(s.groups&&s.groups.length)?'':(s.text?('<p style=\"text-indent:2em\">'+esc(s.text)"
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1)
        # close paren: pattern ends with `</p>`):''}${zx}` -> need extra )
        h=h.replace("+'</p>'):''}${zx}","+'</p>'):'')}${zx}",1)
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk30.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print("rc",r.returncode, (r.stderr or "")[:200])
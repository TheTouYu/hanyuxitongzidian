import io,re,sys,tempfile,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old='<img class="cim" src="glyphs/chars/\'+h+\'.png">'
new='<img class="cim" data-t="&#x\'+h+\';" src="glyphs/chars/\'+h+\'.png" onerror="this.replaceWith(document.createTextNode(this.dataset.t))">'
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new)
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    else: print("MISS",os.path.basename(f))
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk27.js"); io.open(t,"w",encoding="utf-8").write(js)
    print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
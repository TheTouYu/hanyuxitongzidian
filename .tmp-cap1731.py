import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old=":(chain.length?chain.slice().reverse().map(ln).join(' → '):'—'));"
new=":(chain.length?((t.lv===2?chain:chain.slice().reverse()).map(ln).join(' → ')):'—'));"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    tt=os.path.join(tempfile.gettempdir(),"chk32.js"); io.open(tt,"w",encoding="utf-8").write(js)
    print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",tt],capture_output=True,text=True).returncode)
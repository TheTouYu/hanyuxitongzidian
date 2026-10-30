import io,re,sys,subprocess,os,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const lvlTag = d.level?`<span class=\"tag\">${d.level===1?'一級字根':d.level===2?'二級字根':'谐声字'}</span>`:'';"
new="const lvlTag = d.level?`<span class=\"tag\">${d.rootLevel?({1:'一級字根',2:'二級字根',3:'三級字根'}[d.rootLevel]||'字根'):(d.level===1?'一級字根':d.level===2?'二級字根':'谐声字')}</span>`:'';"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"tag patched")
    elif "rootLevel" in h: print(f.split("\\")[-1],"already")
    else: print(f.split("\\")[-1],"MISS")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk40.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print(" rc",r.returncode)
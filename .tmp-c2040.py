import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read(); o=h
h=h.replace("${GGRP(s)}${TTBL(s)}", "${(()=>{try{return GGRP(s)+TTBL(s)}catch(e){return '<p class=\"err\">表格渲染失败：'+esc(String(e))+'</p>'}})()}",1)
if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=os.path.join(tempfile.gettempdir(),"chk60.js"); io.open(t,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
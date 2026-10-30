import io,re,sys,os,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"
h=io.open(f,encoding="utf-8").read(); o=h
# 1) 别名括注用小号
h=h.replace(".chead .ch{font-size:26px;line-height:1}",".chead .ch{font-size:26px;line-height:1}.chead .ch .alt{font-size:.55em;color:#7a6a55}")
# 2) 渲染卡头时把「（…）」包成 .alt
h=h.replace("esc(d.head||d.cname||ch)","(()=>{const s=d.head||d.cname||ch;const i=s.indexOf('（');return i<0?esc2(s):esc2(s.slice(0,i))+'<span class=\"alt\">'+esc2(s.slice(i))+'</span>';})()")
if h!=o:
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched")
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
tt=os.path.join(tempfile.gettempdir(),"chk41.js"); io.open(tt,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",tt],capture_output=True,text=True).returncode)
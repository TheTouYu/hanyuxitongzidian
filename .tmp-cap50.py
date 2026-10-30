# -*- coding: utf-8 -*-
import io,re,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); o=h
    # photoBlock: drop fallback, keep only own photos
    h=re.sub(r"const photoBlock=\(\(\)=>\{.*?\}\)\(\);",
             "const photoBlock=(()=>{if(!window.PHOTO)return '';const own=window.PHOTO[d.char]||[];if(!own.length)return '';return '<div class=\"sec\"><h3>插图</h3><div class=\"pscroll\">'+own.map((f,i)=>'<figure><img loading=\"lazy\" src=\"'+encodeURI('glyphs/photos/'+d.char+'/'+f)+'\"><figcaption>'+(i+1)+'</figcaption></figure>').join('')+'</div></div>';})();",
             h,flags=re.S)
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(os.path.basename(f),"patched")
    js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
    t=os.path.join(tempfile.gettempdir(),"chk21.js"); io.open(t,"w",encoding="utf-8").write(js)
    r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True)
    print("rc",r.returncode)
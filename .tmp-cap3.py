# -*- coding: utf-8 -*-
import io,re,sys,subprocess,tempfile,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
f=r"D:\系统汉字\web\public\test.html"; h=io.open(f,encoding="utf-8").read()
old="P.map(f=>'<figure><img loading=\"lazy\" src=\"glyphs/photos/'+encodeURIComponent(who)+'/'+encodeURIComponent(f)+'\" alt=\"'+esc(ch)+'\"><figcaption>'+esc(f.replace(/\\.[a-z]+$/i,''))+'</figcaption></figure>').join('')"
new="P.map((f,i)=>{const CP=(window.CAPS||{})[who]||[];const cap=CP[i]||'';return '<figure><img loading=\"lazy\" src=\"glyphs/photos/'+encodeURIComponent(who)+'/'+encodeURIComponent(f)+'\" alt=\"'+esc(ch)+'\">'+(cap?'<figcaption>'+esc(cap)+'</figcaption>':'')+'</figure>';}).join('')"
assert old in h, "anchor miss"
h=h.replace(old,new,1)
old2="fetch('glyphs/photos/index.json').then(r=>r.json()).then(d=>{window.PHOTO=d.photos||d;}).catch(()=>{});"
new2=old2+" fetch('glyphs/photos/captions.json').then(r=>r.json()).then(d=>{window.CAPS=d;}).catch(()=>{});"
if old2 in h and "captions.json" not in h:
    h=h.replace(old2,new2,1)
io.open(f,"w",encoding="utf-8",newline="\n").write(h)
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
p=os.path.join(tempfile.gettempdir(),"chk13.js"); io.open(p,"w",encoding="utf-8").write(js)
r=subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",p],capture_output=True,text=True)
print("rc",r.returncode,(r.stderr or "")[:150],"cap",("captions.json" in h))
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("esc(s.text)","esc(s.text).replace(/&lt;img class=&quot;gin&quot; src=&quot;([^&]*)&quot; alt=&quot;字形&quot;&gt;/g,'<img class=\"gin\" src=\"$1\" alt=\"字形\">')")
    if h!=o:
        io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"patched")
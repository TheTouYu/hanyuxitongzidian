import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    old="fetch('glyphs/photos/index.json')"
    new="fetch('glyphs/photos/index.json?v='+Date.now())"
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched",f.split(chr(92))[-1])
    else: print("miss",f.split(chr(92))[-1])
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
old='src="glyphs/${encodeURIComponent(ch)}/${encodeURIComponent(f)}"'
new='src="glyphs/${encodeURIComponent(String(f).startsWith(ch+\'/\')?f:ch+\'/\'+f)}"'
if old in t:
    t=t.replace(old,new,1); io.open(p,"w",encoding="utf-8").write(t); print("patched")
else:
    print("pattern not found")
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
b=open(p,"rb").read()
t=b.decode("utf-8-sig")
old="}catch(e){ return ''; } })() : '';"
new="}catch(e){ return '<div class=\"sec rootbox\"><h3>字根「'+esc(d.parent)+'」</h3><p style=\"color:#c00\">ERR '+esc(String(e&&e.stack||e))+'</p></div>'; } })() : '';"
assert old in t, "catch pattern not found"
open(p,"wb").write(t.replace(old,new,1).encode("utf-8"))
print("patched ok")
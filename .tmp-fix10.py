import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
old="fetch('cards/'+encodeURIComponent(ch)+'.json')"
new="fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now())"
if old in t:
    t=t.replace(old,new,1); print("patched card fetch")
old2="fetch('cards/index.json')"
if old2 in t:
    t=t.replace(old2,"fetch('cards/index.json?v='+Date.now())",1); print("patched index fetch")
old3="fetch('cards/'+encodeURIComponent(d.parent)+'.json')"
if old3 in t:
    t=t.replace(old3,"fetch('cards/'+encodeURIComponent(d.parent)+'.json?v='+Date.now())",1); print("patched parent fetch")
io.open(p,"w",encoding="utf-8").write(t)
# server: no-store for /cards/*.json
s=r"D:\系统汉字\web\server.mjs"; st=io.open(s,encoding="utf-8").read()
if "pathname.startsWith('/cards/')" not in st:
    m=re.search(r"['\"]cache-control['\"]:\s*['\"]no-cache['\"]",st)
    print("header spot", bool(m))
io.open(s,"w",encoding="utf-8").write(st)
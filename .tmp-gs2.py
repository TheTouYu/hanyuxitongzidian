import sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
old=".gscroll img{height:96px;display:block;background:#fff;border:1px solid var(--line);border-radius:6px;padding:2px}"
new=old+"\n.gscroll figure{margin:0;text-align:center;flex:0 0 auto}\n.gscroll figcaption{font-size:11px;color:var(--mut);margin-top:2px;letter-spacing:.5px}"
assert old in t; t=t.replace(old,new,1)
o="""`<div class="gscroll">${g.map(f=>`<img loading="lazy" src="glyphs/${encodeURIComponent(ch)}/${encodeURIComponent(f)}" alt="${esc(ch)}" title="${esc(f)}">`).join('')}</div>`"""
n="""`<div class="gscroll">${g.map((f,i)=>`<figure><img loading="lazy" src="glyphs/${encodeURIComponent(ch)}/${encodeURIComponent(f)}" alt="${esc(ch)}" title="${esc(f)}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`"""
assert o in t; t=t.replace(o,n,1)
io.open(p,"w",encoding="utf-8").write(t)
print("ok")
import sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
css_old=".glyphs img{height:78px;display:block}"
css_new=css_old+"\n.gscroll{display:flex;gap:8px;overflow-x:auto;padding:6px 0;scroll-behavior:smooth}\n.gscroll img{height:96px;display:block;background:#fff;border:1px solid var(--line);border-radius:6px;padding:2px}"
assert css_old in t; t=t.replace(css_old,css_new,1)
old100="""  const glyph=g.length?`<div class="glyphs">${g.map(f=>`<figure><img loading="lazy" src="glyphs/${encodeURIComponent(ch)}/${encodeURIComponent(f)}" alt="${esc(ch)}"></figure>`).join('')}</div>`:'<p class="m" style="color:var(--mut)">（字形库未收本字古文字形）</p>';"""
new100="""  const strip=g.length?`<div class="gscroll">${g.map(f=>`<img loading="lazy" src="glyphs/${encodeURIComponent(ch)}/${encodeURIComponent(f)}" alt="${esc(ch)}" title="${esc(f)}">`).join('')}</div>`:'<p class="m" style="color:var(--mut)">（字形库未收本字古文字形）</p>';"""
assert old100 in t; t=t.replace(old100,new100,1)
old99="""const secs=(d.sections||[]).map(s=>`<div class="sec"><h3>${esc(s.label||s.key)}</h3>${grp(s)}${tbl(s)}<p>${esc(s.text)}</p>${(s.cites&&s.cites.length)?`<div class="cites">${s.cites.map(c=>`<span class="tag">${esc(c)}</span>`).join('')}</div>`:''}</div>`).join('');"""
new99="""let hasZX=false;
const secs=(d.sections||[]).map(s=>{ if(s.key==='zixing'||/古文字字形/.test(s.label||'')) hasZX=true;
  const zx=(s.key==='zixing'||/古文字字形/.test(s.label||''))?strip:'';
  return `<div class="sec"><h3>${esc(s.label||s.key)}</h3>${grp(s)}${tbl(s)}<p>${esc(s.text)}</p>${zx}${(s.cites&&s.cites.length)?`<div class="cites">${s.cites.map(c=>`<span class="tag">${esc(c)}</span>`).join('')}</div>`:''}</div>`;}).join('');"""
assert old99 in t; t=t.replace(old99,new99,1)
old110="${secs}${parentBlock}<div class=\"sec\"><h3>古文字字形</h3>${glyph}</div></div>`;"
new110="${secs}${parentBlock}${hasZX?'':'<div class=\"sec\"><h3>古文字字形</h3>'+strip+'</div>'}</div>`;"
assert old110 in t; t=t.replace(old110,new110,1)
io.open(p,"w",encoding="utf-8").write(t)
print("patched")
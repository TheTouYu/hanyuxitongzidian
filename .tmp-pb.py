import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
old="""      const inner=(p.sections||[]).map(s=>secHTML(s,d.parent)).join('');"""
new="""      const pg=((GLYPH[d.parent]&&GLYPH[d.parent].files)||[]);
      const pgsrc=f=>encodeURI('glyphs/'+d.parent+'/'+(String(f).startsWith(d.parent+'/')?String(f).slice(d.parent.length+1):f));
      const pstrip=pg.length?`<div class="gscroll">${pg.map((f,i)=>`<figure><img loading="lazy" src="${pgsrc(f)}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:'';
      const pb=(p.bus||[])[0]||{};
      const inner=`<div class="ph"><span class="ch">${esc(p.char||d.parent)}</span><span class="py">${esc(p.pinyin||'')}</span><span class="bu">第${esc(String(pb.num||'?'))}部 ${esc(pb.name||'')}</span></div>${pstrip}`
        +(p.sections||[]).filter(x=>!(x.key==='zigen'||x.key==='zixing'||/字形/.test(x.label||'')))
           .map(x=>`<div class="sec"><h3>${esc(x.label||x.key)}</h3>${GGRP(x)}${TTBL(x)}<p>${esc(x.text)}</p></div>`).join('');"""
assert old in s
s=s.replace(old,new,1)
if ".ph{" not in s:
    s=s.replace("</style>",".ph{display:flex;gap:10px;align-items:baseline;margin:6px 0 10px}.ph .ch{font-size:40px;line-height:1}\n</style>",1)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("patched:", ".ph{" in s)
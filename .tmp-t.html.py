# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
start=t.index("const rootLink = (d.level===2")
end=t.index("const lvlTag =")
new = r'''const rootLink = '';
  let parentBlock='';
  if (d.level>2 && d.parent) {
    try{
      const pr=await fetch('cards/'+encodeURIComponent(d.parent)+'.json?v='+Date.now());
      if(pr.ok){
        const p=await pr.json();
        const keep=(p.sections||[]).filter(s=>['benyi','zhuanyi','bianzheng','yinyuan'].includes(s.key)&&s.text);
        const body=keep.map(s=>'<div class="sec"><h3>'+esc(s.label||s.key)+'</h3><p style="text-indent:2em">'+esc(s.text)+'</p></div>').join('');
        const pgs=((window.GLYPH&&GLYPH[d.parent]&&GLYPH[d.parent].files)||[]);
        const strip=pgs.length?('<div class="gscroll">'+pgs.map((f,i)=>'<figure><img loading="lazy" src="'+encodeURI('glyphs/'+d.parent+'/'+(String(f).startsWith(d.parent+'/')?String(f).slice(d.parent.length+1):f))+'"><figcaption>'+String(i+1).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'):'';
        const b2=(Array.isArray(p.bus)?p.bus[0]:(p.bus||{}))||{};
        parentBlock='<div class="sec rootbox"><h3>字根「'+esc(d.parent)+'」</h3><div class="chead"><div class="ch">'+esc(p.head||p.char||d.parent)+'</div><div class="py">'+esc(p.pinyin||'')+'</div><div class="bu">'+(p.level===1?'一級字根':p.level===2?'二級字根':'谐声字')+(b2.num?' · 第'+b2.num+'部 '+esc(b2.name||''):'')+'</div></div>'+strip+body+'</div>';
      } else { parentBlock='<div class="sec rootbox"><h3>字根「'+esc(d.parent)+'」</h3><p>父卡未找到：'+esc(d.parent)+'</p></div>'; }
    }catch(e){ parentBlock='<div class="sec rootbox"><h3>字根「'+esc(d.parent)+'」</h3><p>父卡读取失败：'+esc(String(e&&e.message||e))+'</p></div>'; }
  }

  '''
t=t[:start]+new+t[end:]
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched test.html")
# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="""  try { const gi=glyphInfo(d.char); if (gi && gi.files && gi.files.length){ h+='<div class="gs">'+gi.files.map((u,i)=>'<figure><img src="'+u+'?v='+Date.now()+'" alt="字形'+(i+1)+'"><figcaption>'+String(i+1).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'; } } catch(e){}"""
new=old+"""
  try { const gi2=glyphInfo(d.char); const ps=(gi2&&gi2.photos)||[]; if (ps.length){ h+='<h3>插图</h3><div class="gs">'+ps.map(p=>{const f=(typeof p==='string')?p:(p.file||p.name||'');const cap=(typeof p==='object'&&p.caption)?p.caption:'';return '<figure><img src="/glyphs/photos/'+encodeURIComponent(d.char)+'/'+encodeURIComponent(f)+'" alt="'+escH(cap||'插图')+'" style="height:170px"><figcaption>'+escH(cap||'')+'</figcaption></figure>';}).join('')+'</div>'; } } catch(e){}"""
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched")
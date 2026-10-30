# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="""  h+='<a class="back" href="/test.html">← 返回检索</a><h2>'+ext(d.head||d.char)+' <small>'+escH(d.pinyin||'')+'</small></h2>';"""
new="""  h+='<a class="back" href="/test.html">← 返回检索</a><h2>'+ext(d.head||d.char)+' <small>'+escH(d.pinyin||'')+'</small></h2>';
  try { const gi=glyphInfo(d.char); if (gi && gi.files && gi.files.length){ h+='<div class="gs">'+gi.files.map((u,i)=>'<figure><img src="'+u+'" alt="字形'+(i+1)+'"><figcaption>'+String(i+1).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'; } } catch(e){}"""
assert old in t
t=t.replace(old,new,1)
t=t.replace(".cim{height:1.12em;vertical-align:-0.2em}", ".cim{height:1.12em;vertical-align:-0.2em}.gs{display:flex;gap:10px;overflow-x:auto;padding:6px 0 10px}.gs figure{margin:0;text-align:center}.gs img{height:110px;border:1px solid #e7e0d2;border-radius:6px;background:#fff}.gs figcaption{font-size:11px;color:#999}",1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched glyph strip")
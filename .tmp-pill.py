# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
old = """  try { const b0=(d.bus&&d.bus[0])||null; if (b0){ h+='<p class="pill">'+(d.level===1?'一级字根':d.level===2?'二级字根':d.level===3?'谐声字':'')+' · 第'+(b0.num||'?')+'部「'+(b0.name||'')+'部」</p>'; } } catch(e){}"""
new = """  try { const b0=Array.isArray(d.bus)?d.bus[0]:(d.bus||null); const lv=d.level===1?'一级字根':d.level===2?'二级字根':d.level===3?'谐声字':''; let pill=lv; if(b0&&b0.num>0) pill+=' · 第'+b0.num+'部「'+(b0.name||'')+'部」'; else if(b0&&b0.name) pill+=' · 「'+b0.name+'部」'; if(pill) h+='<p class="pill">'+pill+'</p>'; } catch(e){}"""
assert old in t, "pattern not found"
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched pill")
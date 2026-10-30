# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
i=t.find("  let _b0=")
j=t.find("  try { const gi=", i)
assert i>0 and j>i
good = """  let _b0=Array.isArray(d.bus)?d.bus[0]:(d.bus||null);
  try { if(!_b0||!_b0.num){ let pr=d.parent, hop=0; while(pr&&hop<3){ const pf=join(CARDDIR,pr+'.json'); if(existsSync(pf)){ const pd=JSON.parse(readFileSync(pf,'utf8')); const pb=Array.isArray(pd.bus)?pd.bus[0]:pd.bus; if(pb&&pb.num){ _b0=pb; break; } pr=pd.parent; } else break; hop++; } } } catch(e){}
  try { const b0=_b0; const lv=d.level===1?'一级字根':d.level===2?'二级字根':d.level===3?'谐声字':''; let pill=lv; if(b0&&b0.num>0) pill+=' · 第'+b0.num+'部「'+(b0.name||'')+'部」'; else if(b0&&b0.name) pill+=' · 「'+b0.name+'部」'; if(pill) h+='<p class="pill">'+pill+'</p>'; } catch(e){}
"""
t=t[:i]+good+t[j:]
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("rebuilt pill block")
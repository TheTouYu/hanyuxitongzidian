# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
anchor="  try { const b0=Array.isArray(d.bus)?d.bus[0]:(d.bus||null);"
if anchor not in t: print("anchor missing"); sys.exit(1)
inject = """  let _b0=Array.isArray(d.bus)?d.bus[0]:(d.bus||null);
  try { if(!_b0||!_b0.num){ let pr=d.parent, hop=0; while(pr&&hop<3){ const pf=join(CARD_DIR,pr+'.json'); if(fs.existsSync(pf)){ const pd=JSON.parse(fs.readFileSync(pf,'utf8')); const pb=Array.isArray(pd.bus)?pd.bus[0]:pd.bus; if(pb&&pb.num){ _b0=pb; break; } pr=pd.parent; } else break; hop++; } } } catch(e){}
  const b0=_b0;"""
t=t.replace(anchor, inject, 1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("injected parent-walk pill")
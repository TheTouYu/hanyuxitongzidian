# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old_lines=[]
new_block='''      const kids=IDX.filter(x=>x.pr===t.c).map(x=>x.c);
      const ln=(ch)=>{const it=IDX.find(x=>x.c===ch||((x.a||[]).includes(ch)));const al=(it&&it.a&&it.a.length)?('（'+it.a.join('/')+'）'):'';const lab=(it?it.c:ch)+al;return `<a data-c="${esc(ch)}" style="color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer">${esc(lab)}</a>`;};
      const rl=chain.length?chain.slice().reverse().map(ln).join(' → '):'—';
      const fam=kids.length?`　<label>字族</label>　${kids.map(ln).join('')}`:'';
      rel=`<span style="margin-left:14px">字根　${rl}${fam}<span id="famspan"></span></span>`;
      window.fillFam(t.c);'''
fn='''window.fillFam=(ch)=>{fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now()).then(r=>r.json()).then(d=>{const seen=new Set(),names=[];(d.sections||[]).forEach(s=>(s.groups||[]).forEach(g=>(g.rows||[]).forEach(r=>{let c=String(r[0]||'').replace(/（.*?）|\\(.*?\\)/g,'').trim();if(c&&!seen.has(c)){seen.add(c);names.push(c);}})));const sp=document.getElementById('famspan');if(sp&&names.length){sp.innerHTML='　<label>字族</label>　'+names.map(famln).join('');bindHint();}}).catch(()=>{});};
const famln=(ch)=>{const it=IDX.find(x=>x.c===ch||((x.a||[]).includes(ch)));const al=(it&&it.a&&it.a.length)?('（'+it.a.join('/')+'）'):'';const lab=(it?it.c:ch)+al;return `<a data-c="${esc(ch)}" style="color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer">${esc(lab)}</a>`;};
window.bindHint=()=>{document.querySelectorAll('#hint a[data-c]').forEach(a=>a.onclick=()=>open(a.dataset.c));};'''
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    i=h.find("      const kids=IDX.filter"); j=h.find("      rel=`<span",i)
    k=h.find("</span>`;",j)+len("</span>`;")
    if i<0 or j<0 or k<0: print("MISS",f); continue
    h=h[:i]+new_block+h[k:]
    h=h.replace("document.querySelectorAll('#hint a[data-c]').forEach(a=>a.onclick=()=>open(a.dataset.c));","bindHint();",1)
    # insert helper definitions before function render(
    h=h.replace("function render(q){", fn+"\nfunction render(q){",1)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"patched")
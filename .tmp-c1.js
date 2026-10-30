
const $=s=>document.querySelector(s);
let IDX=[], GLYPH={}, cur='';
const norm=s=>(s||'').toLowerCase();
fetch('cards/index.json?v='+Date.now()).then(r=>r.json()).then(d=>{IDX=d;$('#hint').textContent=`共 ${d.length} 张卡`;render('');}).catch(e=>$('#hint').textContent='索引加载失败：'+e);
fetch('glyphs/index.json').then(r=>r.json()).then(d=>{GLYPH=d.chars||d;}).catch(()=>{});
fetch('glyphs/photos/index.json').then(r=>r.json()).then(d=>{window.PHOTO=d.photos||d;}).catch(()=>{});
function match(q){
  q=norm(q.trim()); if(!q) return IDX.slice(0,200);
  const exact=IDX.filter(x=>x.c===q||x.a===q);
  if(exact.length) return exact.concat(IDX.filter(x=>x.c!==q&&norm(x.a)!==q&&(norm(x.p).startsWith(q)||x.t.some(t=>norm(t).includes(q)))).slice(0,80));
  return IDX.filter(x=>norm(x.c).includes(q)||norm(x.a||'').includes(q)||norm(x.p).includes(q)||x.t.some(t=>norm(t).includes(q))).slice(0,120);
}
function render(q){
  const rows=match(q);
  $('#list').innerHTML=rows.map(x=>`<div class="item${x.c===cur?' on':''}" data-c="${x.c}"><b>${x.c}</b><span class="m">${x.p||''}</span><span class="m">第${x.b||'?'}部 ${x.n||''}</span></div>`).join('')||'<div class="empty">无结果</div>';
  const base=q?`命中 ${rows.length} 张`:`共 ${IDX.length} 张卡`;
  let rel='';
  if(q){
    const byChar=ch=>IDX.find(x=>x.c===ch||x.a===ch);
    let t=byChar(q)||rows.find(r=>r.lv>0)||rows[0];
    if(t){
      const chain=[];let p=t.pr;let guard=0;
      while(p&&guard++<5){chain.push(p);const pc=byChar(p);p=pc?pc.pr:'';}
      const kids=IDX.filter(x=>x.pr===t.c).map(x=>x.c);
      const sibs=t.pr?IDX.filter(x=>x.pr===t.pr&&x.c!==t.c).map(x=>x.c):[];
      const ln=(ch)=>{const it=IDX.find(x=>x.c===ch||x.a===ch);const lab=(it&&it.a)?(it.c+'（'+it.a+'）'):ch;return `<a data-c="${esc(ch)}" style="color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer">${esc(lab)}</a>`;};
      const rl=chain.length?chain.slice().reverse().map(ln).join(' → '):'—';
      const fam=kids.length?`　字族　${kids.map(ln).join('')}`:(sibs.length?`　同族（${t.pr}）　${sibs.map(ln).join('')}`:'');
      rel=`<span style="margin-left:14px">字根　${rl}`+fam+`</span>`;
    }
  }
  $('#hint').innerHTML=base+rel;
  document.querySelectorAll('#hint a[data-c]').forEach(a=>a.onclick=()=>open(a.dataset.c));
  $('#list').querySelectorAll('.item').forEach(el=>el.onclick=()=>open(el.dataset.c));
}
function esc(s){return (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
const GGRP=s=>{if(!s.groups||!s.groups.length)return '';return s.groups.map(g=>`<div class="grp"><h4>${esc(g.title)}</h4><p class="gnote">${esc(g.note||'')}</p><table class="ct"><thead><tr><th>字</th><th>读音</th><th>类属</th><th>取义落点</th></tr></thead><tbody>${g.rows.map(r=>`<tr><td class="zc">${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td>${esc(r[3])}</td></tr>`).join('')}</tbody></table></div>`).join('');};
const TTBL=s=>{if(!s.rows||s.rows.length<3)return '';const head='<tr><th>字</th><th>类属</th><th>取义落点</th></tr>';return `<table class="ct"><thead>${head}</thead><tbody>${s.rows.map(r=>`<tr><td class="zc">${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table>`;};
const secHTML=(s,ch2)=>{const g2=(GLYPH[ch2]&&(GLYPH[ch2].files||[]))||[];const st=g2.length?`<div class="gscroll">${g2.map((f,i)=>`<figure><img loading="lazy" src="${encodeURI('glyphs/'+ch2+'/'+(String(f).startsWith(ch2+'/')?String(f).slice(ch2.length+1):f))}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:'';const zx=(s.key==='zixing'||/字形|古文字/.test(s.label||''))?st:'';return `<div class="sec"><h3>${esc(s.label||s.key)}</h3>${GGRP(s)}${TTBL(s)}${(s.groups&&s.groups.length)?'':`<p>${esc(s.text)}</p>`}${zx}${LKR(s)}</div>`;};
let VARIANT_MAP=null;
async function variantsFor(ch){
  if(!VARIANT_MAP){
    try{VARIANT_MAP=await (await fetch('cards/variants.json?v='+Date.now())).json();}catch(e){VARIANT_MAP={};}
  }
  const list=VARIANT_MAP[ch]||[];
  if(!list.length) return '';
  const btns=list.map(v=>`<button class="vbtn" onclick="goCard('${v}')">${v}</button>`).join(' ');
  return `<div class="vbox"><span>对应繁体/借字：</span>${btns}<span class="vnote">（分卡各释本义，勿混）</span></div>`;
}
const SEC_ORDER=['benyi','benyi2','zhuanyi','bianzheng','yinyuan','shiyi','shengmu','zizu','zigen'];
const secRank=k=>{const i=SEC_ORDER.indexOf(k);return i<0?99:i;};
async function cardBody(ch,d,opt){
  const vhtml=await variantsFor(ch);
  const g=(GLYPH[ch]&&(GLYPH[ch].files||[]))||[];
  const gsrc=f=>encodeURI('glyphs/'+ch+'/'+(String(f).startsWith(ch+'/')?String(f).slice(ch.length+1):f));
const strip=g.length?`<div class="gscroll">${g.map((f,i)=>`<figure><img loading="lazy" src="${gsrc(f)}" alt="${esc(ch)}" title="${esc(f)}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:'<p class="m" style="color:var(--mut)">（字形库未收本字古文字形）</p>';
  const grp=s=>{ if(!s.groups||!s.groups.length) return '';
  return s.groups.map(g=>`<div class="grp"><h4>${esc(g.title)}</h4><p class="gnote">${esc(g.note||'')}</p>
  <table class="ct"><thead><tr><th>字</th><th>读音</th><th>类属</th><th>取义落点</th></tr></thead><tbody>${g.rows.map(r=>`<tr><td class="zc">${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td>${esc(r[3])}</td></tr>`).join('')}</tbody></table></div>`).join('');
};
const tbl=s=>{ if(!s.rows||s.rows.length<3) return '';
  const head='<tr><th>字</th><th>类属</th><th>取义落点</th></tr>';
  return `<table class="ct"><thead>${head}</thead><tbody>${s.rows.map(r=>`<tr><td class="zc">${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table>`;
};
let hasZX=false;const isZX=s=>s.key==='zigen'||s.key==='zixing'||/字形/.test(s.label||'');
const LKR=(s)=>((s&&s.links&&s.links.length)?("<p class=\"lks\">"+s.links.map(l=>"<a href=\"javascript:void(0)\" onclick=\"goCard('"+l.ch+"')\">"+esc(l.label)+"</a>").join(" · ")+"</p>"):"");
const secs=(d.sections||[]).filter(s=>!isZX(s)).sort((a,b)=>secRank(a.key)-secRank(b.key)).map(s=>{ if(isZX(s)) hasZX=true;
  const zx='';
  return `<div class="sec"><h3>${esc(s.label||s.key)}</h3>${grp(s)}${tbl(s)}<p>${esc(s.text)}</p>${zx}${LKR(s)}${(s.cites&&s.cites.length)?`<div class="cites">${s.cites.map(c=>`<span class="tag">${esc(c)}</span>`).join('')}</div>`:''}</div>`;}).join('');

  const parentBlock = (d.level>1 && d.parent) ? await (async()=>{ try{
      const pr=await fetch('cards/'+encodeURIComponent(d.parent)+'.json?v='+Date.now()); if(!pr.ok) return '';
      const p=await pr.json();
      const pg=((GLYPH[d.parent]&&GLYPH[d.parent].files)||[]);
      const pgsrc=f=>encodeURI('glyphs/'+d.parent+'/'+(String(f).startsWith(d.parent+'/')?String(f).slice(d.parent.length+1):f));
      const pstrip=pg.length?`<div class="gscroll">${pg.map((f,i)=>`<figure><img loading="lazy" src="${pgsrc(f)}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:'';
      const pb=(p.bus||[])[0]||{};
      const inner=await cardBody(d.parent,p,{noPhoto:true});
      return `<div class="sec rootbox"><h3>字根「${esc(d.parent)}」</h3>${inner}</div>`;
    }catch(e){ return ''; } })() : '';
  const lvlTag = d.level?`<span class="tag">${d.level===1?'一級字根':d.level===2?'二級字根':'谐声字'}</span>`:'';
  const b=(d.bus||[])[0]||{};
  const photoBlock=(()=>{let P=(window.PHOTO||{})[ch]||[];let own=true;let who=ch;const pm=(window.CARDS||{})[d.parent];if(!P.length&&d.level===3&&d.parent&&pm&&pm.lv===1){P=(window.PHOTO||{})[d.parent]||[];own=false;who=d.parent;}if(!P.length)return '';return '<div class="sec"><h3>插图'+(own?'':'（字根）')+'</h3><div class="gscroll">'+P.map(f=>'<figure><img loading="lazy" src="glyphs/photos/'+encodeURIComponent(who)+'/'+encodeURIComponent(f)+'" alt="'+esc(ch)+'"><figcaption>'+esc(f.replace(/\.[a-z]+$/i,''))+'</figcaption></figure>').join('')+'</div></div>';})();

  return `${vhtml}<div class="card"><div class="chead"><div class="ch">${esc(ch)}${d.simp?`（${esc(d.simp)}）`:''}</div><div class="py">${esc(d.pinyin||'')}</div><div class="bu">${lvlTag}第${esc(String(b.num||'?'))}部 ${esc(b.name||'')}</div></div>${strip}${secs}${(opt&&opt.noPhoto)?'':photoBlock}${parentBlock}</div>`;
}
async function open(ch){
  cur=ch; render($('#q').value);
  const main=$('#main'); main.innerHTML='<div class="empty">读取中…</div>';
  let d;
  try{ d=await (await fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now())).json(); }
  catch(e){ main.innerHTML='<div class="empty">没有这张卡：'+esc(ch)+'</div>'; return; }
main.innerHTML = await cardBody(ch,d);
}
$('#q').addEventListener('input',e=>render(e.target.value));
try{window.goCard=open;}catch(e){}
  async function tryDirect(ch){
  try{ const r=await fetch('cards/'+encodeURIComponent(ch)+'.json'); if(!r.ok) return false; const d=await r.json(); if(!d||!d.sections) return false;
    IDX.unshift({c:ch,p:d.pinyin||'',b:((d.bus||[{}])[0]||{}).num||'',n:((d.bus||[{}])[0]||{}).name||'',t:[]}); return true; }catch(e){ return false; }
}
$('#q').addEventListener('keydown',async e=>{
  if(e.key!=='Enter') return;
  const q=e.target.value.trim();
  if(q.length===1 && !IDX.some(x=>x.c===q)){ if(await tryDirect(q)) open(q); else render(q); }
});



const $=s=>document.querySelector(s);
let IDX=[], GLYPH={}, cur='';
const norm=s=>(s||'').toLowerCase();
fetch('cards/index.json?v='+Date.now()).then(r=>r.json()).then(d=>{IDX=d;$('#hint').textContent=`共 ${d.length} 张卡`;render('');}).catch(e=>$('#hint').textContent='索引加载失败：'+e);
fetch('glyphs/index.json').then(r=>r.json()).then(d=>{GLYPH=d.chars||d;}).catch(()=>{});
fetch('glyphs/photos/index.json?v='+Date.now()).then(r=>r.json()).then(d=>{window.PHOTO=d.photos||d;}).catch(()=>{}); fetch('glyphs/photos/captions.js?v=20261029bon?v='+Date.now()).then(r=>r.json()).then(d=>{window.CAPS=d.captions||d;}).catch(()=>{});
function match(q){
  q=norm(q.trim()); if(!q) return IDX.slice(0,200);
  const exact=IDX.filter(x=>x.c===q||((x.a||[]).includes(q))||((x.v||[]).includes(q))).sort((a,b)=>(b.c===q)-(a.c===q));
  if(exact.length) return exact.concat(IDX.filter(x=>x.c!==q&&!((x.a||[]).includes(q))&&(norm(x.p).startsWith(q)||x.t.some(t=>norm(t).includes(q)))).slice(0,80));
  return IDX.filter(x=>norm(x.c).includes(q)||((x.a||[]).some(t=>norm(t).includes(q)))||((x.v||[]).some(t=>norm(t).includes(q)))||norm(x.p).includes(q)||x.t.some(t=>norm(t).includes(q))).slice(0,120);
}
window.fillFam=(ch)=>{fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now()).then(r=>r.json()).then(d=>{const seen=new Set(),names=[];(d.sections||[]).forEach(s=>(s.groups||[]).forEach(g=>(g.rows||[]).forEach(r=>{let c=String(r[0]||'').replace(/（.*?）|\(.*?\)/g,'').trim();if(c&&!seen.has(c)){seen.add(c);names.push(c);}})));const sp=document.getElementById('famspan');if(!names.length){kh=IDX.filter(x=>x.pr===ch).map(x=>x.c);kh.forEach(c=>names.push(c));}
if(sp&&names.length){sp.innerHTML='　<label>字族</label>　'+names.map(famln).join('');bindHint();}}).catch(()=>{});};
const famln=(ch)=>{const it=IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch)));const as=(it&&it.a||[]).filter(x=>x!==(it?it.c:ch));const al=as.length?('（'+as.join('/')+'）'):'';const lab=(it?it.c:ch);return `<a data-c="${esc(ch)}" style="color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer">${esc(lab)+esc(al)}</a>`;};
window.bindHint=()=>{document.querySelectorAll('#hint a[data-c]').forEach(a=>a.onclick=()=>open(a.dataset.c));};
function render(q){
  const rows=match(q);
  $('#list').innerHTML=rows.map(x=>`<div class="item${x.c===cur?' on':''}" data-c="${x.c}"><b>${x.c}</b><span class="m">${x.p||''}</span><span class="m">${x.ch?(function(){var L='第'+x.ch+'章'+(x.cn?' '+x.cn:'');return (x.cc?('<a href="javascript:void(0)" class="chp" onclick="goCard(\''+x.cc+'\')">'+L+'</a>'):L);}()):('第'+(x.b||'?')+'部')} ${x.ch?'':(x.n||'')}</span></div>`).join('')||'<div class="empty">无结果</div>';
  const base=q?`命中 ${rows.length} 张`:`共 ${IDX.length} 张卡`;
  let rel='';
  if(q){
    const byChar=ch=>IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch)));
    let t=byChar(q)||rows.find(r=>r.lv>0)||rows[0];
    if(t){
      const chain=[];let p=(t.rc&&t.rc.length)?t.rc[t.rc.length-1]:(t.pr||t.n);let guard=0;
      while(p&&guard++<5){chain.push(p);const pc=byChar(p);const nx=pc?pc.pr:'';if(nx===p)break;p=nx;}if(t.rc&&t.rc.length)chain.length=0,(t.rc).forEach(x=>chain.push(x));else if(t.lv===2)chain.push(t.c);
      const kids=IDX.filter(x=>x.pr===t.c).map(x=>x.c);
      const ln=(ch)=>{const it=IDX.find(x=>x.c===ch)||IDX.find(x=>((x.a||[]).includes(ch)));const as=(it&&it.a||[]).filter(x=>x!==(it?it.c:ch));const al=as.length?('（'+as.join('/')+'）'):'';const lab=(it?it.c:ch);return `<a data-c="${esc(ch)}" style="color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer">${esc(lab)}</a>`;};
      const rl=t.rlb?esc(t.rlb):((t.rc2&&t.rc2.length)?t.rc2.map(o=>'<a data-c=\"'+esc(o.ch)+'\" style=\"color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a;margin:0 2px;cursor:pointer\">'+esc(o.label)+'</a>').join(' → '):(chain.length?((t.lv===2?chain:chain.slice().reverse()).map(ln).join(' → ')):'—'));
      let fam='';
      if(t.lv===3&&t.pr&&!t.rl){const seenS=new Set([t.c]);const sibs=[];
        IDX.filter(x=>x.pr===t.pr).forEach(x=>{const it=byChar(x.c)||x;const key=it.c;if(seenS.has(key))return;seenS.add(key);sibs.push(key);});
        if(sibs.length){fam='　同族　'+sibs.map(ln).join('');}}
      if(t.chapter||t.ch){const vols=IDX.filter(x=>x.ch&&x.ch===t.ch&&(x.c||'').indexOf('卷')===0).map(x=>x.c);rel=vols.length?('<span style="margin-left:14px">'+vols.map(ln).join('　')+'</span>'):' ';}else{rel=`<span style="margin-left:14px">字根　${rl}${fam}<span id="famspan"></span></span>`;}
      if(!(t.chapter||t.ch)) window.fillFam(t.c);
    }
  }
  $('#hint').innerHTML=base+rel;
  bindHint();
  $('#list').querySelectorAll('.item').forEach(el=>el.onclick=()=>open(el.dataset.c));
}
function esc(s){return (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
const gt=(t,dir)=>esc(t).replace(/\{\{([^}]+)\}\}/g,(m,f)=>`<img class="gin" src="glyphs/${dir}/${f}">`);
function esc2(s){return esc(String(s==null?'':s)).replace(/[\u{20000}-\u{2FFFF}]/gu,c=>'@@IMG@@'+c.codePointAt(0).toString(16)+'@@').replace(/@@IMG@@([0-9a-f]+)@@/g,(m,h)=>'<img class="cim" data-t="&#x'+h+';" src="glyphs/chars/'+h+'.png" onerror="this.replaceWith(document.createTextNode(this.dataset.t))">');}
function sm(s){return esc2(s).replace(/（[^）]{1,12}）/g,m=>'<span class="smalt">'+m+'</span>');}
const GGRP=s=>{if(!s.groups||!s.groups.length)return '';return (s.text?'<p class="gnote">'+esc(s.text)+'</p>':'')+s.groups.map(g=>`<div class="grp">${g.title?'<h4>'+esc(g.no||'')+esc(g.title)+'</h4>':''}<p class="gnote">${esc(g.note||'')}</p><table class="ct"><thead><tr>${(((g.title||'').indexOf('部目')>=0)?['部目','字根','中心义','字族']:(g.header||((g.rows&&g.rows[0]&&String(g.rows[0][0]).slice(-1)==='部')?['部目','字根','中心义','字族']:['字','读音','类属','取义落点']))).map(t=>'<th>'+esc(t)+'</th>').join('')}</tr></thead><tbody>${g.rows.map((r,i)=>`<tr><td class="${g.header?'':'zc'}">${(g.links&&g.links[i])?('<a href="javascript:void(0)" onclick="goCard(\''+g.links[i]+'\')">'+esc2(r[0])+'</a>'):esc2(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td>${esc(r[3])}</td></tr>`).join('')}</tbody></table></div>`).join('');};
const TTBL=s=>{if(!s.rows||s.rows.length<3)return '';const head='<tr><th>字</th><th>类属</th><th>取义落点</th></tr>';return `<table class="ct"><thead>${head}</thead><tbody>${s.rows.map(r=>`<tr><td class="zc">${esc2(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table>`;};
const secHTML=(s,ch2)=>{const g2=(GLYPH[ch2]&&(GLYPH[ch2].files||[]))||[];const st=g2.length?`<div class="gscroll">${g2.map((f,i)=>`<figure><img loading="lazy" src="${encodeURI('glyphs/'+ch2+'/'+(String(f).startsWith(ch2+'/')?String(f).slice(ch2.length+1):f))}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:'';const zx=(s.key==='zixing'||/字形|古文字/.test(s.label||''))?st:'';return `<div class="sec"><h3>${esc(s.label||s.key)}</h3>${(()=>{try{return GGRP(s)+TTBL(s)}catch(e){return '<p class="err">表格渲染失败：'+esc(String(e))+'</p>'}})()}${(s.groups&&s.groups.length)?'':`${s.text?'<p>'+(s.gdir?gt(s.text,s.gdir):((s.text||'').indexOf('gscroll')>=0?s.text:esc(s.text).replace(/\{\{gin:([^}]+)\}\}/g,'<img class="gin" src="$1" alt="字形">')))+'</p>':''}`}${zx}${(s.gimgs||[]).map(f=>`<img class="gin" src="glyphs/${f}">`).join('')}${LKR(s)}</div>`;};
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
const strip=g.length?`<div class="gscroll">${g.map((f,i)=>`<figure><img loading="lazy" src="${gsrc(f)}" alt="${esc(ch)}" title="${esc(f)}"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:((d.chapter||d.level===0)?'':'<p class="m" style="color:var(--mut)">（字形库未收本字古文字形）</p>');
  const grp=s=>{ if(!s.groups||!s.groups.length) return '';
  return s.groups.map(g=>`<div class="grp">${g.title?'<h4>'+esc(g.no||'')+esc(g.title)+'</h4>':''}<p class="gnote">${esc(g.note||'')}</p>
  <table class="ct"><thead><tr>${((g.title||'').indexOf('部目')>=0?['部目','字根','中心义','字族']:(g.header||['字','读音','类属','取义落点'])).map(t=>'<th>'+esc(t)+'</th>').join('')}</tr></thead><tbody>${g.rows.map(r=>`<tr><td class="zc">${esc2(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td>${esc(r[3])}</td></tr>`).join('')}</tbody></table></div>`).join('');
};
const tbl=s=>{ if(!s.rows||s.rows.length<3) return '';
  const head='<tr><th>字</th><th>类属</th><th>取义落点</th></tr>';
  return `<table class="ct"><thead>${head}</thead><tbody>${s.rows.map(r=>`<tr><td class="zc">${esc2(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table>`;
};
let hasZX=false;const isZX=s=>!(s.text||'').includes('gscroll')&&(s.key==='zigen'||s.key==='zixing'||/字形/.test(s.label||''));
const LKR=(s)=>((s&&s.links&&s.links.length)?("<p class=\"lks\">"+s.links.map(l=>"<a href=\"javascript:void(0)\" onclick=\"goCard('"+l.ch+"')\">"+esc(l.label)+"</a>").join(" · ")+"</p>"):"");
const ss=(d.sections||[]).find(s=>s.label==='所属卷'); const secs=(d.sections||[]).filter(s=>!isZX(s)&&s.label!=='所属卷').sort((a,b)=>secRank(a.key)-secRank(b.key)).map(s=>{ if(isZX(s)) hasZX=true;
  const zx='';
  return `<div class="sec"><h3>${esc(s.label||s.key)}</h3>${grp(s)}${tbl(s)}${(s.groups&&s.groups.length)?'':(s.text?('<p style="text-indent:2em">'+(s.gdir?gt(s.text,s.gdir):((s.text||'').indexOf('gscroll')>=0?s.text:esc(s.text).replace(/\{\{gin:([^}]+)\}\}/g,'<img class="gin" src="$1" alt="字形">'))).replace(/\n+/g,'</p><p style="text-indent:2em">')+'</p>'):'')}${zx}${(s.gimgs||[]).map(f=>`<img class="gin" src="glyphs/${encodeURI(f)}" alt="参证字形">`).join('')}${LKR(s)}${(s.cites&&s.cites.length)?`<div class="cites">${s.cites.map(c=>`<span class="tag">${esc(c)}</span>`).join('')}</div>`:''}</div>`;}).join('');

  const rootLink = '';
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

  const lvlTag = d.level?`<span class="tag">${d.rootLevel?({1:'一級字根',2:'二級字根',3:'三級字根'}[d.rootLevel]||'字根'):(d.level===1?'一級字根':d.level===2?'二級字根':'谐声字')}</span>`:'';
  const b=(Array.isArray(d.bus)?d.bus[0]:(d.bus||{}))||{};
  const photoBlock=(()=>{if(!window.PHOTO)return '';const own=d.photos||(window.PHOTO&&window.PHOTO[d.char])||[];if(!own.length)return '';const cap=d.captions||(window.CAPS&&window.CAPS[d.char])||[];return '<div class="sec"><h3>插图</h3><div class="pscroll">'+own.map((f,i)=>'<figure><img loading="lazy" src="'+encodeURI('glyphs/photos/'+d.char+'/'+f)+'"><figcaption>'+esc(cap[i]||('图'+(i+1)))+'</figcaption></figure>').join('')+'</div></div>';})();

  return `${vhtml}<div class="card"><div class="chead"><div class="ch">${d.chapterCard?('<a href="javascript:void(0)" class="chp" onclick="goCard(\''+d.chapterCard+'\')">第'+(d.chapter||'')+'章 '+esc(d.chapterName||'')+'</a>'):sm(d.head||d.cname||ch)}${(d.bus&&d.bus[0]&&(d.bus[0].name||'').indexOf('卷')===0)?(' · '+sm(d.head||d.cname||ch)):''}${(d.simp&&!d.cname&&!(d.head||'').includes('（'))?`（${esc(d.simp)}）`:''}</div><div class="py">${esc(d.pinyin||'')}</div><div class="bu">${lvlTag}${d.chapterCard?'':('第'+String(b.num||'?')+'部 '+esc(b.name||''))}</div></div>${strip}${secs}${(opt&&opt.noPhoto)?'':photoBlock}${rootLink}${d.noRoot?'':parentBlock}${ss?'<div class="sec"><h3>所属卷</h3>'+(LKR(ss)||(ss.text?'<p>'+esc(ss.text)+'</p>':''))+'</div>':''}</div>`;
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
  try{ const r=await fetch('cards/'+encodeURIComponent(ch)+'.json?v='+Date.now()); if(!r.ok) return false; const d=await r.json(); if(!d||!d.sections) return false;
    IDX.unshift({c:ch,p:d.pinyin||'',b:(Array.isArray(d.bus)?(d.bus[0]||{}):(d.bus||{})).num||'',n:(Array.isArray(d.bus)?(d.bus[0]||{}):(d.bus||{})).name||'',t:[]}); return true; }catch(e){ return false; }
}
$('#q').addEventListener('keydown',async e=>{
  if(e.key!=='Enter') return;
  const q=e.target.value.trim();
  if(q.length===1 && !IDX.some(x=>x.c===q)){ if(await tryDirect(q)) open(q); else render(q); }
});


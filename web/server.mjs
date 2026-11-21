// server.mjs 鈥?銆岀郴缁熸眽瀛椼€嶇煡璇嗗簱闂瓟缃戦〉鏈嶅姟锛堥浂渚濊禆 Node锛?
// 鍙仛涓や欢浜嬶細鎶婇棶棰樹氦缁?pkc 妫€绱紝鎶婃绱㈠埌鐨?Claim 缁勭粐鎴愭湁鍑哄鐨勭瓟妗堛€?
// 缁濅笉鐩存帴璇?knowledge/** 鎴?.local/锛屼竴鍒囩粡鐢?pkc-bridge.py 鈫?pkc銆?

import { createServer } from 'node:http';
import { spawn } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { join, extname, normalize, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { randomBytes, timingSafeEqual } from 'node:crypto';
import { Shop, TIERS, TRIAL_LIMIT, DAILY_CAP, readCookie } from './member.mjs';

const WEB = fileURLToPath(new URL('.', import.meta.url));
const ROOT = normalize(join(WEB, '..'));

// ---- server-side card page (no client JS needed) ----
const CARDDIR = join(WEB, 'public', 'cards');
function escH(s){return String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function ext(s){
  let out='';
  for (const ch of String(s==null?'':s)){
    const cp=ch.codePointAt(0);
    if (cp>=0x20000 && cp<=0x2FFFF){
      const name=cp.toString(16)+'.png';
      if (existsSync(join(ROOT,'web','public','glyphs','chars',name))) { out+='<img class="cim" src="/glyphs/chars/'+name+'">'; continue; }
    }
    out+=escH(ch);
  }
  return out;
}
function renderCard(ch){
  const fp=join(CARDDIR, ch+'.json');
  if (!existsSync(fp)) return null;
  const d=JSON.parse(readFileSync(fp,'utf8'));
  let h='<!doctype html><meta charset="utf-8"><title>'+escH(d.head||d.char)+'</title>';
  h+='<style>.jl{color:inherit;text-decoration:none;border-bottom:1px dashed #c9b79a}.al{color:#8a5a2b;text-decoration:none;border-bottom:1px dashed #d8b48a}body{font:16px/1.85 "Microsoft YaHei",sans-serif;max-width:1000px;margin:22px auto;padding:0 18px;color:#222}h2{font-size:40px;margin:0 0 4px}h3{color:#a33;margin:24px 0 6px;font-size:19px}h4.sub{color:#8a5a2b;margin:14px 0 2px;font-size:16px}table{border-collapse:collapse;width:100%;margin:6px 0 12px}td,th{border:1px solid #dcdcdc;padding:7px 9px;vertical-align:top;font-size:15px}th{background:#f3ece0;text-align:left}.cch{height:1.05em;vertical-align:-0.12em}'+
  '<style>.cim{height:2.1em;vertical-align:-0.45em;margin:0 2px}.ciw{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 10px}.ciw{align-items:flex-end}.ciw .cibw{display:inline-block;text-align:center;margin:2px 4px 8px 0}.ciw .ciblab{display:inline-block;color:#8a6d3b;font-size:15px;margin:0 14px 26px 2px}.ciw img{height:104px;border:1px solid #e7e0d2;border-radius:6px;background:#fff}.gs{display:flex;gap:10px;overflow-x:auto;padding:6px 0 10px}.gs figure{margin:0;text-align:center}.gs img{height:110px;border:1px solid #e7e0d2;border-radius:6px;background:#fff}.gsbar{position:relative}.gsbar .gs{padding:6px 34px}.gsnav{position:absolute;top:50%;transform:translateY(-50%);z-index:3;width:28px;height:60px;border:1px solid #e0d8c8;border-radius:6px;background:rgba(255,252,245,.92);color:#8a6d3b;font-size:20px;line-height:56px;text-align:center;cursor:pointer;user-select:none}.gsnav:hover{background:#fff}.gsl{left:0}.gsr{right:0}.gs figcaption{font-size:11px;color:#999}.pill{display:inline-block;margin:2px 0 8px;padding:1px 10px;border:1px solid #ddd;border-radius:12px;color:#666;font-size:13px}small{color:#888;font-weight:400}.back{display:inline-block;margin-bottom:10px;color:#06c}</style>';
  const _hd=String(d.head||d.char);const _m=_hd.match(/^([^锛?]+)[锛?]([^锛?]*)[锛?]\s*$/);const _hl=_m?escH(_m[1])+'锛?+Array.from(_m[2]).map(a=>'<a class="al" href="/card/'+encodeURIComponent(a)+'">'+escH(a)+'</a>').join('')+'锛?:ext(_hd);
  h+='<a class="back" href="/test.html">鈫?杩斿洖妫€绱?/a><h2>'+_hl+' <small>'+escH(d.pinyin||'')+'</small></h2>';
  let _b0=Array.isArray(d.bus)?d.bus[0]:(d.bus||null);
  try { if(!_b0||!_b0.num){ let pr=d.parent, hop=0; while(pr&&hop<3){ const pf=join(CARDDIR,pr+'.json'); if(existsSync(pf)){ const pd=JSON.parse(readFileSync(pf,'utf8')); const pb=Array.isArray(pd.bus)?pd.bus[0]:pd.bus; if(pb&&pb.num){ _b0=pb; break; } pr=pd.parent; } else break; hop++; } } } catch(e){}
  try { const b0=_b0; const _fam=(d.sections||[]).some(x=>x&&x.key==='zizu'&&(x.groups||[]).length); const lv=d.grade||(d.level===1?'涓€绾у瓧鏍?:d.level===2?'浜岀骇瀛楁牴':(d.level===3&&_fam)?'涓夌骇瀛楁牴':d.level===3?'璋愬０瀛?:''); let pill=lv; const _rc=(Array.isArray(d.rootChain)&&d.rootChain.length>1)?(' 路 '+d.rootChain.join(' 鈫?')):''; if(_rc) pill+=_rc; if(b0&&b0.num>0) pill+=' 路 绗?+b0.num+'閮ㄣ€?+String(b0.name||'').replace(/閮?/,'')+'閮ㄣ€?; else if(b0&&b0.name) pill+=' 路 銆?+b0.name+'閮ㄣ€?; if(pill) h+='<p class="pill">'+pill+'</p>'; } catch(e){}
  try { const gi=glyphInfo(d.char); if (gi && gi.files && gi.files.length){ h+='<div class="gs">'+gi.files.map((u,i)=>'<figure><img src="'+u+'?v='+Date.now()+'" alt="瀛楀舰'+(i+1)+'"><figcaption>'+String(i+1).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'; } } catch(e){}
  let _photosH='';
  try { const ex=((loadGlyphIndex().chars||{})[d.char]||{}).extra||[];
    for (const e of ex){ const g2=glyphInfo(e.char); if(!g2 || !g2.files || !g2.files.length) continue;
      h+='<p><b>'+escH(e.label||e.char)+'</b></p><div class="gs">'+g2.files.map((u,i)=>'<figure><img src="'+u+'?v='+Date.now()+'" alt="瀛楀舰'+(i+1)+'"><figcaption>'+String(i+1).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'; }
  } catch(e){}
  try { const gi2=glyphInfo(d.char); const ps=(gi2&&gi2.photos)||[]; if (ps.length){ _photosH='<h3>鎻掑浘</h3><div class="gs">'+ps.map(p=>{const f=(typeof p==='string')?p:(p.file||p.name||'');const cap=(typeof p==='object'&&p.caption)?p.caption:'';return '<figure><img src="'+escH((String(f).startsWith('/')?f:('/glyphs/photos/'+encodeURIComponent(d.char)+'/'+encodeURIComponent(f)))+'?v=20261121a')+'" alt="'+escH(cap||'鎻掑浘')+'" style="height:170px"><figcaption>'+escH(cap||'')+'</figcaption></figure>';}).join('')+'</div>'; } } catch(e){}
  try {
    const _hasZigen=(d.sections||[]).some(x=>['zigen','rootembed'].includes(x.key)||String(x.label||'').startsWith('瀛楁牴銆?));
    if (d.parent && !_hasZigen && !d.noRoot) {
      const pf2 = join(CARDDIR, d.parent + '.json');
      if (existsSync(pf2)) {
        const pd2 = JSON.parse(readFileSync(pf2, 'utf8'));
        const keep = (pd2.sections || []).filter(x => ['benyi','zhuanyi','bianzheng','yinyuan'].includes(x.key) && (x.text || (x.paras && x.paras.length)));
        if (keep.length) {
          const label = '瀛楁牴銆? + (pd2.head || pd2.char || d.parent) + '銆?;
          const subs = keep.map(x => ({ label: x.label || '', paras: (x.paras && x.paras.length ? x.paras.slice() : [String(x.text || '')]).flatMap(p => String(p).split(/\n+/).filter(Boolean)) }));
          const _i = (d.sections || []).findIndex(x => x.key === 'suoshujuan');const _pg = (pd2.gdir || ('inline/' + (pd2.char || d.parent)));const _sec = { key: 'rootembed', label: label, subs: subs, gdir: _pg };if (_i >= 0) d.sections.splice(_i, 0, _sec); else d.sections = (d.sections || []).concat([_sec]);
        }
      }
    }
  } catch (e) {}

  for (const s of (d.sections||[]).filter(x=>x.key==="ziatt")){
    h+="<p><b>"+ext(s.label||"")+"</b> "+((s.gimgs||[]).map(f=>"<img class=\"cim\" src=\"/glyphs/"+String(f).split("/").map(encodeURIComponent).join("/")+"\" style=\"height:2.2em;margin:0 6px 0 2px\">").join(""))+"</p>";
  }
  for (const s of (d.sections||[])){ if (s.key==="ziatt") continue;
    if (s.label==='鎵€灞炲嵎'){ h+='<h3>鎵€灞炲嵎</h3><p>'+(((s.links&&s.links.length?s.links:(d.links||[]))).map(l=>'<a class="jl" href="/card/'+encodeURIComponent(l.ch)+'">'+escH(l.label||l.ch)+'</a>').join(' 路 '))+'</p>'; continue; }
    h+='<h3>'+escH(s.label||s.key)+'</h3>';
    if (s.key==='erji' && s.links && s.links.length){
      h+='<p>'+s.links.map(l=>'<a class="jl" href="/card/'+encodeURIComponent(l.ch)+'">'+escH(l.label||l.ch)+'</a>').join(' 路 ')+'</p>';
      continue;
    }
    if (s.subs && s.subs.length){
      for (const sub of s.subs){
        if (sub.label) h+='<h4 class="sub">'+escH(sub.label)+'</h4>';
        for (const pp of (sub.paras||[])){
          const parts=[]; let tx=String(pp).replace(/\{\{([^}]+)\}\}/g,(m,f)=>{parts.push(((s.gdir||'')+'/'+f)); return '\u0002'+(parts.length-1)+'\u0003';});
          tx=ext(tx);
          tx=tx.replace(/\u0002(\d+)\u0003/g,(m,i)=>'<img class="cim" src="/glyphs/'+String(parts[+i]).split('/').map(encodeURIComponent).join('/')+'?v=20261112a">');
          h+='<p>'+tx+'</p>';
        }
      }
      if (s.gimgs && s.gimgs.length){ /* 瀛楁牴鍧椾笉閲嶅鍒楀瓧褰?*/ }
      continue;
    }
    if (s.groups && s.groups.length){
        if (s.text) h+='<p>'+ext(s.text)+'</p>';
      for (const g of s.groups){
        if (g.title) h+='<p><b>'+escH(g.no||'')+ext(g.title)+'</b></p>';
        if (g.note) h+='<p style="color:#666">'+ext(g.note)+'</p>';
        const head=(String(g.title||'').indexOf('閮ㄧ洰')>=0)?['閮ㄧ洰','瀛楁牴','涓績涔?,'瀛楁棌']:(g.header||['瀛?,'璇婚煶','绫诲睘','鍙栦箟钀界偣']);
        h+='<table><tr>'+head.map(t=>'<th>'+escH(t)+'</th>').join('')+'</tr>';
        for (const r of (g.rows||[])) h+='<tr>'+r.map((x,i)=>{
          let cell=ext(x);
          try { if (i===0 && String(head[0])==='閮ㄧ洰'){ const m=/^(.+?)閮?/.exec(String(x||'').trim()); if(m && existsSync(join(CARDDIR,m[1]+'.json'))) cell='<a href="/card/'+encodeURIComponent(m[1])+'">'+cell+'</a>'; } } catch(e){}
          return '<td>'+cell+'</td>';
        }).join('')+'</tr>';
        h+='</table>';
      }
    } else if (s.cimgs) { h+='<div class="gsbar"><button class="gsnav gsl" aria-label="宸︾炕" onclick="var s=this.parentNode.querySelector(\'.gs\');s.scrollBy({left:-260,behavior:\'smooth\'})">鈥?/button><div class="gs">'+s.cimgs.map(f=>{const o=(typeof f==='string')?{f:f}:(f||{});const src='/glyphs/'+String(o.f||'').split('/').map(encodeURIComponent).join('/');return '<figure><img src="'+src+'" alt="'+escH(o.cap||'鍙傝瘉')+'" style="height:88px"><figcaption>'+escH(o.cap||'')+'</figcaption></figure>';}).join('')+'<button class="gsnav gsr" aria-label="鍙崇炕" onclick="var s=this.parentNode.querySelector(\'.gs\');s.scrollBy({left:260,behavior:\'smooth\'})">鈥?/button></div>'; } else if (Array.isArray(s.paras) && s.paras.length) { h+=s.paras.map(pp=>{ const parts=[]; let tx=String(pp).replace(/\{\{([^}]+)\}\}/g,(m,f)=>{parts.push(((s.gdir||'')+'/'+f)); return '\u0002'+(parts.length-1)+'\u0003';}); tx=ext(tx); tx=tx.replace(/\u0002(\d+)\u0003/g,(m,i)=>'<img class="cim" src="/glyphs/'+String(parts[+i]).split('/').map(encodeURIComponent).join('/')+'?v=20261121a">'); return '<p>'+tx+'</p>'; }).join(''); } else if (s.text) { const parts=[]; let tx=String(s.text).replace(/\{\{([^}]+)\}\}/g,(m,f)=>{parts.push(((s.gdir||'')+'/'+f)); return '\u0002'+(parts.length-1)+'\u0003';}); tx=ext(tx); tx=tx.replace(/\u0002(\d+)\u0003/g,(m,i)=>'<img class="cim" src="/glyphs/'+String(parts[+i]).split('/').map(encodeURIComponent).join('/')+'?v=20261121a">'); h+='<p>'+tx+'</p>'; }
    if (s.gimgs && s.gimgs.length){
      let cur=null;
      for (const f of s.gimgs){
        const lab=String(f).includes('/')?String(f).split('/')[0]:'';
        if (lab!==cur){ if(cur!==null) h+='</p>'; h+=(lab?'<p><b>'+ext(lab)+'</b> ':'<p>'); cur=lab; }
        h+='<img class="cim" src="/glyphs/'+String(f).split('/').map(encodeURIComponent).join('/')+'" style="height:2.2em;margin:0 6px 0 2px">';
      }
      if(cur!==null) h+='</p>';
    }
  }
  h+=_photosH;
  return h;
}

const PUBLIC = join(WEB, 'public');
const PYEXE = join(ROOT, '.runtime', 'python', 'python.exe');
const BRIDGE = join(WEB, 'pkc-bridge.py');

// ---------- 浼氬憳 / 璁㈠崟 ----------

const shop = new Shop(join(WEB, 'data'));

const ADMIN_FILE = join(WEB, 'data', 'admin.key');
let ADMIN_PW = process.env.ADMIN_PASSWORD || '';
if (!ADMIN_PW) {
  if (existsSync(ADMIN_FILE)) ADMIN_PW = readFileSync(ADMIN_FILE, 'utf8').trim();
  else {
    ADMIN_PW = randomBytes(9).toString('base64url');
    writeFileSync(ADMIN_FILE, ADMIN_PW);
  }
}

function isAdmin(req) {
  return shop.verifyNamed('sh_admin', readCookie(req, 'sh_admin')) === 'ok';
}

function publicMember(m) {
  return {
    id: m.id,
    tier: m.tier,
    tier_name: m.tier_name,
    started_at: m.started_at,
    expires_at: m.expires_at,
    gift: m.gift,
    gift_sent: m.gift_sent,
    active: shop.memberStatus(m).active,
    has_password: Boolean(m.pass_hash),
    used_today: shop.usageToday(m.id),
    spent_today: shop.spendToday(m.id),
  };
}


const PORT = Number(process.env.PORT || 8088);
const HOST = process.env.HOST || '127.0.0.1';
const KEY_FILE = 'C:\\Users\\钀х\\.dsh\\secrets\\deepseek.key';
const BASE_URL = process.env.DEEPSEEK_BASE || 'https://api.deepseek.com';
const MODEL = process.env.DEEPSEEK_MODEL || 'deepseek-chat';

const RETRIEVE_LIMIT = 8;
const CONTEXT_CLAIMS = 8;
const MAX_QUESTION = 200;
const MAX_BODY = 64 * 1024;
const RATE_MAX = 20;
const RATE_WINDOW = 60_000;

// ---------- 鎴愭湰闂搁棬 ----------
// 鎸?deepseek-flash 鐨勩€岄珮宄颁环銆嶄繚瀹堣浠凤紙瀹為檯澶氭暟鏃跺€欐槸绌洪棽浠风殑涓€鍗婏級锛?
// 杩欐牱绠楀嚭鏉ョ殑涓婇檺鍙細鍋忓ぇ锛屼笉浼氳瀹㈡埛鐨勭湡瀹炶姳璐硅秴杩囬绠椼€?
// 杈撳叆锛堢紦瀛樻湭鍛戒腑锛? 鍏?鐧句竾 token锛岃緭鍑?8 鍏?鐧句竾 token銆?
const PRICE_IN_YUAN_PER_M = 2;
const PRICE_OUT_YUAN_PER_M = 8;
const TRIAL_BUDGET_YUAN = Number(process.env.TRIAL_BUDGET_YUAN || 1);      // 姣忎釜璁惧鍏嶈垂浣撻獙鏈€澶氳姳 1 鍏?
const MEMBER_DAILY_YUAN = Number(process.env.MEMBER_DAILY_YUAN || 3);      // 浼氬憳姣忓ぉ鏈€澶氳姳 3 鍏冿紝闃叉互鐢?
const MIN_CALL_YUAN = 0.004;   // 涓€娆″洖绛旈璁¤鑺辩殑鏈€浣庢垚鏈紝浣欓浣庝簬瀹冨氨涓嶅啀鏀捐
const MAX_ANSWER_TOKENS = 600; // 鍗曟鍥炵瓟杈撳嚭涓婇檺

function usageCost(usage, inChars, outChars) {
  const inTok = usage && usage.prompt_tokens ? usage.prompt_tokens : Math.round((inChars || 0) / 1.5) + 400;
  const outTok = usage && usage.completion_tokens ? usage.completion_tokens : Math.round((outChars || 0) / 1.2);
  const yuan = (inTok / 1e6) * PRICE_IN_YUAN_PER_M + (outTok / 1e6) * PRICE_OUT_YUAN_PER_M;
  return { yuan: Math.round(yuan * 1e6) / 1e6, inTok, outTok };
}

// ---------- 鍩虹宸ュ叿 ----------

function maskKey(k) {
  if (!k) return '(none)';
  return k.length <= 10 ? '***' : k.slice(0, 6) + '鈥? + k.slice(-4);
}

function log(...args) {
  console.log(new Date().toISOString(), ...args);
}

function loadKey() {
  const env = (process.env.DEEPSEEK_API_KEY || '').trim();
  if (env) return env;
  try {
    if (existsSync(KEY_FILE)) {
      const v = readFileSync(KEY_FILE, 'utf8').trim();
      if (v) return v;
    }
  } catch (e) {
    log('璇诲彇 Key 鏂囦欢澶辫触:', e.message);
  }
  return '';
}

const API_KEY = loadKey();
const MODE = API_KEY ? 'model' : 'skeleton';

// ---------- pkc 璋冪敤 ----------

function pkc(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(PYEXE, [BRIDGE, ...args], {
      cwd: ROOT,
      windowsHide: true,
      stdio: ['ignore', 'pipe', 'pipe'],
    });
    let out = '';
    let err = '';
    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');
    child.stdout.on('data', (d) => (out += d));
    child.stderr.on('data', (d) => (err += d));
    child.on('error', (e) => reject(new Error('鏃犳硶鍚姩 python: ' + e.message)));
    child.on('close', (code) => {
      const text = out.trim();
      if (!text) return reject(new Error('pkc 鏃犺緭鍑? + (err ? ': ' + err.slice(-300) : '')));
      try {
        resolve(JSON.parse(text));
      } catch {
        reject(new Error(`pkc 杩斿洖闈?JSON锛坋xit ${code}锛夛細${text.slice(0, 200)}`));
      }
    });
  });
}

let treeCache = { at: 0, data: null };

async function getTree() {
  if (treeCache.data && Date.now() - treeCache.at < 60_000) return treeCache.data;
  const raw = await pkc(['tree']);
  const text = raw.text || '';
  const nodes = [];
  let current = null;
  for (const line of text.split(/\r?\n/)) {
    const mNode = line.match(/^(\S+)\s+鈥擻s+(.+)$/);
    if (mNode) {
      current = { id: mNode[1], title: mNode[2].trim(), topics: [] };
      nodes.push(current);
      continue;
    }
    const mTopic = line.match(/鈹斺攢\s+(\S+)\s+鈥擻s+(.+?)\s+\((\d+)\s+claims\)/);
    if (mTopic && current) {
      current.topics.push({ id: mTopic[1], title: mTopic[2].trim(), claims: Number(mTopic[3]) });
    }
  }
  const claims = nodes.reduce((s, n) => s + n.topics.reduce((t, x) => t + x.claims, 0), 0);
  const data = { ok: true, nodes, claims };
  treeCache = { at: Date.now(), data };
  return data;
}

// ---------- 妫€绱?----------

function cleanQuestion(q) {
  return String(q || '')
    .replace(/[\u0000-\u001f\u007f]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, MAX_QUESTION);
}

async function retrieve(question) {
  const q = cleanQuestion(question);
  if (!q) return { question: q, hits: [], claims: [] };

  const res = await pkc(['query', q, String(RETRIEVE_LIMIT)]);
  const hits = (res.results || [])
    .filter((r) => r.kind === 'claim' && r.permission === 'public' && r.lifecycle === 'active')
    .slice(0, RETRIEVE_LIMIT);

  // 鍛戒腑鏍囬/鎽樿鐨勬潯鐩啀鍙栧叏鏂囷紙鍚€傜敤杈圭晫锛夛紝鏈€澶?CONTEXT_CLAIMS 鏉?
  return { question: q, hits, claims: await hydrate(hits) };
}

// 鍛戒腑鏍囬/鎽樿鐨勬潯鐩啀鍙栧叏鏂囷紙鍚€傜敤杈圭晫锛夛紝鏈€澶?CONTEXT_CLAIMS 鏉?
async function hydrate(hits) {
  const wanted = hits.slice(0, CONTEXT_CLAIMS);
  const claims = await Promise.all(
    wanted.map((h) =>
      pkc(['show', h.id])
        .then((r) => (r.claim ? { ...r.claim, score: h.score } : null))
        .catch((e) => {
          log('show-claim 澶辫触', h.id, e.message);
          return null;
        })
    )
  );
  return claims.filter(Boolean);
}

function buildContext(claims) {
  return claims
    .map((c, i) => {
      const body = String(c.statement || '').replace(/\r\n/g, '\n').trim();
      return `[${i + 1}] ${c.id} 銆?{c.title}銆媆n鑺傜偣/涓婚锛?{c.node_id} / ${c.topic_id}\n姝ｆ枃锛歕n${body}`;
    })
    .join('\n\n---\n\n');
}

const SYSTEM_PROMPT = `浣犳槸銆岀郴缁熸眽瀛椼€嶇煡璇嗗簱鐨勯棶绛斿姪鎵嬨€備綘鍙兘渚濇嵁涓嬮潰鎻愪緵鐨勭煡璇嗘潯鐩洖绛斻€?

瑙勫垯锛?
1. 姣忔潯缁撹鍚庨潰鐢?[clm_XXXXXXXX] 鏍囨敞鍑哄锛宨d 蹇呴』鏉ヨ嚜鏉＄洰鍒楄〃锛屼笉寰楃紪閫犮€?
2. 鏉＄洰鐨勫叏閮ㄥ唴瀹逛綘閮借兘鐪嬪埌銆傚洖绛斿墠鍏堟妸鏉＄洰閫愭潯璇昏繃锛屽啀缁勭粐绛旀锛涗笉瑕佹柇瑷€銆屾潯鐩病鏈夎杞姐€嶏紝闄ら潪浣犵‘瀹為€愭潯妫€鏌ヨ繃銆?
3. 鍙湁褰撴墍鏈夋潯鐩兘涓庨棶棰樻棤鍏虫椂锛屾墠鍥炵瓟銆岀煡璇嗗簱閲岃繕娌℃湁杩欐柟闈㈢殑鍐呭銆傘€嶏紱鑻ユ潯鐩浉鍏充絾涓嶈冻浠ュ畬鏁村洖绛旓紝鍏堣搴撻噷鏈変粈涔堬紝鍐嶆寚鍑虹己鍝竴閮ㄥ垎锛屼笉瑕佺敤浣犺嚜宸辩殑鐭ヨ瘑琛ュ厖鎴栨帹娴嬨€?
4. 灞炰簬銆婄郴缁熸眽璇€嬭鐐圭殑鏉＄洰锛岃鐐规槑杩欐槸璇ヤ功鐨勫垽鏂紝涓嶆槸鏂囩尞瀛︾晫鐨勫叡璇嗐€?
5. 涓嶈澶嶈堪缂栧彿銆佽妭鐐广€佷富棰樿繖浜涘唴閮ㄥ瓧娈碉紱涓嶈杈撳嚭鏉＄洰鍘熸枃浠ュ鐨勫唴瀹广€?
6. 绠€浣撲腑鏂囷紝鍏堢粰缁撹鍐嶇粰璇存槑锛屾帶鍒跺湪 300 瀛椾互鍐呫€俙;

function userPrompt(question, context) {
  return `鐭ヨ瘑鏉＄洰锛歕n\n${context}\n\n---\n\n鐢ㄦ埛闂锛?{question}`;
}

// ---------- 瀛楀崱妯″紡 ----------
// 妯℃澘鍥哄畾鍥涙锛氱敳楠ㄦ枃瀛楀舰鍥?/ 鏈箟 / 杞箟 / 琛嶇敓瀛椾箟锛堝摢浜涜鐢熷瓧锛夈€?
// 瀛楀舰鍥炬潵鑷€婄郴缁熸眽璇€嬪悇鍗峰師绋挎娊鍑虹殑瀛楀舰琛紙tools/extract-glyphs.mjs锛夛紝
// 鍥句笅鑷甫鍘熶功鏍囨敞鐨勫嚭澶勪笌鍒嗘湡锛涙枃瀛楅儴鍒嗗彧鍏佽鏉ヨ嚜 public+active 鐨?Claim銆?

const GLYPH_INDEX = join(PUBLIC, 'glyphs', 'index.json');
let glyphCache = { at: 0, data: null };

function loadGlyphIndex() {
  if (glyphCache.data && Date.now() - glyphCache.at < 300_000) return glyphCache.data;
  try {
    const data = JSON.parse(readFileSync(GLYPH_INDEX, 'utf8'));
    glyphCache = { at: Date.now(), data };
    return data;
  } catch (e) {
    log('瀛楀舰搴撹鍙栧け璐?', e.message);
    return { chars: {} };
  }
}

// 绠€浣撳瓧澶?鈫?鍘熺绻佷綋瀛楀ご銆傚師绋夸互绻佷綋绔嬪瓧澶达紝鐢ㄦ埛澶氭寜绠€浣撴彁闂紱
// 瀛楀舰搴撱€侀厤鍥惧簱鎸夌箒浣撳缓閿紝鏁呮澶勫仛涓€娆℃樉寮忔槧灏勶紙鍙槧灏勭‘瀹為渶瑕佺殑瀛楋紝瀹佸皯鍕挎互锛夈€?
const VARIANT_INDEX = join(PUBLIC, 'variants.json');
let variantCache = { at: 0, map: {} };

function loadVariantMap() {
  if (variantCache.at && Date.now() - variantCache.at < 300_000) return variantCache.map;
  try {
    const map = JSON.parse(readFileSync(VARIANT_INDEX, 'utf8'));
    variantCache = { at: Date.now(), map };
    return map;
  } catch {
    return {};
  }
}

function photoList(list) {
  return (list || []).map((x) => {
    if (typeof x === 'string') return { file: '/glyphs/photos/' + encodeURIComponent(x), caption: '' };
    const f = String((x && (x.file || x.name)) || '');
    return { file: f ? '/glyphs/' + f.split('/').map(encodeURIComponent).join('/') : '', caption: (x && x.caption) || '' };
  }).filter((p) => p.file);
}

// 瀛楁棌琛細鍘熺瀛楀ご琛屽啋鍙峰悗闈㈤偅涓诧紙鐗?绀?浠曗€︼級锛屾寜鍘熺椤哄簭锛屽悇鑷甫涓婅嚜宸辩殑閰嶅浘
// 鍙湁鑷繁鑳界偣鍑轰竴寮犳湁鍐呭鐨勫瓧鍗★紙鏈夌嫭绔嬫潯鐩垨鑳借惤鍒板瓧鏃忔潯锛夌殑锛屾墠鍋氭垚鍙偣锛涘惁鍒欏彧鍒楀悕涓嶉摼鎺?
function familyInfo(ch) {
  const idx = loadGlyphIndex();
  const fam = (idx.families && idx.families[ch]) || [];
  const ci = claimIdx().byChar || {};
  const vmap = loadVariantMap();
  return fam.map((c) => {
    const alt = variantOf(c);
    const hasEntry = !!(
      (ci[c] && ci[c].length) ||
      (alt && ci[alt] && ci[alt].length) ||
      ((idx.chars && idx.chars[c]) || (alt && idx.chars && idx.chars[alt]))
    );
    return { char: c, photos: [], linked: hasEntry };
  });
}

function glyphInfo(ch) {
  const idx = loadGlyphIndex();
  let key = ch;
  let e = idx.chars && idx.chars[key];
  let ph = (idx.photos && idx.photos[key]) || [];
  if ((!e || !Array.isArray(e.files) || !e.files.length) && !ph.length) {
    const alt = variantOf(ch) || aliasOf(ch);
    if (alt && alt !== ch) {
      key = alt;
      e = idx.chars && idx.chars[alt];
      ph = (idx.photos && idx.photos[alt]) || [];
    }
  }
  const files = (e && Array.isArray(e.files) ? e.files : []).map((f) => '/glyphs/' + (String(f).includes('/') ? String(f) : key + '/' + String(f)).split('/').map(encodeURIComponent).join('/'));
  const photos = photoList(ph);
  if (!files.length && !photos.length) return null;
  return {
    doc: (e && e.doc) || '',
    variants: (e && e.variants) || '',
    files,
    photos,
  };
}

// ---------- 瀛楁牴鍒嗙骇 ----------
// 渚濇嵁銆屽叏涔︾洰褰曚笌缁撴瀯銆嶏細銆岄儴鍙?閮ㄩ瀛椼€嶆槸鏈€灏忓畾浣嶅崟浣嶏紝609 閮ㄥ嵆涓€绾у瓧鏍癸紱
// 閮ㄥ唴鑳藉啀婊嬬敓鐨勮鐢熷瓧鏄簩绾с€佷笁绾у瓧鏍癸紝鍏朵綑鏄皭澹板瓧锛坈lm_640129CD鈥︼級銆?
// 閮ㄥ悕绱㈠紩鐢?tools/zigen-index.mjs 浠?mulu.md 鐢熸垚锛屾湇鍔″眰涓嶇洿鎺ヨ knowledge/銆?
const ZIGEN_INDEX = join(PUBLIC, 'zigen.json');
let zigenCache = { at: 0, data: null };

function loadZigenIndex() {
  if (zigenCache.data && Date.now() - zigenCache.at < 300_000) return zigenCache.data;
  try {
    const data = JSON.parse(readFileSync(ZIGEN_INDEX, 'utf8'));
    zigenCache = { at: Date.now(), data };
    return data;
  } catch (e) {
    log('瀛楁牴绱㈠紩璇诲彇澶辫触:', e.message);
    return { byName: {}, juan: [], chapters: [] };
  }
}

const JUAN_CN = ['', '涓€', '浜?, '涓?, '鍥?, '浜?, '鍏?, '涓?, '鍏?, '涔?, '鍗?];
function juanCn(n) {
  if (!n) return '';
  if (n <= 10) return JUAN_CN[n];
  if (n < 20) return '鍗? + JUAN_CN[n - 10];
  if (n === 100) return '涓€鐧?;
  const a = Math.floor(n / 10);
  const b = n % 10;
  return (a === 1 ? '鍗? : JUAN_CN[a] + '鍗?) + (b ? JUAN_CN[b] : '');
}

const HAN_ONE = /\p{Script=Han}/u;
const isHan = (ch) => !!ch && HAN_ONE.test(ch);
const CARD_TOPICS = /(鏈箟|鏈京|鏈剰|瀛楁簮|瀛楀舰|鐢查鏂噟杞箟|杞夌京|寮曠敵涔墊寮曠敵|琛嶇敓瀛梶琛嶇敓|瀛楁棌|瀛楁牴|鎰忔€潀鍚箟)/;

// 鍒ゆ柇闂鏄笉鏄湪銆岄棶鏌愪竴涓瓧銆?
function detectChar(question) {
  let s = String(question || '').trim();
  if (!s) return null;
  s = s.replace(/[锛?銆傦紒!锛?銆侊紱;锛?~锝瀄s]+$/g, '').trim();
  if (!s) return null;

  // 1) 寮曞彿閲岀偣鍚嶇殑瀛楋細銆岄洖銆嶃€岄浮銆?
  const quoted = s.match(/[銆屻€庘€?]([^銆嶃€忊€?]{1,3})[銆嶃€忊€?]/);
  if (quoted) {
    const cs = [...quoted[1]].filter(isHan);
    if (cs.length === 1) return cs[0];
  }

  // 2) 鏁村彞鍙湁涓€涓眽瀛楋紙鍙甫銆屽瓧銆嶏級
  const plain = s.replace(/\s+/g, '');
  const all = [...plain].filter(isHan);
  if (all.length === 1 && plain.length <= 2) return all[0];

  // 3) X鐨勬湰涔?/ X瀛?/ X鐨勮浆涔?/ X鐨勫瓧鏍规槸浠€涔?鈥?
  const m = plain.match(
    /^[^\p{Script=Han}]{0,4}(\p{Script=Han})(?:瀛??(?:鐨??(?:鏈箟|鏈京|鏈剰|瀛楁簮|瀛楀舰|鐢查鏂噟杞箟|杞夌京|寮曠敵涔墊寮曠敵|琛嶇敓瀛梶琛嶇敓|瀛楁棌|瀛楁牴|鎰忔€潀鍚箟)(?:鏄粈涔坾鏄暐|鏄摢浜泑鏈夊摢浜??$/u
  );
  if (m) return m[1];

  return null;
}

const CARD_SECTIONS = [
  { key: 'jielun', field: '缁撹', label: '缁撹' },
  { key: 'zigen', field: '瀛楁牴', label: '鍏堥噴瀛楁牴' },
  { key: 'benyi', field: '鏈箟', label: '鏈箟' },
  { key: 'zhuanyi', field: '杞箟', label: '杞箟' },
  { key: 'yansheng', field: '琛嶇敓', label: '琛嶇敓瀛椾箟' },
  { key: 'duizhao', field: '瀵圭収', label: '妯悜瀵圭収锛堟寜涔夌被鍒嗙粍锛? },
  { key: 'zixing', field: '瀛楀舰', label: '瀛楀舰' },
  { key: 'xiaojie', field: '灏忕粨', label: '涓€鍙ユ€荤粨' },
];

// 鍥哄畾鏍忓簭锛氱粨璁?鈫?鍒嗙骇 鈫?澹版瘝涔?鈫?鍏堥噴瀛楁牴 鈫?鏈箟 鈫?杞箟 鈫?琛嶇敓瀛椾箟 鈫?妯悜瀵圭収 鈫?瀛楀舰 鈫?涓€鍙ユ€荤粨
const CARD_ORDER = ['jielun', 'fenji', 'shengmu', 'zigen', 'benyi', 'zhuanyi', 'yansheng', 'duizhao', 'zixing', 'xiaojie', 'zuyu', 'other'];

let EXEGESIS_STYLE = "";
try {
  const { readFileSync } = await import("node:fs");
  EXEGESIS_STYLE = readFileSync(new URL("./prompts/exegesis.md", new URL("../", import.meta.url)), "utf8").trim();
} catch (e) { EXEGESIS_STYLE = ""; }
const CARD_PROMPT = `${EXEGESIS_STYLE ? "銆愰噴瀛楀洖绛斾綋渚嬶紙鍏辩敤瑙勮寖锛屽繀椤荤収姝ょ粍缁囩瓟妗堬級銆慭n" + EXEGESIS_STYLE + "\n\n" : ""}浣犳槸銆婄郴缁熸眽璇€嬪瓧鍗＄殑缂栬緫銆傚彧渚濇嵁涓嬮潰缁欏嚭鐨勭煡璇嗘潯鐩～鍐欏瓧鍗★紝鏉＄洰浠ュ鐨勫唴瀹逛竴涓瓧閮戒笉璁稿姞銆?

鍙緭鍑轰弗鏍?JSON锛屼笉瑕佷唬鐮佸潡鏍囪锛屼笉瑕佽В閲婏細
{"缁撹":"鈥?,"瀛楁牴":"鈥?,"鏈箟":"鈥?,"杞箟":"鈥?,"琛嶇敓":"鈥?,"瀵圭収":"鈥?,"瀛楀舰":"鈥?,"灏忕粨":"鈥?}
鏍忓簭涓庡啓娉曪紙鎸夋椤哄簭濉紝姣忔爮閮借鏈夊疄璐ㄥ唴瀹癸紝涓嶈涓€鍙ヨ瘽鎵撳彂锛夛細
- 姣忔爮鏈熬蹇呴』鏍囧嚭澶勶細鐢ㄤ笂闈㈡潯鐩殑缂栧彿鍐?[1]銆乕3]锛屼竴鏍忓紩澶氭潯灏辫繛鍐?[1][3]锛涙病鏈夌紪鍙风殑鍙ュ瓙浼氳涓㈠純銆?
- 缁撹锛氫笁鍒板洓鍙ワ紝鍏堣杩欎釜瀛楁槸浠€涔堝瓧銆佹湰涔夋槸浠€涔堛€佸瓧鏍圭粰瀹冨摢涓€闈箟锛岃浜轰笉璇讳笅鏂囦篃鎷垮埌绛旀銆?
- 瀛楁牴锛氬厛璁插瓧鏍硅嚜宸辩殑鏈箟锛堜竴銆佷簩銆佷笁绾у瓧鏍逛竴寰嬫湰涔夌洿閲婏紝涓嶄綔姣斿喌锛夛紝鍐嶈瀹冩€庝箞杩涘埌杩欎釜瀛楅噷锛涘０绗﹂摼鏈変袱绾т互涓婂氨閫愮骇璁层€?
- 鏈箟锛氬叚涔﹀垽璇紑澶达紝鐒跺悗鎶婃湰涔夎閫忥紙鏋勫舰銆佹墍鎸囦箣鐗┿€佸瓧涔︿緷鎹級锛屽啀鍒嗘潯鍒楀嚭寮曠敵璺緞銆?
- 杞箟锛氭寜寮曠敵璺緞鍒嗗眰鍐欙紝姣忓眰缁欏嚭瀛椾功渚濇嵁涓庝緥璇嶃€?
- 琛嶇敓锛氬瓧鏃忓瓧鎸変箟绫诲垎缁勫垪锛屾瘡缁勫啓銆屽瓧锛堝舰绗︼級钀界偣銆嶏紝閲嶈鑰呴檮涓€鍙ユ枃鍖栫敤娉曘€?
- 瀵圭収锛氭妸鏉＄洰閲屽凡鏈夌殑銆屾í鍚戝鐓э紙鎸変箟绫诲垎鈥︼級銆嶅師鍙ユ暣鐞嗘垚鍒嗙粍涓插啓锛屾寜 鈶犫憽鈶?鍒嗚锛涙病鏈夊鐓ф潗鏂欏氨鍐欍€屾殏鏃犮€嶃€?
- 瀛楀舰锛氳娓呯湅褰㈣鐐癸紙鏋勪欢浣嶇疆銆佷粠鏃╁埌鏅氱殑鍙樺寲锛夛紝涓嶈鍙姤瀛楀舰鏉ユ簮銆?
- 灏忕粨锛氫竴鍙ヨ瘽鏀舵嫝杩欎釜瀛楃殑澹扮缁欎箟銆佸舰绗﹀畾钀界偣鐨勫叧绯伙紝涓嶈閲嶅缁撹銆傜粨璁猴細涓夊埌鍥涘彞锛屽厛璇磋繖涓瓧鏄粈涔堝瓧銆佹湰涔夋槸浠€涔堛€佸瓧鏍圭粰瀹冨摢涓€闈箟锛岃浜轰笉璇讳笅鏂囦篃鎷垮埌绛旀銆?
- 瀵圭収锛氭妸鏉＄洰閲屽凡鏈夌殑銆屾í鍚戝鐓э紙鎸変箟绫诲垎鈥︼級銆嶅師鍙ユ暣鐞嗘垚鍒嗙粍涓插啓锛屾寜 鈶犫憽鈶?鍒嗚锛涚粍鍐呭啓銆屽瓧锛堝舰绗︼級钀界偣銆嶏紱娌℃湁瀵圭収鏉愭枡灏卞啓銆屾殏鏃犮€嶃€?
- 涓€鍙ユ€荤粨锛氫竴鍙ヨ瘽鏀舵嫝杩欎釜瀛楃殑澹扮缁欎箟銆佸舰绗﹀畾钀界偣鐨勫叧绯伙紝涓嶈閲嶅缁撹銆?

濉啓瑕佹眰锛?
0. 鍒嗙骇锛氬瓧鍗℃渶鍓嶉潰銆屽垎绾с€嶄竴鏍忕敱绯荤粺鎸夊叏涔︾粨鏋勫垽濂斤紙涓€绾у瓧鏍癸紳閮ㄥ悕锛涢儴鍐呰兘鍐嶆粙鐢熸柊瀛楄€呬负浜岀骇銆佷笁绾у瓧鏍癸紱鍏朵綑涓鸿皭澹板瓧锛夛紝浣犱笉寰楁敼鍔ㄣ€佷笉寰楀彟绔嬬骇鍒€傚～銆屽瓧鏍广€嶄竴鏍忔椂鍏堜氦浠ｈ瀛楀睘浜庡摢涓€绾с€佺敱鍝釜瀛楁牴琛嶇敓锛屽啀璁插瓧鏍逛箟濡備綍杩涘叆杩欎釜瀛椼€?
0b. 澹版瘝涔夛細璇ュ瓧鎵€灞為儴鐨勫０姣嶆嫙鎬佷箟涓庝竴鑷村害涔熺敱绯荤粺闄勪笂锛堛€屽０姣嶄箟銆嶄竴鏍忥級锛屼綘涓嶅緱鏀瑰啓銆佷笉寰楀彟鎷熷０姣嶄箟锛涜瀛楁牴鏃跺彲浠ュ紩鐢ㄥ畠鐨勭粨璁恒€傚紩鐢ㄦ椂蹇呴』鎶婅繖涓嫙鎬佷箟钀藉埌鏈瓧鎵€鎸囦箣鐗╀笂璁查€忥紙濡傘€岃幖銆嶅彧鍙?ch 鐨勩€屽埡銆嶏細鑺藉皷鍒虹牬鍦熷眰鑰屽嚭锛夛紝涓嶅緱鍙姤銆屾煇姣嶃€佹煇涔夈€佹煇涓€鑷村害銆嶄簡浜嬨€?*鎷熸€佷箟鏈槸鐩稿鐨勪袱闈紙t 娑傜獊銆乧h 鍒烘寔銆乴 鎷㈢鈥︼級锛岄噴涓€涓瓧涓€鑸彧璁插悎浜庡畠鐨勯偅涓€闈紝涓嶅繀涓ら潰閮借В璇?*锛涘彧鏈夊紩鐢抽摼纭疄妯法涓ら潰鏃舵墠鍐欎袱闈紙濡傘€屾煶銆嶇紪鏉熶负鎷€佹姌鍒负绂伙級銆?*涓嶅緱鍥犱竴鑷村害寮便€侀儴鍐呭垎姝с€佹垨璇ラ儴鏈敹鑰屾柇瑷€銆屼笌澹版瘝涔夋棤鍏炽€?*锛氬彜闊?zh銆乧h銆乻h 浠?d銆乼 鍒嗗寲锛岄娇闊充笌鑸岄煶鍚屾簮锛岄』寰０婧愬垎鍖栭摼璐€氳В閲婏紱纭疄鐩歌繚鏃朵篃瑕佽鏄庝负浣曠浉杩濓紙寮傝銆佸亣鍊熼煶銆佹柟瑷€锛夛紝涓嶈杞绘槗璇翠笉鐩稿叧銆?
1. 瀛楀舰锛氳瀛楀湪鐢查鏂囥€侀噾鏂囬噷鐨勫舰浣撳浣曡薄褰㈡垨鏋勫舰锛涙潯鐩病璁插瓧褰紝灏卞～绌哄瓧绗︿覆銆?
2. 瀛楁牴锛氳繖涓瓧鐢卞摢涓瓧鏍规瀯鎴愶紙鏉＄洰閲屻€屼粠鏌愪粠鏌愩€嶃€屼粠鏌愶紝鏌愬０銆嶈鐨勯偅涓瓧锛夛紝骞惰娓呭瓧鏍逛笌杩欎釜瀛楃殑鍏崇郴鈥斺€斾細鎰忚繕鏄舰澹般€佸瓧鏍圭殑鎰忎箟鎬庝箞杩涘埌杩欎釜瀛楅噷銆?*鍙栧瓧鏍逛箟鏃朵紭鍏堢敤瀛楁牴鐨勬湰涔夛紱鏈箟璁蹭笉閫氾紝鎵嶉檷涓€绾х敤杞箟**锛堝銆岀枤銆嶄粠涔咃紝涔呯殑鏈箟鏄伕鐏笺€佺伡鐥咃紝鏁呯枤锛濈伡鐥涗箣鐥咃紝涓嶅彲鍙栥€屼箙銆嶇殑寮曠敵涔夈€屾椂闂撮暱銆嶏紱瀛椾功銆岀枤锛屼箙涔熴€嶆槸澹拌锛屼笉鏄箟婧愶級銆?*澹版梺缁欎箟鐨勬柟寮忔槸姣斿柣锛岃鍐欐垚銆岃薄鈥︹€︿竴鏍枫€?*锛氱枤锛濊薄琚伕鐏间竴鏍风柤鐥涳紝鐜栵紳璞¤鐑х伡涓€鏍疯壊榛戯紱褰㈢鍙畾鍏剁被涓庤惤鐐广€?*浣嗘瘮鍠诲彧缁欍€屽舰鏃侊紜澹版梺銆嶇殑鍚堟垚璋愬０瀛楋紱瑙ｉ噴瀛楁牴鏈韩涓€寰嬫湰涔夌洿閲?*锛氳垎鐨勬湰涔夊氨鏄袱浜哄涓炬姮杞︿箣鐘讹紝杩界殑鏈箟灏辨槸璺熷湪灞佽偂鍚庨潰璺戔€斺€旇繖鏄洿閲婏紝涓嶆槸姣斿柣锛涜薄鎰忓吋澹板瓧锛堣溅锛嬭垇銆侀紟锛嬸Ε戯級鍚岀悊鍙鏄庡０鏃佸吋涔夛紝涓嶅銆岃薄鈥︹€︿竴鏍枫€嶃€?*澹扮閾炬湁涓ょ骇浠ヤ笂鏃讹紙濡?銧啋鍙扳啋濮嬨€佸寖鈫掓浄鈫掓复锛夛紝瑕侀€愮骇璇存槑姣忎竴绾у瓧鏍瑰悇缁欑殑鏄摢涓€闈箟锛屽啀钀藉埌杩欎釜瀛椾笂**鈥斺€斾笉鑳藉彧鍐欐渶鍚庝竴绾с€?***涓嶈杞绘槗鍒や綔銆岃薄澹般€佷笉鍙栦箟銆?*鈥斺€斿０鏃佸嚑涔庨兘鏈夊疄涔夛紝瀹炰箟涓庢瘮鍠讳箟涓ゅ眰骞跺瓨锛堝銆岃桨銆嶏紳涓夎溅璞℃剰浼楄溅锛屽疄涔夈€屼紬杞︺€嶏紝姣斿柣銆屽０澶у浼楄溅琛岄┒涔嬪０銆嶏級銆?*鑻ユ槸璋愬０瀛楋紝蹇呴』鍋氭í鍚戝鐓?*锛氬彇鏉＄洰閲屽悓澹扮鐨勫厔寮熷瓧鑷冲皯 3 涓紝鎸夈€屽瓧锝滃彇涔夐潰锝滃舰绗︼綔钀藉埌浠€涔堜箟銆嶆瘮杈冿紝璇存槑鍚屼竴鍙栦箟闈㈠湪涓嶅悓褰㈢涓嬫€庢牱钀藉埌涓嶅悓瀛椾箟锛屽啀瀹氳繖涓瓧鐨勮惤鐐癸紙濡傚惥閮細姊э紳鏈紜鐩稿鈫掓爲涓婁笅鐩稿綋锛屾櫎锛濇棩锛嬬浉瀵光啋浜虹浉瑙侊紝榧紳榧狅紜鐩稿鈫掗珮涓嬬浉瀵广€佸彧鑳戒粠楂樿荡涓嬶級銆?*瀵圭収瑕佽鐩栧叏鏃忋€佹寜涔夌被鍒嗚〃**锛氭妸鍏ㄦ棌鍏勫紵瀛楀厛鎸夋剰涔夊綊绫伙紙鍙栨湰涔夛紡鍙栬浆涔夛紡鍙€熷０锛夛紝姣忕被涓€寮犺〃锛屾渶鍚庢€绘敹銆屽０绗︾粰涔夈€佸舰绗﹀畾钀界偣銆嶏紝鍙€熷０閭ｄ竴绫讳篃瑕佸垪鍑猴紱鍙鐓х殑鍏勫紵瀛椾笉瓒?3 涓氨鍐欐槑銆屽彲瀵圭収鑰呬粎 N 瀛椼€嶃€?*鍚屼竴鍔ㄧ墿鏈夊紓鍚嶅紓浣撹€屽０绗︿笉鍚岃€呮洿鍙簰璇?*鈥斺€旈极浠庣煶锛堣薄鎺风煶涓嬭惤锛夛紝涓庨集鐨勯珮涓嬬浉瀵瑰悓鎸囥€岀敱楂樺悜涓嬫粦闄嶃€嶃€傚啓鎴愩€屽瓧鏍癸細璇存槑銆嶏紝渚嬪銆屽＋锛氫粫浠庝汉浠庡＋锛屽＋鏄煶婧愬瓧锛屾湰涔夋寚闆勬€э紝寮曠敵涓鸿涔︿汉銆佸畼鍛橈紝鎵€浠ャ€屼粫銆嶈〃浠讳簨銆佸涔犳斂浜嬨€嶃€傝嫢鏉＄洰鍒嗐€屽瓧鏍规潯鐩€嶅崟鍒楋紝鐢ㄥ畠浠鏄庡瓧鏍规湰韬殑鎰忎箟锛屽苟鍒嗗埆鏍囨敞鍑哄銆傚瓧鏍瑰繀椤绘槸鍙︿竴涓瓧锛屼笉鑳芥妸杩欎釜瀛楄嚜宸卞啓杩涘幓锛涙潯鐩彧璇村畠鏄€熼煶瀛椼€佹病鏈夋瀯褰㈠垎鏋愮殑锛屽～绌哄瓧绗︿覆銆?
3. 鏈箟锛?*寮€澶村繀椤诲厛鍐欎竴鍙ュ叚涔﹀垽璇紝鏍煎紡銆屽叚涔︼細鈥︹€︺€?*锛屽啀璁查€犲瓧涔嬪垵鐨勬剰涔夈€傚叚涔︾敤鐝浐鍚嶇洰锛屼笉鐢ㄣ€屽舰澹般€嶄竴璇嶃€傚垽娉曪紙鎸夋潯鐩師鏂囧垽鏂級锛氭潯鐩瀹冩槸銆岄煶婧愬瓧銆嶃€佹垨璇婚煶銆屾簮鑷€︹€﹀０銆嶏紳璞″０锛涙潯鐩銆屼粠鏌愪粠鏌愩€嶈€屼袱瀛楀悇鏈夌嫭绔嬫剰涔夛紳璞℃剰锛涙潯鐩銆屼粠鏌愶紝鏌愬０銆嶃€佹煇瀛楁槸澹版牴銆佽繖涓瓧鏄姞褰㈡梺鍒嗗寲鏉ョ殑锛濊浆娉紱鐙綋銆佸瓧褰㈠鐢伙紳璞″舰锛涘湪璞″舰瀛椾笂鍔犱竴涓棤涔夌鍙凤紳璞′簨锛涘洜涔夊€熷０锛濆亣鍊熴€傚鍚堢殑鐓х华璁哄叚绉嶇粍鍚堟姤锛屽銆岃薄鎰忥紜杞敞銆嶃€岃薄鎰忥紜璞″０銆嶃€傚彧瑕佹潯鐩噷鏈夈€屼粠鏌愬０銆嶃€岄煶婧愬瓧銆嶃€屼粠鏌愪粠鏌愩€嶈繖绫荤嚎绱㈠氨蹇呴』鍒わ紱涓€鏉＄嚎绱㈤兘娌℃湁鎵嶄笉鍐欏垽璇€傝嫢瀛楄〃鏋勫舰涔嬪鍙︽湁鏉＄洰璇村畠鏄€岄煶婧愬瓧銆嶃€佽闊炽€屾簮鑷€︹€﹀０銆嶏紝鍒よ瑕佸悎鎴愪袱鎴紙濡傘€岃薄鎰忥紜璞″０銆嶃€岃薄褰紜璞″０銆嶏級锛屼笉瑕佸彧鍐欐瀯褰㈤偅涓€鎴€?
4. 杞箟锛氬紩鐢充箟銆佸亣鍊熶箟銆?
5. 琛嶇敓锛氱敱瀹冨垎鍖栥€佸姞娉ㄥ舰鏃佹垨鐢ㄥ畠浣滃０绗︾殑瀛楋紝鍐欐垚銆屽瓧锛氭剰涔夛紱瀛楋細鎰忎箟銆嶏紝鏈€澶?6 涓瓧锛涙潯鐩噷璇淬€屽悓缁勩€嶃€屽睘鈥︹€︾被銆嶇殑閭ｄ簺瀛椾篃绠楋紝涓€涓兘鍒紡銆?
6. 姣忎釜闈炵┖瀛楁鏈熬蹇呴』甯?[clm_XXXXXXXX] 鍑哄锛堝瓧鏍广€佽鐢熶袱鏍忓挨鍏朵笉鑳芥紡锛夛紝id 鍙兘鍙栬嚜鏉＄洰鍒楄〃锛屼笉寰楃紪閫狅紝涓€涓瓧娈靛彲浠ュ甫澶氫釜銆?
7. 鏉＄洰閲屾病鏈変緷鎹殑瀛楁涓€寰嬭緭鍑虹┖瀛楃涓?""锛屼笉瑕佺敤浣犺嚜宸辩殑甯歌瘑琛ャ€?
8. 绠€浣撲腑鏂囷紝瀛楀舰銆佸瓧鏍广€佽浆涔夊悇涓嶈秴杩?130 瀛楋紝鏈箟锛堝惈鍏功涓€鍙ワ級涓嶈秴杩?170 瀛楋紝琛嶇敓涓嶈秴杩?150 瀛椼€俙;

function extractJson(text) {
  const s = String(text || '');
  const a = s.indexOf('{');
  const b = s.lastIndexOf('}');
  if (a < 0 || b <= a) return null;
  try {
    return JSON.parse(s.slice(a, b + 1));
  } catch {
    return null;
  }
}

// 鍙繚鐣欏嚭鑷潯鐩殑寮曠敤锛涙病鏈夋湁鏁堝紩鐢ㄧ殑涓€寰嬪垽涓恒€屾棤渚濇嵁銆?
// order 鏄笂涓嬫枃閲岀殑缂栧彿琛紝妯″瀷鍋锋噿鍐?[3] 涔熻兘鏄犲皠鍥?clm_ id
const LIUSHU_CORE = '(?:璞″舰|璞′簨|璞℃剰|璞″０|杞敞|鍋囧€?';
const LIUSHU_HEAD = new RegExp('^(' + LIUSHU_CORE + '(?:[锛?锛?]' + LIUSHU_CORE + ')*)([锛屻€傦細:\\s銆乚)');

// 鍏功鍒よ缁熶竴鎴愩€屽叚涔︼細鈥︹€︺€嶅紑澶达紙涓讳汉瀹氾細鏀惧湪鏈箟瑙ｉ噴閲屽ご锛屼笉鍗曞垪涓€鏍忥級
function ensureLiushu(sec) {
  if (!sec || !sec.text) return sec;
  const t = String(sec.text).trim();
  if (/^鍏功\s*[锛?]/.test(t)) return sec;
  if (!LIUSHU_HEAD.test(t)) return sec;
  return { ...sec, text: '鍏功锛? + t };
}

function sanitizeSection(raw, allowed, order) {
  let s = String(raw || '')
    .replace(/\r/g, '')
    .trim();
  if (!s) return null;
  const ids = [];
  s = s.replace(/[[銆怾\s*(clm_[0-9A-Fa-f]{20,40})\s*[\]銆慮/g, (m, id) => {
    const up = 'clm_' + id.slice(4).toUpperCase();
    if (!allowed.has(up)) return '';
    ids.push(up);
    return `[${up}]`;
  });
  s = s.replace(/[[銆怾\s*(\d{1,2})\s*[\]銆慮/g, (m, n) => {
    const id = Array.isArray(order) ? order[Number(n) - 1] : null;
    if (!id || !allowed.has(id) || ids.includes(id)) return '';
    ids.push(id);
    return `[${id}]`;
  });
  s = s
    .replace(/\*\*/g, '')
    .replace(/[ \t]+/g, ' ')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
  if (!ids.length) return null;
  return { text: s, cites: [...new Set(ids)] };
}

function briefOf(claim) {
  const blocks = String(claim.statement || '')
    .split(/\n{2,}/)
    .map((x) => x.replace(/^#{1,6}\s*/gm, '').trim())
    .filter(Boolean);
  const body = blocks.find((x) => !/^(閫傜敤杈圭晫|杈圭晫)/.test(x)) || '';
  const one = body.split('\n')[0].trim();
  if (!one || one.length > 100) return '';
  if (one === String(claim.title || '').trim()) return '';
  return one;
}

// 娌℃湁妯″瀷锛堟垨妯″瀷澶辫触锛夋椂鐨勭‘瀹氭€у瓧鍗★細鎸夋潯鐩師鏂囧綊绫?
// 瀛楁牴涓€鏍忎笉鍦ㄨ繖閲屽垎妗讹紝鐢?zigenFallback() 鍗曠嫭鎷硷紝閬垮厤鍑虹幇涓や釜銆屽瓧鏍广€?

function dedupeSections(sections) {
  const norm = (s) => String(s || '').replace(/\[clm_[0-9A-F]+\]/g, '').replace(/[\s锛屻€傦紱锛氥€?'锛堬級()銆愩€慮/g, '');
  const grams = (s) => { const n = norm(s); const g = new Set(); for (let i = 0; i < n.length - 1; i++) g.add(n.slice(i, i + 2)); return g; };
  const jac = (a, b) => { if (!a.size || !b.size) return 0; let inter = 0; for (const x of a) if (b.has(x)) inter++; return inter / (a.size + b.size - inter); };
  const kept = [];
  for (const s of sections || []) {
    if (!s || !s.text || !String(s.text).trim()) continue;
    const g = grams(s.text);
    const dup = kept.some((k) => jac(g, k.g) >= 0.62);
    if (dup) continue;
    kept.push({ ...s, g });
  }
  return kept.map(({ g, ...rest }) => rest);
}

function fallbackSections(claims, ch) {
  const defs = CARD_SECTIONS.filter((d) => !['zigen', 'jielun', 'duizhao', 'xiaojie'].includes(d.key));
  const buckets = new Map(defs.map((s) => [s.key, []]));
  const other = [];
  for (const c of claims) {
    const hay = `${c.title}\n${c.statement || ''}`;
    if (/鏈箟|鏈京|鍒濇枃|璞″舰|璞\s\S]{0,6}褰瀛楀舰/.test(hay)) buckets.get('benyi').push(c);
    else if (/寮曠敵|杞夌京|杞箟|鍋囧€焲鍊熼煶|鍊熷０/.test(hay)) buckets.get('zhuanyi').push(c);
    else if (/瀛楁棌|琛嶇敓|鍒嗗寲|浠嶽\s\S]{0,4}[澹拌伈]/.test(hay)) buckets.get('yansheng').push(c);
    else other.push(c);
  }
  const used = new Set();
  const secs = defs.map((def) => {
    const list = buckets.get(def.key);
    if (!list.length) return { key: def.key, label: def.label, missing: true };
    list.forEach((c) => used.add(c.id));
    const text = list
      .map((c) => `**${c.title}** [${c.id}]` + (briefOf(c) ? `\n${briefOf(c)}` : ''))
      .join('\n\n');
    return { key: def.key, label: def.label, text, cites: list.map((c) => c.id) };
  });
  const rest = other.filter((c) => !used.has(c.id));
  if (rest.length) {
    secs.push({
      key: 'other',
      label: '鍏朵粬鐩稿叧鏉＄洰',
      text: rest.map((c) => `**${c.title}** [${c.id}]`).join('\n\n'),
      cites: rest.map((c) => c.id),
    });
  }

  // 缁撹锛氭妸杩欎釜瀛楄嚜宸辩殑鏈箟鏉＄殑绗竴鍙ユ彁鍑烘潵锛屼笉璇讳笅鏂囦篃鑳藉緱鍒扮瓟妗?
  const bc = claims.find((c) => String(c.title || '').startsWith(ch)) || null;
  if (bc) {
    const body = String(bc.statement || '')
      .split('#### 閫傜敤杈圭晫')[0]
      .replace(/^#+\s*/gm, '')
      .replace(/^\s*[^\n锛?]{0,30}[锛?]\s*(?=\S)/m, '')
      .replace(/\s+/g, ' ')
      .trim();
    const first = (body.split(/(?<=[銆傦紱])/)[0] || body).slice(0, 130);
    if (first) secs.unshift({ key: 'jielun', label: '缁撹', text: first, cites: [bc.id] });
  }
  // 妯悜瀵圭収锛氭潯鐩鏂囬噷宸茬粡鍐欏ソ鐨勩€屾í鍚戝鐓э紙鈥︼級銆嶅師鍙ワ紝鎽樺嚭鏉ュ崟鐙垚鏍?
  const dz = [];
  for (const c of claims) {
    const m = String(c.statement || '').match(/妯悜瀵圭収锛圼^锛塢*锛夛細[^\n]+/);
    if (m) dz.push(m[0].trim());
  }
  if (dz.length) {
    secs.push({ key: 'duizhao', label: '妯悜瀵圭収锛堟寜涔夌被鍒嗙粍锛?, text: dz.slice(0, 3).join('\n\n') });
  }
  return secs;
}

// 鎸夊瓧妫€绱細浼樺厛鍙栨爣棰?姝ｆ枃閲岀湡鐨勫嚭鐜拌繖涓瓧鐨勬潯鐩?
async function retrieveForChar(ch) {
  const res = await pkc(['query', ch, '12']);
  const hits = (res.results || [])
    .filter((r) => r.kind === 'claim' && r.permission === 'public' && r.lifecycle === 'active')
    .slice(0, 12);
  const claims = (await hydrate(hits)).filter(Boolean);
  const direct = claims.filter((c) => `${c.title}\n${c.statement || ''}`.includes(ch));
  return { hits, claims, direct };
}

// 浠庢潯鐩噷鐨勩€屼粠鏌愪粠鏌愩€嶃€屼粠鏌愶紝鏌愬０銆嶆壘鍑鸿繖涓瓧鐨勬瀯瀛楁垚鍒嗭紙鍊欓€夊瓧鏍癸級
const COMP_RE = /浠嶽銆屻€庘€?']?([\p{Script=Han}])[銆嶃€忊€?']?/gu;
const SHENG_RE = /[銆屻€庘€?']?([\p{Script=Han}])[銆嶃€忊€?']?[澹拌伈]/gu;

function rootsOf(ch, claims) {
  const out = new Map();
  const esc = ch.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  // 銆孹銆嶁€︿粠锛氳姹傘€屼粠銆嶇揣璺熷湪杩欎釜瀛椾箣鍚庯紝閬垮厤鎶婂埆浜虹殑鏋勫舰绠楀埌瀹冨ご涓?
  const lead = new RegExp(`銆?${esc}銆?[^銆傦紱;\\n]{0,14}?浠巂, 'u');
  for (const c of claims) {
    const text = `${c.title}\n${c.statement || ''}`;
    if (text.includes(`${ch}鏄煶婧愬瓧`)) continue; // 鑷繁灏辨槸闊虫簮瀛楋紝娌℃湁鏇翠笂浣嶇殑瀛楁牴
    if (/涓嶇‘|涓嶇⒑|鏋愬舰涓嶇‘|璇瘄瑾?.test(text)) continue; // 鏉＄洰鑷繁璇磋繖绉嶆瀽褰㈤潬涓嶄綇锛屼笉閲?
    for (const sent of text.split(/[銆傦紱;\n]/)) {
      if (!lead.test(sent)) continue;
      for (const re of [COMP_RE, SHENG_RE]) {
        for (const m of sent.matchAll(re)) {
          const r = m[1];
          if (r !== ch && !out.has(r)) out.set(r, c);
        }
      }
    }
  }
  return out;
}

// 浼樺厛鍙栥€岀煡璇嗗簱閲岃嚜宸辨湁涓婚锛圶閮級銆嶆垨銆屾潯鐩嚜绉伴煶婧愬瓧銆嶇殑閭ｄ釜鎴愬垎褰撳瓧鏍?
async function findRoot(ch, direct) {
  const cands = rootsOf(ch, direct);
  if (!cands.size) return null;
  const titles = [];
  try {
    const tree = await getTree();
    for (const n of tree.nodes || []) for (const t of n.topics || []) titles.push(String(t.title || ''));
  } catch {}
  const list = [...cands.entries()].map(([root, claim]) => {
    const hay = `${claim.title}\n${claim.statement || ''}`;
    return {
      root,
      claim,
      byTopic: titles.some((t) => t.includes(root)),
      byYinyuan: hay.includes('闊虫簮瀛?) && hay.includes(`銆?{root}銆峘),
    };
  });
  return list.find((x) => x.byTopic) || list.find((x) => x.byYinyuan) || null;
}

// 杩欎釜瀛楄兘涓嶈兘鍐嶆粙鐢熸柊瀛楋紙鍒や簩绾?涓夌骇瀛楁牴鐨勪緷鎹級锛氭潯鐩噷瀹冧綔澹扮锛屾垨鑷О闊虫簮瀛?
function spawnsFrom(ch, claims) {
  if (!ch) return false;
  const esc = ch.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const reFrom = new RegExp(`浠嶽^銆傦紱\\n]{0,8}${esc}[澹拌伈]`, 'u');
  for (const c of claims) {
    const t = `${c.title}\n${c.statement || ''}`;
    if (String(c.title || '').startsWith(`${ch}閮╜)) return true; // 鏈夎嚜宸辩殑銆孹閮ㄣ€嶅瓧鏃忔潯鐩?
    if (t.includes(`${ch}鏄煶婧愬瓧`) || t.includes(`銆?{ch}銆嶆槸闊虫簮瀛梎)) return true;
    if (reFrom.test(t)) return true;
  }
  return false;
}

// 寮備綋鎴栭毝鍙樺啓娉曪紙濡傘€屼互銆嶄箣浜庛€屻牤銆嶏級锛氬悓灞炰竴閮紝鎸変竴绾у瓧鏍圭湅寰?
function variantOf(ch, claims, z) {
  const esc = ch.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  for (const c of claims) {
    const title = String(c.title || '');
    const m = title.match(/^([\p{Script=Han}])閮╗锛?]/u);
    if (!m || !z.byName || !z.byName[m[1]]) continue;
    const escRoot = m[1].replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    if (new RegExp(`${escRoot}锛?{esc}锛塦, 'u').test(title)) return m[1];
  }
  return null;
}

// 銆孹閮細瀛楁棌鈥︺€嶈繖绫绘潯鐩妸璋愬０瀛楁寜瀛楁棌褰掑爢锛屾槸銆屼粠鏌愬０銆嶄箣澶栫殑绗簩鏉″垽绾х嚎绱?
function familyOf(ch, claims) {
  for (const c of claims) {
    const title = String(c.title || '');
    const m = title.match(/^([\p{Script=Han}])閮╗锛?]/u);
    if (!m || m[1] === ch) continue;
    if (!/瀛楁棌|琛嶇敓|璋愬０/.test(title)) continue;
    if (`${title}\n${c.statement || ''}`.includes(ch)) return { root: m[1], claim: c };
  }
  return null;
}

// 鍒ょ骇锛堥噴瀛楃涓€姝ワ級锛氫竴绾у瓧鏍癸紳609 閮ㄧ殑閮ㄩ瀛楋紱閮ㄥ唴琛嶇敓瀛楁寜鑳藉惁鍐嶆粙鐢熷垎浜岀骇銆佷笁绾у瓧鏍癸紝
// 涓嶈兘鍐嶆粙鐢熻€呬负璋愬０瀛椼€傚０绗﹂摼鏈€澶氫笂婧袱灞傦紝澶熻鐩栥€屻牤鈫掑彴鈫掑銆嶈繖绫荤粨鏋勩€?
// ---------- 澹版瘝涔夛紙鍒嗛儴涓婚锛?---------
// 涓€閮ㄤ竴鏉★紝鐢?pkc 鐢熸垚鍒?knowledge/hanzi-yinyuan/02z-shengmu-yi.md锛岃繖閲岀洿鎺ヨ璇ヤ富棰樻枃浠?
const SM_DOC = join(ROOT, 'knowledge', 'hanzi-yinyuan', '02z-shengmu-yi.md');
let smCache = { at: 0, byRoot: new Map(), byZi: new Map(), zero: null };

async function shengmuIndex() {
  if (smCache.byRoot.size && Date.now() - smCache.at < 300_000) return smCache;
  const byRoot = new Map();
  const byZi = new Map();
  let zero = null;
  try {
    const text = await readFile(SM_DOC, 'utf8');
    const re = /<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### (.+?)\n([\s\S]*?)<!-- CLAIM:END/g;
    for (const m of text.matchAll(re)) {
      const id = m[1];
      const title = m[2].trim();
      const body = m[3].split('#### 閫傜敤杈圭晫')[0].trim();
      const hit = title.match(/^(.+?)閮細澹版瘝涔?u);
      const sub = title.match(/^(.+?)锛堜簩绾у瓧鏍癸級锛氬０姣嶄箟/u);
      if (hit) byRoot.set(hit[1], { id, text: body });
      else if (sub) byZi.set(sub[1], { id, text: body });
      else if (title.startsWith('闆跺０姣嶈閮?)) zero = { id, text: body };
    }
  } catch (e) {
    log('璇诲０姣嶄箟涓婚澶辫触:', e.message);
  }
  smCache = { at: Date.now(), byRoot, byZi, zero };
  return smCache;
}

async function shengmuOf(ch, chain) {
  if (!ch && !(chain && chain.length)) return null;
  const idx = await shengmuIndex();
  // 澹扮閾剧敱杩滃強杩戯紝鏈熬鍐嶅甫涓婃湰瀛楋細鍏堟壘銆岃皝鑷繁鏈夌嫭绔嬪０姣嶄箟鏉°€嶏紝
  // 渚嬪銆屽銆嶄粠鍙板０锛岃鐢ㄣ€屽彴銆嶆潯锛堜笁璇讳笉绯伙級鑰屼笉鏄牤閮ㄧ殑闆跺０姣嶆潯銆?
  const list = [...(chain && chain.length ? chain : []), ch].filter(Boolean);
  for (let i = list.length - 1; i >= 0; i -= 1) {
    const own = idx.byZi.get(list[i]);
    if (own) return { claim: own.id, text: own.text };
  }
  const root = list[0] || ch;
  const hit = idx.byRoot.get(root);
  if (hit) return { claim: hit.id, text: hit.text };
  if (idx.zero && idx.zero.text.includes(`銆?{root}閮ㄣ€峘)) {
    return {
      claim: idx.zero.id,
      text: `${root}閮ㄨ闆跺０姣嶏紱缁涓冪粍澹版瘝鏈垪闆跺０姣嶏紝鏁呬笉绯绘嫙鎬佸０姣嶄箟锛岃閮ㄩ噴涔夐潬涔夌被涓庡瓧褰€俙,
    };
  }
  return null;
}

// 娌℃湁鐙珛鏉＄洰鐨勫瓧锛堝銆岄妧銆嶃€屾捣銆嶃€岃幖銆嶏級锛氬埌瀛楁棌鏉￠噷鎵惧畠琚В閲婄殑閭ｄ竴鏉★紝鏁存浣滀负銆屽瓧鏃忔潯鐩€嶆爮
let claimIdxCache = null;
function claimIdx() {
  if (claimIdxCache) return claimIdxCache;
  try {
    claimIdxCache = JSON.parse(readFileSync(join(PUBLIC, 'claims-index.json'), 'utf8'));
  } catch (e) {
    claimIdxCache = { byChar: {} };
  }
  return claimIdxCache;
}

async function familyClaimFor(ch) {
  const alt = loadVariantMap()[ch];
  const chars = [ch, alt].filter(Boolean);
  const idx = claimIdx();
  const seen = new Set();
  for (const c of chars) {
    const hits = (idx.byChar || {})[c] || [];
    for (const h of hits) {
      if (seen.has(h.claim)) continue;
      seen.add(h.claim);
      if (!/瀛楁棌|閮╗锛?]/.test(h.title || '')) continue;
      let cl = null;
      try {
        cl = JSON.parse(await pkc(['show-claim', h.claim, '--format', 'json'])).claim;
      } catch (e) {
        continue;
      }
      if (!cl || !cl.statement) continue;
      const text = String(cl.statement).split('#### 閫傜敤杈圭晫')[0].trim();
      if (!text) continue;
      if (!chars.some((x) => text.includes(x))) continue;
      return { claim: cl.id, title: cl.title, text };
    }
  }
  return null;
}

async function levelOf(ch, direct) {
  const z = loadZigenIndex();
  // 鍘熺鎸夌箒浣撶珛瀛楀ご锛岀敤鎴峰鎸夌畝浣撴彁闂細鍏堟槧灏勫埌绻佷綋鍐嶅垽绾э紝
  // 鍚﹀垯 zigen.json / 瀛楀舰搴撴煡涓嶅埌閿紝鍒嗙骇鏍忓氨绌轰簡銆?
  const aliasCh = variantOf(ch);
  if (aliasCh && aliasCh !== ch) ch = aliasCh;
  const bu = z.byName && z.byName[ch];
  if (bu) {
    return {
      level: '涓€绾у瓧鏍?,
      text: `涓€绾у瓧鏍癸細銆?{ch}銆嶆槸绗?${bu.no} 閮ㄣ€?{ch}閮ㄣ€嶇殑閮ㄩ瀛楋紝灞炲嵎${juanCn(bu.juanNo)}銆?{bu.juanName}銆嶏紙p${bu.p}锛夈€傞儴鍗冲瓧鏍癸紱鍏ㄤ功 609 閮ㄤ腑绗?23閮ㄥ師缂恒€佺554閮ㄩ儴棣栧瓧鏈兘杞綍锛屽叾浣?608 閮ㄥ嵆涓€绾у瓧鏍广€俙,
      cites: [bu.claim],
      chainChars: [ch],
    };
  }
  if (!direct || !direct.length) return null;
  const variant = variantOf(ch, direct, z);
  if (variant) {
    const bv = z.byName[variant];
    return {
      level: '涓€绾у瓧鏍?,
      text: `涓€绾у瓧鏍癸細銆?{ch}銆嶆槸銆?{variant}銆嶇殑寮備綋鎴栭毝鍙樺啓娉曪紝鍚屽睘绗?${bv.no} 閮ㄣ€?{variant}閮ㄣ€嶏紙鍗?{juanCn(bv.juanNo)}銆?{bv.juanName}銆嶏級锛屾寜閮ㄩ瀛楃湅寰呫€俙,
      cites: direct.filter((c) => String(c.title || '').startsWith(`${variant}閮╜)).map((c) => c.id),
      chainChars: [variant],
    };
  }
  let r1 = await findRoot(ch, direct);
  if (!r1) {
    const fam = familyOf(ch, direct);
    if (fam) r1 = fam;
  }
  if (!r1) return null;
  const spawn = spawnsFrom(ch, direct);
  let root = r1.root;
  let via = null;
  let depth = 1;
  if (!z.byName || !z.byName[root]) {
    via = root;
    try {
      const rr = await retrieveForChar(root);
      const r2 = await findRoot(root, rr.direct);
      if (r2 && z.byName && z.byName[r2.root]) {
        root = r2.root;
        depth = 2;
      }
    } catch {}
  }
  // 寮備綋鎴栭毝鍙樺啓娉曪紙濡傘€屼互銆嶄箣浜庛€屻牤銆嶏級锛氭寜涓€绾у瓧鏍圭湅寰咃紝涓嶉檷绾?
  const alias = direct.some((c) => {
    const t = `${c.title}\n${c.statement || ''}`;
    return t.includes(ch) && t.includes(root) && /(闅朵綔|闅镐綔|鍏变竴瀛梶寮備綋|鐣伴珨|鎴栦綔|鍙ゅ瓧|鍚屽瓧)/.test(t);
  });
  const bu2 = z.byName && z.byName[root];
  const where = bu2
    ? `绗?${bu2.no} 閮ㄣ€?{root}閮ㄣ€嶏紙鍗?{juanCn(bu2.juanNo)}銆?{bu2.juanName}銆嶏級`
    : `銆?{root}銆峘;
  const chain = depth === 2 ? `銆?{root}銆嶁啋銆?{via}銆嶁啋銆?{ch}銆峘 : `銆?{root}銆嶁啋銆?{ch}銆峘;
  const cites = [r1.claim.id];
  if (depth === 1 && alias && bu2) {
    return {
      level: '涓€绾у瓧鏍?,
      text: `涓€绾у瓧鏍癸細銆?{ch}銆嶆槸銆?{root}銆嶇殑寮備綋鎴栭毝鍙樺啓娉曪紝鍚屽睘${where}锛屾寜閮ㄩ瀛楃湅寰呫€俙,
      cites,
      chainChars: [root],
    };
  }
  if (depth === 1) {
    if (spawn) {
      return {
        level: '浜岀骇瀛楁牴',
        text: `浜岀骇瀛楁牴锛氥€?{ch}銆嶄粠${where}鐨勩€?{root}銆嶅緱澹版瀯褰紙${chain}锛夛紱瀹冨湪閮ㄥ唴杩樿兘婊嬬敓鏂板瓧锛屾晠涓轰簩绾у瓧鏍广€俙,
        cites,
        chainChars: [root],
      };
    }
    return {
      level: '璋愬０瀛?,
      text: `璋愬０瀛楋細銆?{ch}銆嶄粠${where}鐨勩€?{root}銆嶅緱涔夊緱澹帮紙${chain}锛夛紱鑷韩涓嶅啀婊嬬敓鏂板瓧锛屽睘璇ラ儴鏈璋愬０瀛椼€俙,
      cites,
      chainChars: [root],
    };
  }
  if (spawn) {
    return {
      level: '涓夌骇瀛楁牴',
      text: `涓夌骇瀛楁牴锛氥€?{ch}銆嶄笉鍦ㄩ儴鐩笂锛屽０绗﹂摼涓?{chain}锛屾簮澶存槸${where}锛涘畠鍦ㄤ簩绾у瓧鏍逛箣涓嬭繕鑳芥粙鐢熸柊瀛楋紝鏁呬负涓夌骇瀛楁牴銆俙,
      cites,
      chainChars: [root, via],
    };
  }
  return {
    level: '璋愬０瀛?,
    text: `璋愬０瀛楋細銆?{ch}銆嶇殑澹扮閾句负${chain}锛屾簮澶存槸${where}锛涜嚜韬笉鍐嶆粙鐢熸柊瀛楋紝灞為儴鍐呬笁绾т互涓嬬殑璋愬０瀛椼€俙,
    cites,
    chainChars: [root, via],
  };
}

// 瀛楁潯鐩?+ 瀛楁牴鏉＄洰鍒嗕袱缁勭紪鍙凤紝妯″瀷鎵嶈兘鍒嗘竻鍝彞鍦ㄨ瀛楁牴
// 杩斿洖涓婁笅鏂囦笌銆岀紪鍙?鈫?鏉＄洰 id銆嶇殑瀵圭収锛屾ā鍨嬪彧鍐?[3] 杩欑缂栧彿鏃朵篃鑳借拷鍥炴潵
function cardContext(ch, direct, root, rootClaims) {
  const order = [];
  const block = (claims) =>
    claims
      .map((c) => {
        order.push(c.id);
        const body = String(c.statement || '').replace(/\r\n/g, '\n').trim();
        return `[${order.length}] ${c.id} 銆?{c.title}銆媆n鑺傜偣/涓婚锛?{c.node_id} / ${c.topic_id}\n姝ｆ枃锛歕n${body}`;
      })
      .join('\n\n---\n\n');
  const parts = [`銆?{ch}銆嶇殑鏉＄洰锛歕n\n${block(direct)}`];
  if (root && rootClaims.length) {
    parts.push(`瀛楁牴銆?{root}銆嶇殑鏉＄洰锛堢敤鏉ヨ鏄庡瓧鏍规湰韬殑鎰忎箟锛夛細\n\n${block(rootClaims)}`);
  }
  return { context: parts.join('\n\n====\n\n'), order };
}

// 娌℃湁妯″瀷鏃讹紝瀛楁牴涓€鏍忓彧鐢ㄦ潯鐩師鏂囨嫾
function zigenFallback(info, rootClaims) {
  const { root, claim } = info;
  const body = briefOf(claim);
  if (!body && !rootClaims.length) return null;
  const lines = [`瀛楁牴锛?{root}`];
  if (body) lines.push(body);
  for (const c of rootClaims.slice(0, 4)) {
    const b = briefOf(c);
    lines.push(`**${c.title}** [${c.id}]` + (b ? `\n${b}` : ''));
  }
  return {
    key: 'zigen',
    label: '瀛楁牴',
    text: lines.join('\n\n'),
    cites: [claim.id, ...rootClaims.slice(0, 4).map((c) => c.id)],
  };
}

async function askModelForCard(ch, question, context, meter) {
  const messages = [
    { role: 'system', content: CARD_PROMPT },
    { role: 'user', content: `瀛楋細${ch}\n鐢ㄦ埛闂锛?{question}\n\n鐭ヨ瘑鏉＄洰锛歕n\n${context}` },
  ];
  const r = await fetch(`${BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: { 'content-type': 'application/json', authorization: `Bearer ${API_KEY}` },
    body: JSON.stringify({ model: MODEL, messages, stream: false, temperature: 0.2, max_tokens: 1800 }),
    signal: AbortSignal.timeout(45_000),
  });
  if (!r.ok) {
    const d = await r.text().catch(() => '');
    throw new Error(`妯″瀷杩斿洖 ${r.status}锛?{d.slice(0, 200)}`);
  }
  const j = await r.json();
  const content = j.choices && j.choices[0] && j.choices[0].message ? j.choices[0].message.content : '';
  if (meter) {
    const c = usageCost(j.usage, CARD_PROMPT.length + context.length + 60, String(content || '').length);
    meter.yuan += c.yuan;
    meter.inTok += c.inTok;
    meter.outTok += c.outTok;
    log(`瀛楀崱鎴愭湰 ${c.yuan} 鍏冿紙鍏?${c.inTok} / 鍑?${c.outTok} token锛塦);
  }
  log('瀛楀崱妯″瀷鍘熸枃:', String(content || '').replace(/\s+/g, ' ').slice(0, 400));
  return extractJson(content);
}

const CARD_DIR = join(PUBLIC, 'cards');
const presetCache = new Map();

// 鍒悕 鈫?鍗℃枃浠跺悕锛堢敱 cards/alias-index.json 鎻愪緵锛宐uild_card_alias_index 鐢熸垚锛夈€?
const ALIAS_FILE = join(CARD_DIR, 'alias-index.json');
let aliasCache = { at: 0, map: {} };
function loadAliasMap() {
  if (aliasCache.at && Date.now() - aliasCache.at < 300_000) return aliasCache.map;
  try {
    const map = JSON.parse(readFileSync(ALIAS_FILE, 'utf8'));
    aliasCache = { at: Date.now(), map };
    return map;
  } catch {
    return {};
  }
}
function aliasOf(ch) {
  const m = loadAliasMap();
  return m[ch] || '';
}

function sanitizeCard(d) {
  // 瀛楁棌琛岄蹇呴』鏄竴涓眽瀛楋紱鍥炬敞娈嬭锛堛€屸柌鈥︺€嶇瓑锛変竴寰嬩涪寮冿紝閬垮厤鍑虹幇鍦ㄥ瓧鏃?chips 閲?
  const HAN = /^\p{Script=Han}$/u;
  for (const s of (d.sections || [])) {
    if (!s || s.key !== 'zizu' || !Array.isArray(s.groups)) continue;
    for (const g of s.groups) {
      if (!g || !Array.isArray(g.rows)) continue;
      g.rows = g.rows.filter((r) => Array.isArray(r) && typeof r[0] === 'string' && HAN.test(r[0].trim().replace(/锛圼^锛塢*锛?/, '')));
    }
  }
  return d;
}

function loadPresetCard(ch) {
  const alias = variantOf(ch) || ch;
  const names = [ch, alias, aliasOf(ch)].filter(Boolean);
  for (const key of new Set(names)) {
    const p = join(CARD_DIR, key + '.json');
    try { if (existsSync(p)) return sanitizeCard(JSON.parse(readFileSync(p, 'utf8'))); } catch (e) { log('瀛楀崱璇诲彇澶辫触', key, e.message); }
  }
  return null;
}

async function handleCard(emit, res, question, ch, ip, meter) {
  let glyph = glyphInfo(ch);
  const preset = loadPresetCard(ch);
  if (preset) {
    emit({ type: 'card', card: { char: ch, mode: 'preset', head: preset.head || ch, pinyin: preset.pinyin || '', level: preset.level || null, parent: preset.parent || null, bus: preset.bus || [], aliases: preset.aliases || [], sections: preset.sections || [], glyph, photos: (glyph || {}).photos || [], roots: [] } });
    return res.end();
  }
  let glyphFrom = null;
  emit({ type: 'card-start', char: ch, glyph: null });

  let evidence;
  try {
    evidence = await retrieveForChar(ch);
  } catch (e) {
    log('瀛楀崱妫€绱㈠け璐?', e.message);
    emit({ type: 'error', message: '妫€绱㈠嚭閿欙紝璇风◢鍚庡啀璇曘€? });
    return res.end();
  }

  emit({
    type: 'sources',
    items: evidence.hits.map((h) => ({
      id: h.id,
      title: h.title,
      topic_id: h.topic_id,
      node_id: h.node_id,
      score: h.score,
    })),
  });

  const direct = evidence.direct;
  const allowed = new Set(direct.map((c) => c.id));
  let sections = null;
  let mode = 'none';
  let note = '';

  // 瀛楁牴锛氫粠銆屼粠浜轰粠澹€嶈繖绫绘潯鐩噷鎵撅紝鍐嶆妸瀛楁牴鑷繁鐨勬潯鐩篃鍙栨潵褰撹瘉鎹?
  let rootInfo = null;
  let rootClaims = [];
  if (direct.length) {
    try {
      rootInfo = await findRoot(ch, direct);
    } catch (e) {
      log('瀛楁牴璇嗗埆澶辫触:', e.message);
    }
    if (rootInfo) {
      try {
        const rr = await retrieveForChar(rootInfo.root);
        rootClaims = rr.direct.filter((c) => !allowed.has(c.id)).slice(0, 6);
        for (const c of rootClaims) allowed.add(c.id);
      } catch (e) {
        log('瀛楁牴妫€绱㈠け璐?', e.message);
      }
    }
  }

  // 杩欎釜瀛楀湪鍘熺閲屾病鏈夌嫭绔嬬殑瀛楀舰琛岋紙鍙槸瀛楁棌鎴愬憳锛夋椂锛岄€€涓€姝ョ敤瀛楁牴鐨勫瓧褰笌閰嶅浘
  if (!glyph && rootInfo && !d.noRoot) {
    const g = glyphInfo(rootInfo.root);
    if (g) {
      glyph = g;
      glyphFrom = rootInfo.root;
    }
  }

  if (!direct.length) {
    note = `鐭ヨ瘑搴撻噷杩樻病鏈夈€?{ch}銆嶇殑涓撻棬鏉＄洰銆傚瓧褰㈠浘鍙栬嚜銆婄郴缁熸眽璇€嬪師绋匡紝鍙互鍏堢湅褰綋锛涘瓧涔夋潯鐩繕鍦ㄥ綍鍏ワ紝鏆備笉鎺ㄦ柇銆俙;
  } else if (MODE === 'model') {
    try {
      const ctx = cardContext(ch, direct, rootInfo && rootInfo.root, rootClaims);
      const obj = await askModelForCard(ch, question, ctx.context, meter);
      if (obj) {
        const built = CARD_SECTIONS.map((def) => {
          const raw = obj[def.field] ?? obj[def.label] ?? obj[def.key];
          let sec = sanitizeSection(raw, allowed, ctx.order);
          if (sec) sec = { key: def.key, label: def.label, ...sec };
          if (sec && def.key === 'benyi') sec = ensureLiushu(sec);
          return sec || { key: def.key, label: def.label, missing: true };
        });
        if (built.some((s) => !s.missing)) {
          sections = built;
          mode = 'model';
        }
      }
    } catch (e) {
      log('瀛楀崱妯″瀷璋冪敤澶辫触:', e.message);
    }
  }

  if (!sections && direct.length) {
    sections = fallbackSections(direct, ch);
    mode = 'fallback';
    if (rootInfo) {
      const zi = zigenFallback(rootInfo, rootClaims);
      if (zi) {
        const i = sections.findIndex((s) => s.key === 'zixing');
        sections.splice(i >= 0 ? i + 1 : 0, 0, zi);
      }
    }
  }
  if (!sections) sections = [];

  // 杩欎釜瀛楁病鏈夌嫭绔嬫潯鐩椂锛屾妸瑙ｉ噴瀹冪殑閭ｆ潯瀛楁棌鏁存闄勪笂锛堢綉椤典篃鐪嬪緱鍒伴噴瀛楁椂鐢ㄧ殑鍘熸枃锛?
  if (!direct.length) {
    try {
      const fam = await familyClaimFor(ch);
      if (fam) {
        sections.push({ key: 'zuyu', label: '瀛楁棌鏉＄洰', text: fam.text, cites: [fam.claim] });
      }
    } catch (e) {
      log('瀛楁棌鍏滃簳澶辫触:', e.message);
    }
  }

  // 鍒嗙骇鏀炬渶鍓嶏細鍏堝畾鎬э紝鍐嶇湅瀛楀舰涓庡瓧涔夛紱鍒ゅ嚭鐨勫瓧鏍瑰彧瑕佹湁瀛楀舰鍥撅紝灏变竴骞堕檮涓?
  let rootGlyphs = [];
  try {
    const lv = await levelOf(ch, direct);
    if (lv) {
      sections.unshift({ key: 'fenji', label: '鍒嗙骇', text: lv.text, cites: lv.cites.filter(Boolean) });
      if (MODE !== 'none') {
        const own = new Set(glyph ? glyph.files : []);
        for (const rc of lv.chainChars || []) {
          if (!rc || rc === ch) continue;
          const gi = glyphInfo(rc);
          // 寮備綋闅跺彉锛堝銆屼互銆嶄箣浜庛€屻牤銆嶏級鏈夋椂鍏辩敤鍚屾壒鍥撅紝鍒噸澶嶅睍绀?
          if (gi && gi.files.length && !gi.files.every((f) => own.has(f))) {
            rootGlyphs.push({ char: rc, doc: gi.doc, files: gi.files });
          }
        }
      }
      // 澹版瘝涔夛細鐢辫繎鍙婅繙鎵惧０绗﹂摼涓婂甫鐙珛澹版瘝涔夋潯鐨勫瓧锛岃惤鍒版墍灞為儴鍒欑敤閮ㄦ潯锛岀揣鎺掑湪鍒嗙骇涔嬪悗
      const sm = await shengmuOf(ch, lv.chainChars || []);
      if (sm) sections.splice(1, 0, { key: 'shengmu', label: '澹版瘝涔?, text: sm.text, cites: [sm.claim] });
    }
    if (!lv) {
      // 鍒や笉鍑哄瓧鏍逛篃涓嶈婕忔帀澹版瘝涔夛細閮ㄥ唴浜岀骇瀛楁牴锛堟皬銆佹皭銆佸烦銆佷簡绛夛級鑷垚涓€鏉?
      const sm = await shengmuOf(ch, []);
      if (sm) sections.splice(1, 0, { key: 'shengmu', label: '澹版瘝涔?, text: sm.text, cites: [sm.claim] });
    }
  } catch (e) {
    log('鍒ょ骇澶辫触:', e.message);
  }

  // 鏍忓簭鍥哄畾锛氱粨璁?鈫?鍒嗙骇 鈫?澹版瘝涔?鈫?瀛楁牴 鈫?鏈箟 鈫?杞箟 鈫?琛嶇敓 鈫?瀵圭収 鈫?瀛楀舰 鈫?灏忕粨
  const rank = (k) => (CARD_ORDER.indexOf(k) === -1 ? 99 : CARD_ORDER.indexOf(k));
  sections = sections
    .map((s, i) => ({ s, i }))
    .sort((a, b) => rank(a.s.key) - rank(b.s.key) || a.i - b.i)
    .map((x) => x.s);
  let presetMeta = null;
  try {
    const pf = join(CARDDIR, ch + '.json');
    if (existsSync(pf)) {
      const pd = JSON.parse(readFileSync(pf, 'utf8'));
      if (pd && !Array.isArray(pd)) presetMeta = { head: pd.head, pinyin: pd.pinyin, level: pd.level, parent: pd.parent, bus: pd.bus, aliases: pd.aliases };
    }
  } catch (e) {}
  emit({
    type: 'card',
    card: {
      ...(presetMeta || {}),
      char: ch,
      question,
      mode,
      note,
      // 鍘熺瀹炵墿鍥撅紙web/public/glyphs/photos/ + index.json 鐨?photos锛夐殢鍗¤緭鍑猴紝
      // 璁╃綉椤典篃鑳界湅鍒伴噴瀛楁椂鐢ㄧ殑閭ｆ壒鍥撅紱閰嶅浘涓嶅弬涓庡垎绾э紝鍙綔鍙傝€冦€?
      glyph: glyph
        ? { doc: glyph.doc, variants: glyph.variants, files: glyph.files, photos: glyph.photos, from: glyphFrom }
        : null,
      family: familyInfo(ch),
      root: rootInfo ? rootInfo.root : null,
      roots: rootGlyphs,
      sections: dedupeSections(sections),
      claims: direct.length + rootClaims.length,
    },
  });
  emit({ type: 'done' });
  res.end();
}

// ---------- 闄愭祦 ----------

const buckets = new Map();

// 浼氬憳鐧诲綍澶辫触璁℃暟锛圛P + 鎵嬫満鍙凤級锛?0 鍒嗛挓鍐呮渶澶?8 娆?
const loginTries = new Map();

function rateLimited(ip) {
  const now = Date.now();
  const b = buckets.get(ip);
  if (!b || now > b.reset) {
    buckets.set(ip, { count: 1, reset: now + RATE_WINDOW });
    return false;
  }
  b.count += 1;
  return b.count > RATE_MAX;
}

// ---------- HTTP ----------

function sendJson(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, {
    'content-type': 'application/json; charset=utf-8',
    'cache-control': 'no-store',
    'content-length': Buffer.byteLength(body),
  });
  res.end(body);
}

function sse(res) {
  res.writeHead(200, {
    'content-type': 'text/event-stream; charset=utf-8',
    'cache-control': 'no-cache, no-transform',
    connection: 'keep-alive',
    'x-accel-buffering': 'no',
  });
  return (obj) => res.write(`data: ${JSON.stringify(obj)}\n\n`);
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on('data', (c) => {
      size += c.length;
      if (size > MAX_BODY) {
        reject(new Error('璇锋眰浣撹繃澶?));
        req.destroy();
        return;
      }
      chunks.push(c);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

const NO_EVIDENCE = '鐭ヨ瘑搴撻噷杩樻病鏈夎繖鏂归潰鐨勫唴瀹广€?;

async function handleAsk(req, res, ip, meter) {
  const emit = sse(res);
  const controller = new AbortController();
  res.on('close', () => controller.abort());

  let question = '';
  let mode = 'auto';
  try {
    const raw = await readBody(req);
    const body = JSON.parse(raw || '{}');
    question = cleanQuestion(body.question);
    if (body.mode === 'card' || body.mode === 'chat') mode = body.mode;
  } catch (e) {
    emit({ type: 'error', message: '璇锋眰鏍煎紡涓嶅锛? + e.message });
    return res.end();
  }
  if (!question) {
    emit({ type: 'error', message: '闂涓嶈兘涓虹┖' });
    return res.end();
  }
  log(`ask [${ip}] ${question}`);

  // 闂殑鏄煇涓€涓瓧 鈫?璧板瓧鍗★紙闄ら潪鐢ㄦ埛鏄庣‘瑕佹櫘閫氶棶绛旓級
  const asked = detectChar(question);
  if (asked && mode !== 'chat') return await handleCard(emit, res, question, asked, ip, meter);

  let evidence;
  try {
    evidence = await retrieve(question);
  } catch (e) {
    log('妫€绱㈠け璐?', e.message);
    emit({ type: 'error', message: '妫€绱㈠嚭閿欙紝璇风◢鍚庡啀璇曘€? });
    return res.end();
  }

  emit({
    type: 'sources',
    items: evidence.hits.map((h) => ({
      id: h.id,
      title: h.title,
      topic_id: h.topic_id,
      node_id: h.node_id,
      score: h.score,
    })),
  });

  if (!evidence.claims.length) {
    emit({ type: 'delta', text: NO_EVIDENCE });
    emit({ type: 'done' });
    return res.end();
  }

  if (MODE === 'skeleton') {
    const text =
      '锛堟湭閰嶇疆妯″瀷锛屼互涓嬩负妫€绱㈠埌鐨勭煡璇嗗師鏂囷級\n\n' +
      evidence.claims
        .map((c) => `**${c.title}** [${c.id}]\n${String(c.statement || '').trim()}`)
        .join('\n\n');
    for (const chunk of text.match(/[\s\S]{1,60}/g) || []) {
      emit({ type: 'delta', text: chunk });
    }
    emit({ type: 'done' });
    return res.end();
  }

  const messages = [
    { role: 'system', content: SYSTEM_PROMPT },
    { role: 'user', content: userPrompt(question, buildContext(evidence.claims)) },
  ];

  let upstream;
  try {
    upstream = await fetch(`${BASE_URL}/chat/completions`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        authorization: `Bearer ${API_KEY}`,
      },
      body: JSON.stringify({
        model: MODEL,
        messages,
        stream: true,
        temperature: 0.2,
        max_tokens: MAX_ANSWER_TOKENS,
        stream_options: { include_usage: true },
      }),
      signal: controller.signal,
    });
  } catch (e) {
    log('妯″瀷璇锋眰澶辫触:', e.message);
    emit({ type: 'error', message: '妯″瀷鏈嶅姟杩炰笉涓婏紝璇风◢鍚庡啀璇曘€? });
    return res.end();
  }

  if (!upstream.ok || !upstream.body) {
    const detail = await upstream.text().catch(() => '');
    log('妯″瀷杩斿洖閿欒:', upstream.status, detail.slice(0, 300));
    emit({ type: 'error', message: `妯″瀷杩斿洖 ${upstream.status}锛岃妫€鏌?Key 鎴栭搴︺€俙 });
    return res.end();
  }

  const reader = upstream.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  let answerChars = 0;
  let usage = null;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split('\n');
      buffer = parts.pop() || '';
      for (const line of parts) {
        const t = line.trim();
        if (!t.startsWith('data:')) continue;
        const payload = t.slice(5).trim();
        if (!payload || payload === '[DONE]') continue;
        try {
          const json = JSON.parse(payload);
          if (json.usage) usage = json.usage;
          const delta = json.choices?.[0]?.delta?.content;
          if (delta) {
            answerChars += delta.length;
            emit({ type: 'delta', text: delta });
          }
        } catch {
          /* 蹇界暐蹇冭烦绛夐潪 JSON 琛?*/
        }
      }
    }
  } catch (e) {
    if (!controller.signal.aborted) {
      log('娴佸紡璇诲彇涓柇:', e.message);
      emit({ type: 'error', message: '鍥炵瓟涓柇浜嗭紝璇烽噸璇曘€? });
    }
  }
  if (meter) {
    const inChars = messages[0].content.length + messages[1].content.length;
    const c = usageCost(usage, inChars, answerChars);
    meter.yuan += c.yuan;
    meter.inTok += c.inTok;
    meter.outTok += c.outTok;
    log(`闂瓟鎴愭湰 [${ip}] ${c.yuan} 鍏冿紙鍏?${c.inTok} / 鍑?${c.outTok} token锛塦);
  }
  emit({ type: 'done' });
  res.end();
}

const MIME = new Map([
  ['.html', 'text/html; charset=utf-8'],
  ['.css', 'text/css; charset=utf-8'],
  ['.js', 'text/javascript; charset=utf-8'],
  ['.json', 'application/json; charset=utf-8'],
  ['.svg', 'image/svg+xml'],
  ['.png', 'image/png'],
  ['.jpg', 'image/jpeg'],
  ['.jpeg', 'image/jpeg'],
  ['.webp', 'image/webp'],
  ['.gif', 'image/gif'],
  ['.ico', 'image/x-icon'],
]);

async function serveStatic(res, pathname) {
  pathname = pathname.replace(/^\/glyphs\/([^\/]+)\/\1\/(.+)$/, '/glyphs/$1/$2');
  // 瀛楀舰鍥剧洰褰曟槸涓枃鍚嶏紝URL 閲屾槸鐧惧垎鍙风紪鐮侊紝蹇呴』鍏堣В鐮?
  let rel;
  try {
    rel = decodeURIComponent(pathname);
  } catch {
    rel = pathname;
  }
  rel = rel === '/' ? 'index.html' : rel.replace(/^\/+/, '');
  if (rel === 'admin' || rel === 'admin/') rel = 'admin.html';
  const target = normalize(join(PUBLIC, rel));
  if (!target.startsWith(PUBLIC + sep) && target !== join(PUBLIC, 'index.html')) {
    res.writeHead(403).end('forbidden');
    return;
  }
  try {
    const data = await readFile(target);
    res.writeHead(200, {
      'content-type': MIME.get(extname(target).toLowerCase()) || 'application/octet-stream',
      'cache-control': (extname(target).toLowerCase()==='.html'?'no-store':'no-cache'),
      'content-length': data.length,
    });
    res.end(data);
  } catch {
    res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' }).end('404');
  }
}

// 鍏嶈垂璇曠敤 / 浼氬憳鏉冪泭鐨勯椄闂細鍙湁杩欓噷鑳藉喅瀹氫竴娆℃彁闂畻涓嶇畻鏁?
function gateAsk(req, res) {
  const mid = shop.verifyNamed('sh_mid', readCookie(req, 'sh_mid'));
  const m = shop.memberOf(mid);
  if (m && shop.memberStatus(m).active) {
    if (shop.usageToday(m.id) >= DAILY_CAP) {
      return { ok: false, status: 429, body: { ok: false, error: '浠婂ぉ鐨勬彁闂凡杈炬瘡鏃ヤ笂闄愶紝鏄庡ぉ鍐嶆潵銆? } };
    }
    if (shop.spendToday(m.id) >= MEMBER_DAILY_YUAN) {
      return { ok: false, status: 429, body: { ok: false, error: '浠婂ぉ鐨勭敤閲忓凡杈句笂闄愶紝鏄庡ぉ鍐嶆潵銆? } };
    }
    return {
      ok: true,
      mode: 'member',
      settle: (cost = 0) => {
        shop.bumpUsage(m.id);
        if (cost > 0) shop.addSpend(m.id, cost);
      },
    };
  }
  const dev = shop.deviceId(req, res);
  const t = shop.trialOf(dev);
  const exhausted = {
    ok: false,
    status: 402,
    body: { ok: false, error: '鍏嶈垂浣撻獙棰濆害宸茬敤瀹岋紝寮€閫氫細鍛樺悗鍙笉闄愭鏌ヨ銆?, need_membership: true, trial: { ...t, budget_yuan: TRIAL_BUDGET_YUAN } },
  };
  if (t.left <= 0) return exhausted;
  // 娆℃暟娌″埌锛屼絾杩欎竴璁惧宸茬粡鑺辨帀鐨勯挶蹇埌 1 鍏冧簡锛屼篃鎷︿綇
  if (t.spent_yuan + MIN_CALL_YUAN > TRIAL_BUDGET_YUAN) return exhausted;
  return { ok: true, mode: 'trial', settle: (cost = 0) => shop.consumeTrial(dev, cost) };
}

const server = createServer(async (req, res) => {
  const ip = (req.socket.remoteAddress || '0.0.0.0').replace('::ffff:', '');
  const url = new URL(req.url || '/', `http://${HOST}:${PORT}`);
  const path = url.pathname;
  if (path.startsWith('/card/')) {
    let ch = decodeURIComponent(path.slice(6)).replace(/\.html$/, '');
    try {
      if (!existsSync(join(CARD_DIR, ch + '.json'))) {
        const idx = JSON.parse(readFileSync(join(CARD_DIR, 'index.json'), 'utf8'));
        const items = Array.isArray(idx) ? idx : (idx.items || []);
        const hits = items.filter((it) => (it.a || []).includes(ch) && it.c && existsSync(join(CARD_DIR, it.c + '.json')));
        hits.sort((p, q) => (p.lv || 9) - (q.lv || 9) || String(p.c).localeCompare(String(q.c)));
        const heads = hits.filter((it) => it.lv === 1);
        if (hits.length > 1 && heads.length === 1) {
          res.writeHead(302, { Location: '/card/' + encodeURIComponent(heads[0].c) }); return res.end();
        }
        if (hits.length === 1) {
          res.writeHead(302, { Location: '/card/' + encodeURIComponent(hits[0].c) }); return res.end();
        }
        const vs=(()=>{try{return JSON.parse(readFileSync(join(PUBLIC,'variants.json'),'utf8'))[ch]||null;}catch(e){return null;}})();
        if(vs&&vs.length){ const arr=Array.isArray(vs)?vs:[vs]; const tt=arr.find(x=>existsSync(join(CARD_DIR,x+'.json'))); if(tt){ res.writeHead(302,{Location:'/card/'+encodeURIComponent(tt)}); return res.end(); } }
        if (hits.length > 1) {
          const seen = new Set(); const links = [];
          for (const h of hits) { if (seen.has(h.c)) continue; seen.add(h.c); links.push('<li><a href="/card/'+encodeURIComponent(h.c)+'">'+escH(h.c)+'</a>'+(h.h&&h.h!==h.c?'锛?+escH(h.h)+'锛?:'')+'</li>'); }
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
          return res.end('<!doctype html><meta charset="utf-8"><h3>銆?+escH(ch)+'銆嶅吋浣滃瀛楃殑鎴栦綋</h3><p>璇烽€夋嫨瑕佺湅鐨勫瓧澶达細</p><ul>'+links.join('')+'</ul>');
        }
        // 鍗峰崱绠€绉?鍏ㄧО浜掗€氾細寤夸竴 鈫?浜屽崄涓€銆佸崊 鈫?涓夊崄
        const _alts = [];
        if (/寤?.test(ch)) _alts.push(ch.replace(/寤?g, '浜屽崄'));
        if (/鍗?.test(ch)) _alts.push(ch.replace(/鍗?g, '涓夊崄'));
        if (/浜屽崄/.test(ch)) _alts.push(ch.replace(/浜屽崄/g, '寤?));
        if (/涓夊崄/.test(ch)) _alts.push(ch.replace(/涓夊崄/g, '鍗?));
        for (const a of _alts) {
          if (existsSync(join(CARD_DIR, a + '.json'))) { res.writeHead(302, { Location: '/card/' + encodeURIComponent(a) }); return res.end(); }
        }
      }
    } catch (e) {}
    const html = renderCard(ch);
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
    return res.end(html || '<!doctype html><meta charset="utf-8"><p>娌℃湁杩欎釜瀛椼€?/p>');
  }

  try {
    const _seg = decodeURIComponent(path.replace(/^\/+|\/+$/g, ''));
    if (_seg && !_seg.includes('/') && !/\./.test(_seg) && Array.from(_seg).length <= 3) {
      let _t = null;
      if (existsSync(join(CARD_DIR, _seg + '.json'))) _t = _seg;
      if (!_t) {
        const idx = JSON.parse(readFileSync(join(CARD_DIR, 'index.json'), 'utf8'));
        const items = Array.isArray(idx) ? idx : (idx.items || []);
        const hit = items.find((it) => it.c === _seg || (it.a || []).includes(_seg));
        if (hit && existsSync(join(CARD_DIR, hit.c + '.json'))) _t = hit.c;
      }
      if (!_t) {
        const vs = (() => { try { return JSON.parse(readFileSync(join(PUBLIC, 'variants.json'), 'utf8'))[_seg] || null; } catch (e) { return null; } })();
        if (vs) { const arr = Array.isArray(vs) ? vs : [vs]; _t = arr.find((x) => existsSync(join(CARD_DIR, x + '.json'))) || null; }
      }
      if (_t) { res.writeHead(302, { Location: '/card/' + encodeURIComponent(_t) }); return res.end(); }
    }
  } catch (e) {}

  try {
    if (path === '/api/health') {
      const tree = await getTree();
      return sendJson(res, 200, { ok: true, pkc: '0.2.0rc5', claims: tree.claims, mode: MODE });
    }

    if (path === '/api/tree') {
      const tree = await getTree();
      return sendJson(res, 200, tree);
    }

    if (path === '/api/glyph') {
      const ch = [...(url.searchParams.get('char') || '').trim()][0] || '';
      if (!isHan(ch)) return sendJson(res, 400, { ok: false, error: 'bad char' });
      return sendJson(res, 200, { ok: true, char: ch, glyph: glyphInfo(ch) });
    }

    if (path.startsWith('/api/claim/')) {
      const id = path.slice('/api/claim/'.length);
      if (!/^clm_[0-9A-F]{20,40}$/.test(id)) return sendJson(res, 400, { ok: false, error: 'bad id' });
      const r = await pkc(['show', id]);
      if (!r.claim) return sendJson(res, 404, { ok: false, error: 'not found' });
      return sendJson(res, 200, {
        ok: true,
        claim: {
          id: r.claim.id,
          title: r.claim.title,
          statement: r.claim.statement,
          node_id: r.claim.node_id,
          topic_id: r.claim.topic_id,
          permission: r.claim.permission,
          lifecycle: r.claim.lifecycle,
        },
      });
    }

    // ---------- 浼氬憳 / 璇曠敤 / 鍏戞崲鐮?----------

    if (path === '/api/pricing') {
      return sendJson(res, 200, {
        ok: true,
        trial_limit: TRIAL_LIMIT,
        trial_budget_yuan: TRIAL_BUDGET_YUAN,
        daily_cap: DAILY_CAP,
        site_url: process.env.SITE_URL || '',
        tiers: Object.values(TIERS),
      });
    }

    if (path === '/api/me') {
      const dev = shop.deviceId(req, res);
      const mid = shop.verifyNamed('sh_mid', readCookie(req, 'sh_mid'));
      const m = shop.memberOf(mid);
      const st = shop.memberStatus(m);
      const t = shop.trialOf(dev);
      return sendJson(res, 200, {
        ok: true,
        trial: { ...t, budget_yuan: TRIAL_BUDGET_YUAN, remaining_yuan: Math.max(0, Math.round((TRIAL_BUDGET_YUAN - t.spent_yuan) * 1e6) / 1e6) },
        member: m
          ? { ...publicMember(m), reason: st.reason, used_today: shop.usageToday(m.id), spent_today: shop.spendToday(m.id) }
          : null,
      });
    }

    if (path === '/api/redeem' && req.method === 'POST') {
      let body = {};
      try {
        body = JSON.parse((await readBody(req)) || '{}');
      } catch {
        body = {};
      }
      const r = shop.redeem(body.code, body.phone, body.password);
      if (!r.ok) return sendJson(res, 400, { ok: false, error: r.error });
      shop.deviceId(req, res);
      res.appendHeader('Set-Cookie', shop.cookie('sh_mid', r.member.id, 365 * 24 * 3600));
      return sendJson(res, 200, { ok: true, member: publicMember(r.member) });
    }

    // 璐﹀彿瀵嗙爜鐧诲綍锛氭墜鏈哄彿 + 瀵嗙爜锛岀櫥褰曞悗鎹㈣澶囦篃鑳界敤
    if (path === '/api/login' && req.method === 'POST') {
      let body = {};
      try {
        body = JSON.parse((await readBody(req)) || '{}');
      } catch {
        body = {};
      }
      const key = `${ip}:${String(body.phone || '').trim()}`;
      const tries = loginTries.get(key) || { n: 0, t: Date.now() };
      if (Date.now() - tries.t > 10 * 60 * 1000) {
        tries.n = 0;
        tries.t = Date.now();
      }
      if (tries.n >= 8) return sendJson(res, 429, { ok: false, error: '瀵嗙爜閿欒娆℃暟澶锛岃 10 鍒嗛挓鍚庡啀璇? });
      const r = shop.login(body.phone, body.password);
      if (!r.ok) {
        tries.n += 1;
        loginTries.set(key, tries);
        await new Promise((rr) => setTimeout(rr, 300));
        return sendJson(res, 401, { ok: false, error: r.error });
      }
      loginTries.delete(key);
      res.appendHeader('Set-Cookie', shop.cookie('sh_mid', r.member.id, 365 * 24 * 3600));
      return sendJson(res, 200, { ok: true, member: publicMember(r.member) });
    }

    if (path === '/api/logout' && req.method === 'POST') {
      res.appendHeader('Set-Cookie', shop.cookie('sh_mid', '', 0));
      return sendJson(res, 200, { ok: true });
    }

    // 宸茬櫥褰曚細鍛樻敼瀵嗙爜
    if (path === '/api/password' && req.method === 'POST') {
      const mid = shop.verifyNamed('sh_mid', readCookie(req, 'sh_mid'));
      const m = shop.memberOf(mid);
      if (!m) return sendJson(res, 401, { ok: false, error: '璇峰厛鐧诲綍' });
      let body = {};
      try {
        body = JSON.parse((await readBody(req)) || '{}');
      } catch {
        body = {};
      }
      if (m.pass_hash) {
        const old = shop.login(m.phone, body.old_password);
        if (!old.ok) return sendJson(res, 400, { ok: false, error: '鍘熷瘑鐮佷笉瀵? });
      }
      try {
        shop.setPassword(m.id, body.new_password);
        return sendJson(res, 200, { ok: true });
      } catch (e) {
        return sendJson(res, 400, { ok: false, error: e.message });
      }
    }

    if (path === '/api/admin/login' && req.method === 'POST') {
      let body = {};
      try {
        body = JSON.parse((await readBody(req)) || '{}');
      } catch {
        body = {};
      }
      const a = Buffer.from(String(body.password || ''));
      const b = Buffer.from(ADMIN_PW);
      const ok = a.length === b.length && timingSafeEqual(a, b);
      if (!ok) {
        await new Promise((r) => setTimeout(r, 400));
        return sendJson(res, 401, { ok: false, error: '瀵嗙爜涓嶅' });
      }
      res.appendHeader('Set-Cookie', shop.cookie('sh_admin', 'ok', 7 * 24 * 3600));
      return sendJson(res, 200, { ok: true });
    }

    if (path === '/api/admin/logout' && req.method === 'POST') {
      res.appendHeader('Set-Cookie', shop.cookie('sh_admin', '', 0));
      return sendJson(res, 200, { ok: true });
    }

    if (path.startsWith('/api/admin/')) {
      if (!isAdmin(req)) return sendJson(res, 401, { ok: false, error: '璇峰厛鐧诲綍' });
      const sub = path.slice('/api/admin/'.length);
      let body = {};
      if (req.method === 'POST') {
        try {
          body = JSON.parse((await readBody(req)) || '{}');
        } catch {
          body = {};
        }
      }
      if (sub === 'stats') return sendJson(res, 200, { ok: true, stats: shop.stats() });
      if (sub === 'codes' && req.method === 'GET') {
        return sendJson(res, 200, { ok: true, codes: shop.listCodes(url.searchParams.get('status') || '') });
      }
      if (sub === 'codes' && req.method === 'POST') {
        try {
          // price: 0 = 琛ュ紑/璧犻€侊紝涓嶈鏀跺叆锛涗笉浼犲垯鎸夋。浣嶅師浠?
          const price = body.free || body.price === 0 ? 0 : undefined;
          return sendJson(res, 200, { ok: true, codes: shop.addCodes(body.tier, body.count, body.note || '', price) });
        } catch (e) {
          return sendJson(res, 400, { ok: false, error: e.message });
        }
      }
      if (sub === 'orders' && req.method === 'GET') {
        const list = Object.values(shop.db.orders)
          .sort((a, b) => b.created_at.localeCompare(a.created_at))
          .slice(0, 500);
        return sendJson(res, 200, { ok: true, orders: list });
      }
      if (sub === 'orders' && req.method === 'POST') {
        try {
          return sendJson(res, 200, { ok: true, ...shop.recordOrder(body) });
        } catch (e) {
          return sendJson(res, 400, { ok: false, error: e.message });
        }
      }
      if (sub === 'members' && req.method === 'GET') {
        const list = Object.values(shop.db.members)
          .sort((a, b) => b.created_at.localeCompare(a.created_at))
          .slice(0, 500)
          .map((m) => ({
            id: m.id, phone: m.phone, tier: m.tier, tier_name: m.tier_name,
            started_at: m.started_at, expires_at: m.expires_at, code: m.code,
            gift: m.gift, gift_sent: m.gift_sent, gift_sent_at: m.gift_sent_at,
            revoked: m.revoked, revoked_at: m.revoked_at, created_at: m.created_at,
            has_password: Boolean(m.pass_hash),
            active: shop.memberStatus(m).active,
            used_today: shop.usageToday(m.id),
            spent_today: shop.spendToday(m.id),
          }));
        return sendJson(res, 200, { ok: true, members: list });
      }
      if (sub === 'revoke' && req.method === 'POST') {
        const ok = shop.revokeMember(body.member_id);
        return sendJson(res, ok ? 200 : 404, { ok, error: ok ? undefined : '娌℃湁杩欎釜浼氬憳' });
      }
      if (sub === 'gift' && req.method === 'POST') {
        const ok = shop.markGiftSent(body.member_id);
        return sendJson(res, ok ? 200 : 404, { ok, error: ok ? undefined : '娌℃湁杩欎釜浼氬憳' });
      }
      if (sub === 'rebind' && req.method === 'POST') {
        try {
          const out = shop.bindCode(body.member_id);
          return sendJson(res, 200, { ok: true, ...out });
        } catch (e) {
          return sendJson(res, 400, { ok: false, error: e.message });
        }
      }
      if (sub === 'reset-password' && req.method === 'POST') {
        try {
          shop.setPassword(body.member_id, body.password);
          return sendJson(res, 200, { ok: true });
        } catch (e) {
          return sendJson(res, 400, { ok: false, error: e.message });
        }
      }
      return sendJson(res, 404, { ok: false, error: 'no such admin api' });
    }

    if (path === '/api/ask' && req.method === 'POST') {
      if (rateLimited(ip)) {
        res.writeHead(429, { 'content-type': 'application/json; charset=utf-8' });
        return res.end(JSON.stringify({ ok: false, error: '闂緱澶揩浜嗭紝姝囦竴鍒嗛挓鍐嶆潵銆? }));
      }
      const g = gateAsk(req, res);
      if (!g.ok) return sendJson(res, g.status, g.body);
      let failed = false;
      const meter = { yuan: 0, inTok: 0, outTok: 0 };
      const origWrite = res.write.bind(res);
      res.write = (chunk, ...rest) => {
        if (typeof chunk === 'string' && chunk.includes('"type":"error"')) failed = true;
        return origWrite(chunk, ...rest);
      };
      res.on('finish', () => {
        if (!failed) g.settle(meter.yuan);
      });
      return await handleAsk(req, res, ip, meter);
    }

    if (req.method === 'GET') return await serveStatic(res, path);

    res.writeHead(405).end('method not allowed');
  } catch (e) {
    log('澶勭悊璇锋眰鍑洪敊:', e.stack || e.message);
    if (!res.headersSent) sendJson(res, 500, { ok: false, error: '鏈嶅姟鍣ㄥ唴閮ㄩ敊璇? });
    else res.end();
  }
});

server.listen(PORT, HOST, () => {
  log(`绯荤粺姹夊瓧闂瓟鏈嶅姟宸插惎鍔?http://${HOST}:${PORT}`);
  log(`妯″紡: ${MODE} | 妯″瀷: ${MODEL} | Key: ${maskKey(API_KEY)}`);
  log(`鐭ヨ瘑搴撴牴: ${ROOT}`);
});

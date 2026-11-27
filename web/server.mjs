// server.mjs — 「系统汉字」知识库问答网页服务（零依赖 Node）
// 只做两件事：把问题交给 pkc 检索，把检索到的 Claim 组织成有出处的答案。
// 绝不直接读 knowledge/** 或 .local/，一切经由 pkc-bridge.py → pkc。

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
    if (cp>=0x20000 && cp<=0x3FFFF){
      const name=cp.toString(16)+'.png';
      if (existsSync(join(ROOT,'web','public','glyphs','chars',name))) { out+='<img class="cch" src="/glyphs/chars/'+name+'">'; continue; }
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
  const _hd=String(d.head||d.char);const _m=_hd.match(/^([^（(]+)[（(]([^）)]*)[）)]\s*$/);const _hl=_m?escH(_m[1])+'（'+Array.from(_m[2]).map(a=>'<a class="al" href="/card/'+encodeURIComponent(a)+'">'+ext(a)+'</a>').join('')+'）':ext(_hd);
  h+='<a class="back" href="/test.html">← 返回检索</a><h2>'+_hl+' <small>'+escH(d.pinyin||'')+'</small></h2>';
  let _b0=Array.isArray(d.bus)?d.bus[0]:(d.bus||null);
  try { if(!_b0||!_b0.num){ let pr=d.parent, hop=0; while(pr&&hop<3){ const pf=join(CARDDIR,pr+'.json'); if(existsSync(pf)){ const pd=JSON.parse(readFileSync(pf,'utf8')); const pb=Array.isArray(pd.bus)?pd.bus[0]:pd.bus; if(pb&&pb.num){ _b0=pb; break; } pr=pd.parent; } else break; hop++; } } } catch(e){}
  try { const b0=_b0; const _fam=(d.sections||[]).some(x=>x&&x.key==='zizu'&&(x.groups||[]).length); const lv=d.grade||(d.level===1?'一级字根':d.level===2?'二级字根':(d.level===3&&_fam)?'三级字根':d.level===3?'谐声字':''); let pill=lv; const _rc=(Array.isArray(d.rootChain)&&d.rootChain.length>1)?(' · '+d.rootChain.join(' → ')):''; if(_rc) pill+=_rc; if(b0&&b0.num>0) pill+=' · 第'+b0.num+'部「'+String(b0.name||'').replace(/部$/,'')+'部」'; else if(b0&&b0.name) pill+=' · 「'+b0.name+'部」'; if(pill) h+='<p class="pill">'+pill+'</p>'; } catch(e){}
  let _gN=0;
  try { const gi=glyphInfo(d.char); if (gi && gi.files && gi.files.length){ h+='<div class="gs">'+gi.files.map((u)=>'<figure><img src="'+u+'?v='+Date.now()+'" alt="字形'+(++_gN)+'"><figcaption>'+String(_gN).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'; } } catch(e){}
  let _photosH='';
  try { const ex=((loadGlyphIndex().chars||{})[d.char]||{}).extra||[];
    for (const e of ex){ const g2=glyphInfo(e.char); if(!g2 || !g2.files || !g2.files.length) continue;
      h+='<p><b><a class="al" href="/card/'+encodeURIComponent(e.char)+'">'+escH(e.label||e.char)+'</a></b></p><div class="gs">'+g2.files.map((u,i)=>'<figure><img src="'+u+'?v='+Date.now()+'" alt="字形'+(++_gN)+'"><figcaption>'+String(_gN).padStart(2,'0')+'</figcaption></figure>').join('')+'</div>'; }
  } catch(e){}
  try { const gi2=glyphInfo(d.char); const ps=(gi2&&gi2.photos)||[]; if (ps.length){ _photosH='<h3>插图</h3><div class="gs">'+ps.map(p=>{const f=(typeof p==='string')?p:(p.file||p.name||'');const cap=(typeof p==='object'&&p.caption)?p.caption:'';return '<figure><img src="'+escH((String(f).startsWith('/')?f:('/glyphs/photos/'+encodeURIComponent(d.char)+'/'+encodeURIComponent(f)))+'?v=20261127b')+'" alt="'+escH(cap||'插图')+'" style="'+(ps.length===1?'max-width:100%;height:auto':'height:170px')+'"><figcaption>'+escH(cap||'')+'</figcaption></figure>';}).join('')+'</div>'; } } catch(e){}
  try {
    const _hasZigen=(d.sections||[]).some(x=>['zigen','rootembed'].includes(x.key)||String(x.label||'').startsWith('字根「'));
    if (d.parent && !_hasZigen && !d.noRoot) {
      const pf2 = join(CARDDIR, d.parent + '.json');
      if (existsSync(pf2)) {
        const pd2 = JSON.parse(readFileSync(pf2, 'utf8'));
        const keep = (pd2.sections || []).filter(x => ['benyi','zhuanyi','bianzheng','yinyuan'].includes(x.key) && (x.text || (x.paras && x.paras.length)));
        if (keep.length) {
          const label = '字根「' + (pd2.head || pd2.char || d.parent) + '」';
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
    if (s.label==='所属卷'){ h+='<h3>所属卷</h3><p>'+(((s.links&&s.links.length?s.links:(d.links||[]))).map(l=>'<a class="jl" href="/card/'+encodeURIComponent(l.ch)+'">'+escH(l.label||l.ch)+'</a>').join(' · '))+'</p>'; continue; }
    h+='<h3>'+escH(s.label||s.key)+'</h3>';
    if (s.key==='erji' && s.links && s.links.length){
      h+='<p>'+s.links.map(l=>'<a class="jl" href="/card/'+encodeURIComponent(l.ch)+'">'+escH(l.label||l.ch)+'</a>').join(' · ')+'</p>';
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
      if (s.gimgs && s.gimgs.length){ /* 字根块不重复列字形 */ }
      continue;
    }
    if (s.groups && s.groups.length){
        if (s.text) h+='<p>'+ext(s.text)+'</p>';
      /* 唯一一组且组题只是「未分组（原稿未列/归组）」这类占位时，不印组题，只印表 */
      const _ph = s.groups.length===1 && /^未分[组組]/.test(String((s.groups[0]||{}).title||''));
      for (const g of s.groups){
        if (g.title && !_ph) h+='<p><b>'+escH(g.no||'')+ext(g.title)+'</b></p>';
        if (g.note) h+='<p style="color:#666">'+ext(g.note)+'</p>';
        const head=(String(g.title||'').indexOf('部目')>=0)?['部目','字根','中心义','字族']:(g.header||['字','读音','类属','取义落点']);
        h+='<table><tr>'+head.map(t=>'<th>'+escH(t)+'</th>').join('')+'</tr>';
        for (const r of (g.rows||[])) h+='<tr>'+r.map((x,i)=>{
          let cell=ext(x);
          try { if (i===0 && String(head[0])==='部目'){ const m=/^(.+?)部$/.exec(String(x||'').trim()); if(m && existsSync(join(CARDDIR,m[1]+'.json'))) cell='<a href="/card/'+encodeURIComponent(m[1])+'">'+cell+'</a>'; } } catch(e){}
          return '<td>'+cell+'</td>';
        }).join('')+'</tr>';
        h+='</table>';
      }
    } else if (s.cimgs) { h+='<div class="gsbar"><button class="gsnav gsl" aria-label="左翻" onclick="var s=this.parentNode.querySelector(\'.gs\');s.scrollBy({left:-260,behavior:\'smooth\'})">‹</button><div class="gs">'+s.cimgs.map(f=>{const o=(typeof f==='string')?{f:f}:(f||{});const src='/glyphs/'+String(o.f||'').split('/').map(encodeURIComponent).join('/');return '<figure><img src="'+src+'" alt="'+escH(o.cap||'参证')+'" style="height:88px"><figcaption>'+escH(o.cap||'')+'</figcaption></figure>';}).join('')+'<button class="gsnav gsr" aria-label="右翻" onclick="var s=this.parentNode.querySelector(\'.gs\');s.scrollBy({left:260,behavior:\'smooth\'})">›</button></div>'; } else if (Array.isArray(s.paras) && s.paras.length) { h+=s.paras.map(pp=>{ const parts=[]; let tx=String(pp).replace(/\{\{([^}]+)\}\}/g,(m,f)=>{parts.push(((s.gdir||'')+'/'+f)); return '\u0002'+(parts.length-1)+'\u0003';}); tx=ext(tx); tx=tx.replace(/\u0002(\d+)\u0003/g,(m,i)=>'<img class="cim" src="/glyphs/'+String(parts[+i]).split('/').map(encodeURIComponent).join('/')+'?v=20261127b">'); return '<p>'+tx+'</p>'; }).join(''); } else if (s.text) { const parts=[]; let tx=String(s.text).replace(/\{\{([^}]+)\}\}/g,(m,f)=>{parts.push(((s.gdir||'')+'/'+f)); return '\u0002'+(parts.length-1)+'\u0003';}); tx=ext(tx); tx=tx.replace(/\u0002(\d+)\u0003/g,(m,i)=>'<img class="cim" src="/glyphs/'+String(parts[+i]).split('/').map(encodeURIComponent).join('/')+'?v=20261127b">'); h+='<p>'+tx+'</p>'; }
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

// ---------- 会员 / 订单 ----------

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
const KEY_FILE = 'C:\\Users\\萧磊\\.dsh\\secrets\\deepseek.key';
const BASE_URL = process.env.DEEPSEEK_BASE || 'https://api.deepseek.com';
const MODEL = process.env.DEEPSEEK_MODEL || 'deepseek-chat';

const RETRIEVE_LIMIT = 8;
const CONTEXT_CLAIMS = 8;
const MAX_QUESTION = 200;
const MAX_BODY = 64 * 1024;
const RATE_MAX = 20;
const RATE_WINDOW = 60_000;

// ---------- 成本闸门 ----------
// 按 deepseek-flash 的「高峰价」保守计价（实际多数时候是空闲价的一半），
// 这样算出来的上限只会偏大，不会让客户的真实花费超过预算。
// 输入（缓存未命中）2 元/百万 token，输出 8 元/百万 token。
const PRICE_IN_YUAN_PER_M = 2;
const PRICE_OUT_YUAN_PER_M = 8;
const TRIAL_BUDGET_YUAN = Number(process.env.TRIAL_BUDGET_YUAN || 1);      // 每个设备免费体验最多花 1 元
const MEMBER_DAILY_YUAN = Number(process.env.MEMBER_DAILY_YUAN || 3);      // 会员每天最多花 3 元，防滥用
const MIN_CALL_YUAN = 0.004;   // 一次回答预计要花的最低成本，余额低于它就不再放行
const MAX_ANSWER_TOKENS = 600; // 单次回答输出上限

function usageCost(usage, inChars, outChars) {
  const inTok = usage && usage.prompt_tokens ? usage.prompt_tokens : Math.round((inChars || 0) / 1.5) + 400;
  const outTok = usage && usage.completion_tokens ? usage.completion_tokens : Math.round((outChars || 0) / 1.2);
  const yuan = (inTok / 1e6) * PRICE_IN_YUAN_PER_M + (outTok / 1e6) * PRICE_OUT_YUAN_PER_M;
  return { yuan: Math.round(yuan * 1e6) / 1e6, inTok, outTok };
}

// ---------- 基础工具 ----------

function maskKey(k) {
  if (!k) return '(none)';
  return k.length <= 10 ? '***' : k.slice(0, 6) + '…' + k.slice(-4);
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
    log('读取 Key 文件失败:', e.message);
  }
  return '';
}

const API_KEY = loadKey();
const MODE = API_KEY ? 'model' : 'skeleton';

// ---------- pkc 调用 ----------

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
    child.on('error', (e) => reject(new Error('无法启动 python: ' + e.message)));
    child.on('close', (code) => {
      const text = out.trim();
      if (!text) return reject(new Error('pkc 无输出' + (err ? ': ' + err.slice(-300) : '')));
      try {
        resolve(JSON.parse(text));
      } catch {
        reject(new Error(`pkc 返回非 JSON（exit ${code}）：${text.slice(0, 200)}`));
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
    const mNode = line.match(/^(\S+)\s+—\s+(.+)$/);
    if (mNode) {
      current = { id: mNode[1], title: mNode[2].trim(), topics: [] };
      nodes.push(current);
      continue;
    }
    const mTopic = line.match(/└─\s+(\S+)\s+—\s+(.+?)\s+\((\d+)\s+claims\)/);
    if (mTopic && current) {
      current.topics.push({ id: mTopic[1], title: mTopic[2].trim(), claims: Number(mTopic[3]) });
    }
  }
  const claims = nodes.reduce((s, n) => s + n.topics.reduce((t, x) => t + x.claims, 0), 0);
  const data = { ok: true, nodes, claims };
  treeCache = { at: Date.now(), data };
  return data;
}

// ---------- 检索 ----------

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

  // 命中标题/摘要的条目再取全文（含适用边界），最多 CONTEXT_CLAIMS 条
  return { question: q, hits, claims: await hydrate(hits) };
}

// 命中标题/摘要的条目再取全文（含适用边界），最多 CONTEXT_CLAIMS 条
async function hydrate(hits) {
  const wanted = hits.slice(0, CONTEXT_CLAIMS);
  const claims = await Promise.all(
    wanted.map((h) =>
      pkc(['show', h.id])
        .then((r) => (r.claim ? { ...r.claim, score: h.score } : null))
        .catch((e) => {
          log('show-claim 失败', h.id, e.message);
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
      return `[${i + 1}] ${c.id} 《${c.title}》\n节点/主题：${c.node_id} / ${c.topic_id}\n正文：\n${body}`;
    })
    .join('\n\n---\n\n');
}

const SYSTEM_PROMPT = `你是「系统汉字」知识库的问答助手。你只能依据下面提供的知识条目回答。

规则：
1. 每条结论后面用 [clm_XXXXXXXX] 标注出处，id 必须来自条目列表，不得编造。
2. 条目的全部内容你都能看到。回答前先把条目逐条读过，再组织答案；不要断言「条目没有记载」，除非你确实逐条检查过。
3. 只有当所有条目都与问题无关时，才回答「知识库里还没有这方面的内容。」；若条目相关但不足以完整回答，先说库里有什么，再指出缺哪一部分，不要用你自己的知识补充或推测。
4. 属于《系统汉语》观点的条目，要点明这是该书的判断，不是文献学界的共识。
5. 不要复述编号、节点、主题这些内部字段；不要输出条目原文以外的内容。
6. 简体中文，先给结论再给说明，控制在 300 字以内。`;

function userPrompt(question, context) {
  return `知识条目：\n\n${context}\n\n---\n\n用户问题：${question}`;
}

// ---------- 字卡模式 ----------
// 模板固定四段：甲骨文字形图 / 本义 / 转义 / 衍生字义（哪些衍生字）。
// 字形图来自《系统汉语》各卷原稿抽出的字形表（tools/extract-glyphs.mjs），
// 图下自带原书标注的出处与分期；文字部分只允许来自 public+active 的 Claim。

const GLYPH_INDEX = join(PUBLIC, 'glyphs', 'index.json');
let glyphCache = { at: 0, data: null };

function loadGlyphIndex() {
  if (glyphCache.data && Date.now() - glyphCache.at < 300_000) return glyphCache.data;
  try {
    const data = JSON.parse(readFileSync(GLYPH_INDEX, 'utf8'));
    glyphCache = { at: Date.now(), data };
    return data;
  } catch (e) {
    log('字形库读取失败:', e.message);
    return { chars: {} };
  }
}

// 简体字头 → 原稿繁体字头。原稿以繁体立字头，用户多按简体提问；
// 字形库、配图库按繁体建键，故此处做一次显式映射（只映射确实需要的字，宁少勿滥）。
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

// 简体/异体写法 → 原稿字头（variants.json 是一键一正字）
function variantOf(ch) {
  const m = loadVariantMap();
  const v = m[ch];
  return Array.isArray(v) ? v[0] || '' : v || '';
}

function photoList(list) {
  return (list || []).map((x) => {
    if (typeof x === 'string') return { file: '/glyphs/photos/' + encodeURIComponent(x), caption: '' };
    const f = String((x && (x.file || x.name)) || '');
    return { file: f ? '/glyphs/' + f.split('/').map(encodeURIComponent).join('/') : '', caption: (x && x.caption) || '' };
  }).filter((p) => p.file);
}

// 字族表：原稿字头行冒号后面那串（牡 社 仕…），按原稿顺序，各自带上自己的配图
// 只有自己能点出一张有内容的字卡（有独立条目或能落到字族条）的，才做成可点；否则只列名不链接
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

// ---------- 字根分级 ----------
// 依据「全书目录与结构」：「部号+部首字」是最小定位单位，609 部即一级字根；
// 部内能再滋生的衍生字是二级、三级字根，其余是谐声字（clm_640129CD…）。
// 部名索引由 tools/zigen-index.mjs 从 mulu.md 生成，服务层不直接读 knowledge/。
const ZIGEN_INDEX = join(PUBLIC, 'zigen.json');
let zigenCache = { at: 0, data: null };

function loadZigenIndex() {
  if (zigenCache.data && Date.now() - zigenCache.at < 300_000) return zigenCache.data;
  try {
    const data = JSON.parse(readFileSync(ZIGEN_INDEX, 'utf8'));
    zigenCache = { at: Date.now(), data };
    return data;
  } catch (e) {
    log('字根索引读取失败:', e.message);
    return { byName: {}, juan: [], chapters: [] };
  }
}

const JUAN_CN = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十'];
function juanCn(n) {
  if (!n) return '';
  if (n <= 10) return JUAN_CN[n];
  if (n < 20) return '十' + JUAN_CN[n - 10];
  if (n === 100) return '一百';
  const a = Math.floor(n / 10);
  const b = n % 10;
  return (a === 1 ? '十' : JUAN_CN[a] + '十') + (b ? JUAN_CN[b] : '');
}

const HAN_ONE = /\p{Script=Han}/u;
const isHan = (ch) => !!ch && HAN_ONE.test(ch);
const CARD_TOPICS = /(本义|本義|本意|字源|字形|甲骨文|转义|轉義|引申义|引申|衍生字|衍生|字族|字根|意思|含义)/;

// 判断问题是不是在「问某一个字」
function detectChar(question) {
  let s = String(question || '').trim();
  if (!s) return null;
  s = s.replace(/[？?。！!，,、；;：:~～\s]+$/g, '').trim();
  if (!s) return null;

  // 1) 引号里点名的字：「雞」「鸡」
  const quoted = s.match(/[「『“"]([^」』”"]{1,3})[」』”"]/);
  if (quoted) {
    const cs = [...quoted[1]].filter(isHan);
    if (cs.length === 1) return cs[0];
  }

  // 2) 整句只有一个汉字（可带「字」）
  const plain = s.replace(/\s+/g, '');
  const all = [...plain].filter(isHan);
  if (all.length === 1 && plain.length <= 2) return all[0];

  // 3) X的本义 / X字 / X的转义 / X的字根是什么 …
  const m = plain.match(
    /^[^\p{Script=Han}]{0,4}(\p{Script=Han})(?:字)?(?:的)?(?:本义|本義|本意|字源|字形|甲骨文|转义|轉義|引申义|引申|衍生字|衍生|字族|字根|意思|含义)(?:是什么|是啥|是哪些|有哪些)?$/u
  );
  if (m) return m[1];

  return null;
}

const CARD_SECTIONS = [
  { key: 'jielun', field: '结论', label: '结论' },
  { key: 'zigen', field: '字根', label: '先释字根' },
  { key: 'benyi', field: '本义', label: '本义' },
  { key: 'zhuanyi', field: '转义', label: '转义' },
  { key: 'yansheng', field: '衍生', label: '衍生字义' },
  { key: 'duizhao', field: '对照', label: '横向对照（按义类分组）' },
  { key: 'zixing', field: '字形', label: '字形' },
  { key: 'xiaojie', field: '小结', label: '一句总结' },
];

// 固定栏序：结论 → 分级 → 声母义 → 先释字根 → 本义 → 转义 → 衍生字义 → 横向对照 → 字形 → 一句总结
const CARD_ORDER = ['jielun', 'fenji', 'shengmu', 'zigen', 'benyi', 'zhuanyi', 'yansheng', 'duizhao', 'zixing', 'xiaojie', 'zuyu', 'other'];

let EXEGESIS_STYLE = "";
try {
  const { readFileSync } = await import("node:fs");
  EXEGESIS_STYLE = readFileSync(new URL("./prompts/exegesis.md", new URL("../", import.meta.url)), "utf8").trim();
} catch (e) { EXEGESIS_STYLE = ""; }
const CARD_PROMPT = `${EXEGESIS_STYLE ? "【释字回答体例（共用规范，必须照此组织答案）】\n" + EXEGESIS_STYLE + "\n\n" : ""}你是《系统汉语》字卡的编辑。只依据下面给出的知识条目填写字卡，条目以外的内容一个字都不许加。

只输出严格 JSON，不要代码块标记，不要解释：
{"结论":"…","字根":"…","本义":"…","转义":"…","衍生":"…","对照":"…","字形":"…","小结":"…"}
栏序与写法（按此顺序填，每栏都要有实质内容，不许一句话打发）：
- 每栏末尾必须标出处：用上面条目的编号写 [1]、[3]，一栏引多条就连写 [1][3]；没有编号的句子会被丢弃。
- 结论：三到四句，先说这个字是什么字、本义是什么、字根给它哪一面义，让人不读下文也拿到答案。
- 字根：先讲字根自己的本义（一、二、三级字根一律本义直释，不作比况），再讲它怎么进到这个字里；声符链有两级以上就逐级讲。
- 本义：六书判语开头，然后把本义讲透（构形、所指之物、字书依据），再分条列出引申路径。
- 转义：按引申路径分层写，每层给出字书依据与例词。
- 衍生：字族字按义类分组列，每组写「字（形符）落点」，重要者附一句文化用法。
- 对照：把条目里已有的「横向对照（按义类分…）」原句整理成分组串写，按 ①②③ 分行；没有对照材料就写「暂无」。
- 字形：说清看形要点（构件位置、从早到晚的变化），不要只报字形来源。
- 小结：一句话收拢这个字的声符给义、形符定落点的关系，不要重复结论。结论：三到四句，先说这个字是什么字、本义是什么、字根给它哪一面义，让人不读下文也拿到答案。
- 对照：把条目里已有的「横向对照（按义类分…）」原句整理成分组串写，按 ①②③ 分行；组内写「字（形符）落点」；没有对照材料就写「暂无」。
- 一句总结：一句话收拢这个字的声符给义、形符定落点的关系，不要重复结论。

填写要求：
0. 分级：字卡最前面「分级」一栏由系统按全书结构判好（一级字根＝部名；部内能再滋生新字者为二级、三级字根；其余为谐声字），你不得改动、不得另立级别。填「字根」一栏时先交代该字属于哪一级、由哪个字根衍生，再讲字根义如何进入这个字。
0b. 声母义：该字所属部的声母拟态义与一致度也由系统附上（「声母义」一栏），你不得改写、不得另拟声母义；讲字根时可以引用它的结论。引用时必须把这个拟态义落到本字所指之物上讲透（如「莼」只取 ch 的「刺」：芽尖刺破土层而出），不得只报「某母、某义、某一致度」了事。**拟态义本是相对的两面（t 涂突、ch 刺持、l 拢离…），释一个字一般只讲合于它的那一面，不必两面都解说**；只有引申链确实横跨两面时才写两面（如「柳」编束为拢、折别为离）。**不得因一致度弱、部内分歧、或该部未收而断言「与声母义无关」**：古音 zh、ch、sh 从 d、t 分化，齿音与舌音同源，须循声源分化链贯通解释；确实相违时也要说明为何相违（异读、假借音、方言），不许轻易说不相关。
1. 字形：该字在甲骨文、金文里的形体如何象形或构形；条目没讲字形，就填空字符串。
2. 字根：这个字由哪个字根构成（条目里「从某从某」「从某，某声」说的那个字），并说清字根与这个字的关系——会意还是形声、字根的意义怎么进到这个字里。**取字根义时优先用字根的本义；本义讲不通，才降一级用转义**（如「疚」从久，久的本义是灸灼、灼病，故疚＝灼痛之病，不可取「久」的引申义「时间长」；字书「疚，久也」是声训，不是义源）。**声旁给义的方式是比喻，要写成「象……一样」**：疚＝象被灸灼一样疼痛，玖＝象被烧灼一样色黑；形符只定其类与落点。**但比喻只给「形旁＋声旁」的合成谐声字；解释字根本身一律本义直释**：舆的本义就是两人对举抬车之状，追的本义就是跟在屁股后面跑——这是直释，不是比喻；象意兼声字（车＋舁、鼎＋𦥑）同理只说明声旁兼义，不套「象……一样」。**声符链有两级以上时（如 㠯→台→始、匃→曷→渴），要逐级说明每一级字根各给的是哪一面义，再落到这个字上**——不能只写最后一级。****不要轻易判作「象声、不取义」**——声旁几乎都有实义，实义与比喻义两层并存（如「轰」＝三车象意众车，实义「众车」，比喻「声大如众车行驶之声」）。**若是谐声字，必须做横向对照**：取条目里同声符的兄弟字至少 3 个，按「字｜取义面｜形符｜落到什么义」比较，说明同一取义面在不同形符下怎样落到不同字义，再定这个字的落点（如吾部：梧＝木＋相对→树上下相当，晤＝日＋相对→人相见，鼯＝鼠＋相对→高下相对、只能从高赴下）。**对照要覆盖全族、按义类分表**：把全族兄弟字先按意义归类（取本义／取转义／只借声），每类一张表，最后总收「声符给义、形符定落点」，只借声那一类也要列出；可对照的兄弟字不足 3 个就写明「可对照者仅 N 字」。**同一动物有异名异体而声符不同者更可互证**——鼫从石（象掷石下落），与鼯的高下相对同指「由高向下滑降」。写成「字根：说明」，例如「士：仕从人从士，士是音源字，本义指雄性，引申为读书人、官员，所以「仕」表任事、学习政事」。若条目分「字根条目」单列，用它们说明字根本身的意义，并分别标注出处。字根必须是另一个字，不能把这个字自己写进去；条目只说它是借音字、没有构形分析的，填空字符串。
3. 本义：**开头必须先写一句六书判语，格式「六书：……」**，再讲造字之初的意义。六书用班固名目，不用「形声」一词。判法（按条目原文判断）：条目说它是「音源字」、或读音「源自……声」＝象声；条目说「从某从某」而两字各有独立意义＝象意；条目说「从某，某声」、某字是声根、这个字是加形旁分化来的＝转注；独体、字形如画＝象形；在象形字上加一个无义符号＝象事；因义借声＝假借。复合的照绪论六种组合报，如「象意＋转注」「象意＋象声」。只要条目里有「从某声」「音源字」「从某从某」这类线索就必须判；一条线索都没有才不写判语。若字表构形之外另有条目说它是「音源字」、读音「源自……声」，判语要合成两截（如「象意＋象声」「象形＋象声」），不要只写构形那一截。
4. 转义：引申义、假借义。
5. 衍生：由它分化、加注形旁或用它作声符的字，写成「字：意义；字：意义」，最多 6 个字；条目里说「同组」「属……类」的那些字也算，一个都别漏。
6. 每个非空字段末尾必须带 [clm_XXXXXXXX] 出处（字根、衍生两栏尤其不能漏），id 只能取自条目列表，不得编造，一个字段可以带多个。
7. 条目里没有依据的字段一律输出空字符串 ""，不要用你自己的常识补。
8. 简体中文，字形、字根、转义各不超过 130 字，本义（含六书一句）不超过 170 字，衍生不超过 150 字。`;

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

// 只保留出自条目的引用；没有有效引用的一律判为「无依据」
// order 是上下文里的编号表，模型偷懒写 [3] 也能映射回 clm_ id
const LIUSHU_CORE = '(?:象形|象事|象意|象声|转注|假借)';
const LIUSHU_HEAD = new RegExp('^(' + LIUSHU_CORE + '(?:[＋+／/]' + LIUSHU_CORE + ')*)([，。：:\\s、])');

// 六书判语统一成「六书：……」开头（主人定：放在本义解释里头，不单列一栏）
function ensureLiushu(sec) {
  if (!sec || !sec.text) return sec;
  const t = String(sec.text).trim();
  if (/^六书\s*[：:]/.test(t)) return sec;
  if (!LIUSHU_HEAD.test(t)) return sec;
  return { ...sec, text: '六书：' + t };
}

function sanitizeSection(raw, allowed, order) {
  let s = String(raw || '')
    .replace(/\r/g, '')
    .trim();
  if (!s) return null;
  const ids = [];
  s = s.replace(/[[【]\s*(clm_[0-9A-Fa-f]{20,40})\s*[\]】]/g, (m, id) => {
    const up = 'clm_' + id.slice(4).toUpperCase();
    if (!allowed.has(up)) return '';
    ids.push(up);
    return `[${up}]`;
  });
  s = s.replace(/[[【]\s*(\d{1,2})\s*[\]】]/g, (m, n) => {
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
  const body = blocks.find((x) => !/^(适用边界|边界)/.test(x)) || '';
  const one = body.split('\n')[0].trim();
  if (!one || one.length > 100) return '';
  if (one === String(claim.title || '').trim()) return '';
  return one;
}

// 没有模型（或模型失败）时的确定性字卡：按条目原文归类
// 字根一栏不在这里分桶，由 zigenFallback() 单独拼，避免出现两个「字根」

function dedupeSections(sections) {
  const norm = (s) => String(s || '').replace(/\[clm_[0-9A-F]+\]/g, '').replace(/[\s，。；：、"'（）()【】]/g, '');
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
    if (/本义|本義|初文|象形|象[\s\S]{0,6}形|字形/.test(hay)) buckets.get('benyi').push(c);
    else if (/引申|轉義|转义|假借|借音|借声/.test(hay)) buckets.get('zhuanyi').push(c);
    else if (/字族|衍生|分化|从[\s\S]{0,4}[声聲]/.test(hay)) buckets.get('yansheng').push(c);
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
      label: '其他相关条目',
      text: rest.map((c) => `**${c.title}** [${c.id}]`).join('\n\n'),
      cites: rest.map((c) => c.id),
    });
  }

  // 结论：把这个字自己的本义条的第一句提出来，不读下文也能得到答案
  const bc = claims.find((c) => String(c.title || '').startsWith(ch)) || null;
  if (bc) {
    const body = String(bc.statement || '')
      .split('#### 适用边界')[0]
      .replace(/^#+\s*/gm, '')
      .replace(/^\s*[^\n：:]{0,30}[：:]\s*(?=\S)/m, '')
      .replace(/\s+/g, ' ')
      .trim();
    const first = (body.split(/(?<=[。；])/)[0] || body).slice(0, 130);
    if (first) secs.unshift({ key: 'jielun', label: '结论', text: first, cites: [bc.id] });
  }
  // 横向对照：条目正文里已经写好的「横向对照（…）」原句，摘出来单独成栏
  const dz = [];
  for (const c of claims) {
    const m = String(c.statement || '').match(/横向对照（[^）]*）：[^\n]+/);
    if (m) dz.push(m[0].trim());
  }
  if (dz.length) {
    secs.push({ key: 'duizhao', label: '横向对照（按义类分组）', text: dz.slice(0, 3).join('\n\n') });
  }
  return secs;
}

// 按字检索：优先取标题/正文里真的出现这个字的条目
async function retrieveForChar(ch) {
  const res = await pkc(['query', ch, '12']);
  const hits = (res.results || [])
    .filter((r) => r.kind === 'claim' && r.permission === 'public' && r.lifecycle === 'active')
    .slice(0, 12);
  const claims = (await hydrate(hits)).filter(Boolean);
  const direct = claims.filter((c) => `${c.title}\n${c.statement || ''}`.includes(ch));
  return { hits, claims, direct };
}

// 从条目里的「从某从某」「从某，某声」找出这个字的构字成分（候选字根）
const COMP_RE = /从[「『“"']?([\p{Script=Han}])[」』”"']?/gu;
const SHENG_RE = /[「『“"']?([\p{Script=Han}])[」』”"']?[声聲]/gu;

function rootsOf(ch, claims) {
  const out = new Map();
  const esc = ch.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  // 「X」…从：要求「从」紧跟在这个字之后，避免把别人的构形算到它头上
  const lead = new RegExp(`「?${esc}」?[^。；;\\n]{0,14}?从`, 'u');
  for (const c of claims) {
    const text = `${c.title}\n${c.statement || ''}`;
    if (text.includes(`${ch}是音源字`)) continue; // 自己就是音源字，没有更上位的字根
    if (/不确|不確|析形不确|误|誤/.test(text)) continue; // 条目自己说这种析形靠不住，不采
    for (const sent of text.split(/[。；;\n]/)) {
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

// 优先取「知识库里自己有主题（X部）」或「条目自称音源字」的那个成分当字根
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
      byYinyuan: hay.includes('音源字') && hay.includes(`「${root}」`),
    };
  });
  return list.find((x) => x.byTopic) || list.find((x) => x.byYinyuan) || null;
}

// 这个字能不能再滋生新字（判二级/三级字根的依据）：条目里它作声符，或自称音源字
function spawnsFrom(ch, claims) {
  if (!ch) return false;
  const esc = ch.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const reFrom = new RegExp(`从[^。；\\n]{0,8}${esc}[声聲]`, 'u');
  for (const c of claims) {
    const t = `${c.title}\n${c.statement || ''}`;
    if (String(c.title || '').startsWith(`${ch}部`)) return true; // 有自己的「X部」字族条目
    if (t.includes(`${ch}是音源字`) || t.includes(`「${ch}」是音源字`)) return true;
    if (reFrom.test(t)) return true;
  }
  return false;
}

// 异体或隶变写法（如「以」之于「㠯」）：同属一部，按一级字根看待
// 注意：与一元的 variantOf(ch)（variants.json 简化字映射）不是一回事，勿混用
function variantRootOf(ch, claims, z) {
  if (!ch || !Array.isArray(claims) || !z) return null;
  const esc = ch.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  for (const c of claims) {
    const title = String(c.title || '');
    const m = title.match(/^([\p{Script=Han}])部[：:]/u);
    if (!m || !z.byName || !z.byName[m[1]]) continue;
    const escRoot = m[1].replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    if (new RegExp(`${escRoot}（${esc}）`, 'u').test(title)) return m[1];
  }
  return null;
}

// 「X部：字族…」这类条目把谐声字按字族归堆，是「从某声」之外的第二条判级线索
function familyOf(ch, claims) {
  for (const c of claims) {
    const title = String(c.title || '');
    const m = title.match(/^([\p{Script=Han}])部[：:]/u);
    if (!m || m[1] === ch) continue;
    if (!/字族|衍生|谐声/.test(title)) continue;
    if (`${title}\n${c.statement || ''}`.includes(ch)) return { root: m[1], claim: c };
  }
  return null;
}

// 判级（释字第一步）：一级字根＝609 部的部首字；部内衍生字按能否再滋生分二级、三级字根，
// 不能再滋生者为谐声字。声符链最多上溯两层，够覆盖「㠯→台→始」这类结构。
// ---------- 声母义（分部主题）----------
// 一部一条，由 pkc 生成到 knowledge/hanzi-yinyuan/02z-shengmu-yi.md，这里直接读该主题文件
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
      const body = m[3].split('#### 适用边界')[0].trim();
      const hit = title.match(/^(.+?)部：声母义/u);
      const sub = title.match(/^(.+?)（二级字根）：声母义/u);
      if (hit) byRoot.set(hit[1], { id, text: body });
      else if (sub) byZi.set(sub[1], { id, text: body });
      else if (title.startsWith('零声母诸部')) zero = { id, text: body };
    }
  } catch (e) {
    log('读声母义主题失败:', e.message);
  }
  smCache = { at: Date.now(), byRoot, byZi, zero };
  return smCache;
}

async function shengmuOf(ch, chain) {
  if (!ch && !(chain && chain.length)) return null;
  const idx = await shengmuIndex();
  // 声符链由远及近，末尾再带上本字：先找「谁自己有独立声母义条」，
  // 例如「始」从台声，该用「台」条（三读不系）而不是㠯部的零声母条。
  const list = [...(chain && chain.length ? chain : []), ch].filter(Boolean);
  for (let i = list.length - 1; i >= 0; i -= 1) {
    const own = idx.byZi.get(list[i]);
    if (own) return { claim: own.id, text: own.text };
  }
  const root = list[0] || ch;
  const hit = idx.byRoot.get(root);
  if (hit) return { claim: hit.id, text: hit.text };
  if (idx.zero && idx.zero.text.includes(`「${root}部」`)) {
    return {
      claim: idx.zero.id,
      text: `${root}部读零声母；绪论七组声母未列零声母，故不系拟态声母义，该部释义靠义类与字形。`,
    };
  }
  return null;
}

// 没有独立条目的字（如「銀」「海」「莼」）：到字族条里找它被解释的那一条，整段作为「字族条目」栏
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
      if (!/字族|部[：:]/.test(h.title || '')) continue;
      let cl = null;
      try {
        cl = JSON.parse(await pkc(['show-claim', h.claim, '--format', 'json'])).claim;
      } catch (e) {
        continue;
      }
      if (!cl || !cl.statement) continue;
      const text = String(cl.statement).split('#### 适用边界')[0].trim();
      if (!text) continue;
      if (!chars.some((x) => text.includes(x))) continue;
      return { claim: cl.id, title: cl.title, text };
    }
  }
  return null;
}

async function levelOf(ch, direct) {
  const z = loadZigenIndex();
  // 原稿按繁体立字头，用户多按简体提问：先映射到繁体再判级，
  // 否则 zigen.json / 字形库查不到键，分级栏就空了。
  const aliasCh = variantOf(ch);
  if (aliasCh && aliasCh !== ch) ch = aliasCh;
  const bu = z.byName && z.byName[ch];
  if (bu) {
    return {
      level: '一级字根',
      text: `一级字根：「${ch}」是第 ${bu.no} 部「${ch}部」的部首字，属卷${juanCn(bu.juanNo)}「${bu.juanName}」（p${bu.p}）。部即字根；全书 609 部中第223部原缺、第554部部首字未能转录，其余 608 部即一级字根。`,
      cites: [bu.claim],
      chainChars: [ch],
    };
  }
  if (!direct || !direct.length) return null;
  const variant = variantRootOf(ch, direct, z);
  if (variant) {
    const bv = z.byName[variant];
    return {
      level: '一级字根',
      text: `一级字根：「${ch}」是「${variant}」的异体或隶变写法，同属第 ${bv.no} 部「${variant}部」（卷${juanCn(bv.juanNo)}「${bv.juanName}」），按部首字看待。`,
      cites: direct.filter((c) => String(c.title || '').startsWith(`${variant}部`)).map((c) => c.id),
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
  // 异体或隶变写法（如「以」之于「㠯」）：按一级字根看待，不降级
  const alias = direct.some((c) => {
    const t = `${c.title}\n${c.statement || ''}`;
    return t.includes(ch) && t.includes(root) && /(隶作|隸作|共一字|异体|異體|或作|古字|同字)/.test(t);
  });
  const bu2 = z.byName && z.byName[root];
  const where = bu2
    ? `第 ${bu2.no} 部「${root}部」（卷${juanCn(bu2.juanNo)}「${bu2.juanName}」）`
    : `「${root}」`;
  const chain = depth === 2 ? `「${root}」→「${via}」→「${ch}」` : `「${root}」→「${ch}」`;
  const cites = [r1.claim.id];
  if (depth === 1 && alias && bu2) {
    return {
      level: '一级字根',
      text: `一级字根：「${ch}」是「${root}」的异体或隶变写法，同属${where}，按部首字看待。`,
      cites,
      chainChars: [root],
    };
  }
  if (depth === 1) {
    if (spawn) {
      return {
        level: '二级字根',
        text: `二级字根：「${ch}」从${where}的「${root}」得声构形（${chain}）；它在部内还能滋生新字，故为二级字根。`,
        cites,
        chainChars: [root],
      };
    }
    return {
      level: '谐声字',
      text: `谐声字：「${ch}」从${where}的「${root}」得义得声（${chain}）；自身不再滋生新字，属该部末端谐声字。`,
      cites,
      chainChars: [root],
    };
  }
  if (spawn) {
    return {
      level: '三级字根',
      text: `三级字根：「${ch}」不在部目上，声符链为${chain}，源头是${where}；它在二级字根之下还能滋生新字，故为三级字根。`,
      cites,
      chainChars: [root, via],
    };
  }
  return {
    level: '谐声字',
    text: `谐声字：「${ch}」的声符链为${chain}，源头是${where}；自身不再滋生新字，属部内三级以下的谐声字。`,
    cites,
    chainChars: [root, via],
  };
}

// 字条目 + 字根条目分两组编号，模型才能分清哪句在讲字根
// 返回上下文与「编号 → 条目 id」的对照，模型只写 [3] 这种编号时也能追回来
function cardContext(ch, direct, root, rootClaims) {
  const order = [];
  const block = (claims) =>
    claims
      .map((c) => {
        order.push(c.id);
        const body = String(c.statement || '').replace(/\r\n/g, '\n').trim();
        return `[${order.length}] ${c.id} 《${c.title}》\n节点/主题：${c.node_id} / ${c.topic_id}\n正文：\n${body}`;
      })
      .join('\n\n---\n\n');
  const parts = [`「${ch}」的条目：\n\n${block(direct)}`];
  if (root && rootClaims.length) {
    parts.push(`字根「${root}」的条目（用来说明字根本身的意义）：\n\n${block(rootClaims)}`);
  }
  return { context: parts.join('\n\n====\n\n'), order };
}

// 没有模型时，字根一栏只用条目原文拼
function zigenFallback(info, rootClaims) {
  const { root, claim } = info;
  const body = briefOf(claim);
  if (!body && !rootClaims.length) return null;
  const lines = [`字根：${root}`];
  if (body) lines.push(body);
  for (const c of rootClaims.slice(0, 4)) {
    const b = briefOf(c);
    lines.push(`**${c.title}** [${c.id}]` + (b ? `\n${b}` : ''));
  }
  return {
    key: 'zigen',
    label: '字根',
    text: lines.join('\n\n'),
    cites: [claim.id, ...rootClaims.slice(0, 4).map((c) => c.id)],
  };
}

async function askModelForCard(ch, question, context, meter) {
  const messages = [
    { role: 'system', content: CARD_PROMPT },
    { role: 'user', content: `字：${ch}\n用户问题：${question}\n\n知识条目：\n\n${context}` },
  ];
  const r = await fetch(`${BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: { 'content-type': 'application/json', authorization: `Bearer ${API_KEY}` },
    body: JSON.stringify({ model: MODEL, messages, stream: false, temperature: 0.2, max_tokens: 1800 }),
    signal: AbortSignal.timeout(45_000),
  });
  if (!r.ok) {
    const d = await r.text().catch(() => '');
    throw new Error(`模型返回 ${r.status}：${d.slice(0, 200)}`);
  }
  const j = await r.json();
  const content = j.choices && j.choices[0] && j.choices[0].message ? j.choices[0].message.content : '';
  if (meter) {
    const c = usageCost(j.usage, CARD_PROMPT.length + context.length + 60, String(content || '').length);
    meter.yuan += c.yuan;
    meter.inTok += c.inTok;
    meter.outTok += c.outTok;
    log(`字卡成本 ${c.yuan} 元（入 ${c.inTok} / 出 ${c.outTok} token）`);
  }
  log('字卡模型原文:', String(content || '').replace(/\s+/g, ' ').slice(0, 400));
  return extractJson(content);
}

const CARD_DIR = join(PUBLIC, 'cards');
const presetCache = new Map();

// 别名 → 卡文件名（由 cards/alias-index.json 提供，build_card_alias_index 生成）。
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
  // 字族行首必须是一个汉字；图注残行（「▲…」等）一律丢弃，避免出现在字族 chips 里
  const HAN = /^\p{Script=Han}$/u;
  for (const s of (d.sections || [])) {
    if (!s || s.key !== 'zizu' || !Array.isArray(s.groups)) continue;
    for (const g of s.groups) {
      if (!g || !Array.isArray(g.rows)) continue;
      g.rows = g.rows.filter((r) => Array.isArray(r) && typeof r[0] === 'string' && HAN.test(r[0].trim().replace(/（[^）]*）$/, '')));
    }
  }
  return d;
}

function loadPresetCard(ch) {
  const alias = variantOf(ch) || ch;
  const names = [ch, alias, aliasOf(ch)].filter(Boolean);
  for (const key of new Set(names)) {
    const p = join(CARD_DIR, key + '.json');
    try { if (existsSync(p)) return sanitizeCard(JSON.parse(readFileSync(p, 'utf8'))); } catch (e) { log('字卡读取失败', key, e.message); }
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
    log('字卡检索失败:', e.message);
    emit({ type: 'error', message: '检索出错，请稍后再试。' });
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

  // 字根：从「从人从士」这类条目里找，再把字根自己的条目也取来当证据
  let rootInfo = null;
  let rootClaims = [];
  if (direct.length) {
    try {
      rootInfo = await findRoot(ch, direct);
    } catch (e) {
      log('字根识别失败:', e.message);
    }
    if (rootInfo) {
      try {
        const rr = await retrieveForChar(rootInfo.root);
        rootClaims = rr.direct.filter((c) => !allowed.has(c.id)).slice(0, 6);
        for (const c of rootClaims) allowed.add(c.id);
      } catch (e) {
        log('字根检索失败:', e.message);
      }
    }
  }

  // 这个字在原稿里没有独立的字形行（只是字族成员）时，退一步用字根的字形与配图
  if (!glyph && rootInfo && !d.noRoot) {
    const g = glyphInfo(rootInfo.root);
    if (g) {
      glyph = g;
      glyphFrom = rootInfo.root;
    }
  }

  if (!direct.length) {
    note = `知识库里还没有「${ch}」的专门条目。字形图取自《系统汉语》原稿，可以先看形体；字义条目还在录入，暂不推断。`;
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
      log('字卡模型调用失败:', e.message);
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

  // 这个字没有独立条目时，把解释它的那条字族整段附上（网页也看得到释字时用的原文）
  if (!direct.length) {
    try {
      const fam = await familyClaimFor(ch);
      if (fam) {
        sections.push({ key: 'zuyu', label: '字族条目', text: fam.text, cites: [fam.claim] });
      }
    } catch (e) {
      log('字族兜底失败:', e.message);
    }
  }

  // 分级放最前：先定性，再看字形与字义；判出的字根只要有字形图，就一并附上
  let rootGlyphs = [];
  try {
    const lv = await levelOf(ch, direct);
    if (lv) {
      sections.unshift({ key: 'fenji', label: '分级', text: lv.text, cites: lv.cites.filter(Boolean) });
      if (MODE !== 'none') {
        const own = new Set(glyph ? glyph.files : []);
        for (const rc of lv.chainChars || []) {
          if (!rc || rc === ch) continue;
          const gi = glyphInfo(rc);
          // 异体隶变（如「以」之于「㠯」）有时共用同批图，别重复展示
          if (gi && gi.files.length && !gi.files.every((f) => own.has(f))) {
            rootGlyphs.push({ char: rc, doc: gi.doc, files: gi.files });
          }
        }
      }
      // 声母义：由近及远找声符链上带独立声母义条的字，落到所属部则用部条，紧排在分级之后
      const sm = await shengmuOf(ch, lv.chainChars || []);
      if (sm) sections.splice(1, 0, { key: 'shengmu', label: '声母义', text: sm.text, cites: [sm.claim] });
    }
    if (!lv) {
      // 判不出字根也不要漏掉声母义：部内二级字根（氏、氐、巳、了等）自成一条
      const sm = await shengmuOf(ch, []);
      if (sm) sections.splice(1, 0, { key: 'shengmu', label: '声母义', text: sm.text, cites: [sm.claim] });
    }
  } catch (e) {
    log('判级失败:', e.message);
  }

  // 栏序固定：结论 → 分级 → 声母义 → 字根 → 本义 → 转义 → 衍生 → 对照 → 字形 → 小结
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
      // 原稿实物图（web/public/glyphs/photos/ + index.json 的 photos）随卡输出，
      // 让网页也能看到释字时用的那批图；配图不参与分级，只作参考。
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

// ---------- 限流 ----------

const buckets = new Map();

// 会员登录失败计数（IP + 手机号），10 分钟内最多 8 次
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
        reject(new Error('请求体过大'));
        req.destroy();
        return;
      }
      chunks.push(c);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

const NO_EVIDENCE = '知识库里还没有这方面的内容。';

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
    emit({ type: 'error', message: '请求格式不对：' + e.message });
    return res.end();
  }
  if (!question) {
    emit({ type: 'error', message: '问题不能为空' });
    return res.end();
  }
  log(`ask [${ip}] ${question}`);

  // 问的是某一个字 → 走字卡（除非用户明确要普通问答）
  const asked = detectChar(question);
  if (asked && mode !== 'chat') return await handleCard(emit, res, question, asked, ip, meter);

  let evidence;
  try {
    evidence = await retrieve(question);
  } catch (e) {
    log('检索失败:', e.message);
    emit({ type: 'error', message: '检索出错，请稍后再试。' });
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
      '（未配置模型，以下为检索到的知识原文）\n\n' +
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
    log('模型请求失败:', e.message);
    emit({ type: 'error', message: '模型服务连不上，请稍后再试。' });
    return res.end();
  }

  if (!upstream.ok || !upstream.body) {
    const detail = await upstream.text().catch(() => '');
    log('模型返回错误:', upstream.status, detail.slice(0, 300));
    emit({ type: 'error', message: `模型返回 ${upstream.status}，请检查 Key 或额度。` });
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
          /* 忽略心跳等非 JSON 行 */
        }
      }
    }
  } catch (e) {
    if (!controller.signal.aborted) {
      log('流式读取中断:', e.message);
      emit({ type: 'error', message: '回答中断了，请重试。' });
    }
  }
  if (meter) {
    const inChars = messages[0].content.length + messages[1].content.length;
    const c = usageCost(usage, inChars, answerChars);
    meter.yuan += c.yuan;
    meter.inTok += c.inTok;
    meter.outTok += c.outTok;
    log(`问答成本 [${ip}] ${c.yuan} 元（入 ${c.inTok} / 出 ${c.outTok} token）`);
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
  // 字形图目录是中文名，URL 里是百分号编码，必须先解码
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

// 免费试用 / 会员权益的闸门：只有这里能决定一次提问算不算数
function gateAsk(req, res) {
  const mid = shop.verifyNamed('sh_mid', readCookie(req, 'sh_mid'));
  const m = shop.memberOf(mid);
  if (m && shop.memberStatus(m).active) {
    if (shop.usageToday(m.id) >= DAILY_CAP) {
      return { ok: false, status: 429, body: { ok: false, error: '今天的提问已达每日上限，明天再来。' } };
    }
    if (shop.spendToday(m.id) >= MEMBER_DAILY_YUAN) {
      return { ok: false, status: 429, body: { ok: false, error: '今天的用量已达上限，明天再来。' } };
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
    body: { ok: false, error: '免费体验额度已用完，开通会员后可不限次查询。', need_membership: true, trial: { ...t, budget_yuan: TRIAL_BUDGET_YUAN } },
  };
  if (t.left <= 0) return exhausted;
  // 次数没到，但这一设备已经花掉的钱快到 1 元了，也拦住
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
        if(vs&&vs.length){ const arr=Array.isArray(vs)?vs:[vs]; let tt=arr.find(x=>existsSync(join(CARD_DIR,x+'.json'))); if(!tt){ for(const x of arr){ const h2=items.find(it=>(it.a||[]).includes(x)&&it.c&&existsSync(join(CARD_DIR,it.c+'.json'))); if(h2){tt=h2.c;break;} } } if(tt){ res.writeHead(302,{Location:'/card/'+encodeURIComponent(tt)}); return res.end(); } }
        if (hits.length > 1) {
          const seen = new Set(); const links = [];
          for (const h of hits) { if (seen.has(h.c)) continue; seen.add(h.c); links.push('<li><a href="/card/'+encodeURIComponent(h.c)+'">'+escH(h.c)+'</a>'+(h.h&&h.h!==h.c?'（'+escH(h.h)+'）':'')+'</li>'); }
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
          return res.end('<!doctype html><meta charset="utf-8"><h3>「'+escH(ch)+'」兼作多字的或体</h3><p>请选择要看的字头：</p><ul>'+links.join('')+'</ul>');
        }
        // 卷卡简称/全称互通：廿一 ↔ 二十一、卅 ↔ 三十
        const _alts = [];
        if (/廿/.test(ch)) _alts.push(ch.replace(/廿/g, '二十'));
        if (/卅/.test(ch)) _alts.push(ch.replace(/卅/g, '三十'));
        if (/二十/.test(ch)) _alts.push(ch.replace(/二十/g, '廿'));
        if (/三十/.test(ch)) _alts.push(ch.replace(/三十/g, '卅'));
        for (const a of _alts) {
          if (existsSync(join(CARD_DIR, a + '.json'))) { res.writeHead(302, { Location: '/card/' + encodeURIComponent(a) }); return res.end(); }
        }
      }
    } catch (e) {}
    const html = renderCard(ch);
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
    return res.end(html || '<!doctype html><meta charset="utf-8"><p>没有这个字。</p>');
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

    // ---------- 会员 / 试用 / 兑换码 ----------

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

    // 账号密码登录：手机号 + 密码，登录后换设备也能用
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
      if (tries.n >= 8) return sendJson(res, 429, { ok: false, error: '密码错误次数太多，请 10 分钟后再试' });
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

    // 已登录会员改密码
    if (path === '/api/password' && req.method === 'POST') {
      const mid = shop.verifyNamed('sh_mid', readCookie(req, 'sh_mid'));
      const m = shop.memberOf(mid);
      if (!m) return sendJson(res, 401, { ok: false, error: '请先登录' });
      let body = {};
      try {
        body = JSON.parse((await readBody(req)) || '{}');
      } catch {
        body = {};
      }
      if (m.pass_hash) {
        const old = shop.login(m.phone, body.old_password);
        if (!old.ok) return sendJson(res, 400, { ok: false, error: '原密码不对' });
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
        return sendJson(res, 401, { ok: false, error: '密码不对' });
      }
      res.appendHeader('Set-Cookie', shop.cookie('sh_admin', 'ok', 7 * 24 * 3600));
      return sendJson(res, 200, { ok: true });
    }

    if (path === '/api/admin/logout' && req.method === 'POST') {
      res.appendHeader('Set-Cookie', shop.cookie('sh_admin', '', 0));
      return sendJson(res, 200, { ok: true });
    }

    if (path.startsWith('/api/admin/')) {
      if (!isAdmin(req)) return sendJson(res, 401, { ok: false, error: '请先登录' });
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
          // price: 0 = 补开/赠送，不记收入；不传则按档位原价
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
        return sendJson(res, ok ? 200 : 404, { ok, error: ok ? undefined : '没有这个会员' });
      }
      if (sub === 'gift' && req.method === 'POST') {
        const ok = shop.markGiftSent(body.member_id);
        return sendJson(res, ok ? 200 : 404, { ok, error: ok ? undefined : '没有这个会员' });
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
        return res.end(JSON.stringify({ ok: false, error: '问得太快了，歇一分钟再来。' }));
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
    log('处理请求出错:', e.stack || e.message);
    if (!res.headersSent) sendJson(res, 500, { ok: false, error: '服务器内部错误' });
    else res.end();
  }
});

server.listen(PORT, HOST, () => {
  log(`系统汉字问答服务已启动 http://${HOST}:${PORT}`);
  log(`模式: ${MODE} | 模型: ${MODEL} | Key: ${maskKey(API_KEY)}`);
  log(`知识库根: ${ROOT}`);
});

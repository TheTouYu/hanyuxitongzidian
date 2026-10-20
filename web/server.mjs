// server.mjs — 「系统汉字」知识库问答网页服务（零依赖 Node）
// 只做两件事：把问题交给 pkc 检索，把检索到的 Claim 组织成有出处的答案。
// 绝不直接读 knowledge/** 或 .local/，一切经由 pkc-bridge.py → pkc。

import { createServer } from 'node:http';
import { spawn } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { existsSync, readFileSync } from 'node:fs';
import { join, extname, normalize, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const WEB = fileURLToPath(new URL('.', import.meta.url));
const ROOT = normalize(join(WEB, '..'));
const PUBLIC = join(WEB, 'public');
const PYEXE = join(ROOT, '.runtime', 'python', 'python.exe');
const BRIDGE = join(WEB, 'pkc-bridge.py');

const PORT = Number(process.env.PORT || 8080);
const HOST = '127.0.0.1';
const KEY_FILE = 'C:\\Users\\萧磊\\.dsh\\secrets\\deepseek.key';
const BASE_URL = process.env.DEEPSEEK_BASE || 'https://api.deepseek.com';
const MODEL = process.env.DEEPSEEK_MODEL || 'deepseek-chat';

const RETRIEVE_LIMIT = 8;
const CONTEXT_CLAIMS = 8;
const MAX_QUESTION = 200;
const MAX_BODY = 64 * 1024;
const RATE_MAX = 20;
const RATE_WINDOW = 60_000;

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

function glyphInfo(ch) {
  const idx = loadGlyphIndex();
  const e = idx.chars && idx.chars[ch];
  const ph = (idx.photos && idx.photos[ch]) || [];
  const files = (e && Array.isArray(e.files) ? e.files : []).map((f) => '/glyphs/' + f.split('/').map(encodeURIComponent).join('/'));
  const photos = ph.map((x) => ({
    file: '/glyphs/' + x.file.split('/').map(encodeURIComponent).join('/'),
    caption: x.caption || '',
  }));
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
  { key: 'zixing', field: '字形', label: '字形' },
  { key: 'zigen', field: '字根', label: '字根' },
  { key: 'benyi', field: '本义', label: '本义' },
  { key: 'zhuanyi', field: '转义', label: '转义' },
  { key: 'yansheng', field: '衍生', label: '衍生字义' },
];

const CARD_PROMPT = `你是《系统汉语》字卡的编辑。只依据下面给出的知识条目填写字卡，条目以外的内容一个字都不许加。

只输出严格 JSON，不要代码块标记，不要解释：
{"字形":"…","字根":"…","本义":"…","转义":"…","衍生":"…"}

填写要求：
0. 分级：字卡最前面「分级」一栏由系统按全书结构判好（一级字根＝部名；部内能再滋生新字者为二级、三级字根；其余为谐声字），你不得改动、不得另立级别。填「字根」一栏时先交代该字属于哪一级、由哪个字根衍生，再讲字根义如何进入这个字。
1. 字形：该字在甲骨文、金文里的形体如何象形或构形；条目没讲字形，就填空字符串。
2. 字根：这个字由哪个字根构成（条目里「从某从某」「从某，某声」说的那个字），并说清字根与这个字的关系——会意还是形声、字根的意义怎么进到这个字里。写成「字根：说明」，例如「士：仕从人从士，士是音源字，本义指雄性，引申为读书人、官员，所以「仕」表任事、学习政事」。若条目分「字根条目」单列，用它们说明字根本身的意义，并分别标注出处。字根必须是另一个字，不能把这个字自己写进去；条目只说它是借音字、没有构形分析的，填空字符串。
3. 本义：造字之初的意义。
4. 转义：引申义、假借义。
5. 衍生：由它分化、加注形旁或用它作声符的字，写成「字：意义；字：意义」，最多 6 个字；条目里说「同组」「属……类」的那些字也算，一个都别漏。
6. 每个非空字段末尾必须带 [clm_XXXXXXXX] 出处（字根、衍生两栏尤其不能漏），id 只能取自条目列表，不得编造，一个字段可以带多个。
7. 条目里没有依据的字段一律输出空字符串 ""，不要用你自己的常识补。
8. 简体中文，字形、字根、本义、转义各不超过 130 字，衍生不超过 150 字。`;

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
function fallbackSections(claims) {
  const defs = CARD_SECTIONS.filter((d) => d.key !== 'zigen');
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
function variantOf(ch, claims, z) {
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
async function levelOf(ch, direct) {
  const z = loadZigenIndex();
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
  const variant = variantOf(ch, direct, z);
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

async function askModelForCard(ch, question, context) {
  const messages = [
    { role: 'system', content: CARD_PROMPT },
    { role: 'user', content: `字：${ch}\n用户问题：${question}\n\n知识条目：\n\n${context}` },
  ];
  const r = await fetch(`${BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: { 'content-type': 'application/json', authorization: `Bearer ${API_KEY}` },
    body: JSON.stringify({ model: MODEL, messages, stream: false, temperature: 0.2, max_tokens: 900 }),
    signal: AbortSignal.timeout(45_000),
  });
  if (!r.ok) {
    const d = await r.text().catch(() => '');
    throw new Error(`模型返回 ${r.status}：${d.slice(0, 200)}`);
  }
  const j = await r.json();
  const content = j.choices && j.choices[0] && j.choices[0].message ? j.choices[0].message.content : '';
  log('字卡模型原文:', String(content || '').replace(/\s+/g, ' ').slice(0, 400));
  return extractJson(content);
}

async function handleCard(emit, res, question, ch, ip) {
  let glyph = glyphInfo(ch);
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
  if (!glyph && rootInfo) {
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
      const obj = await askModelForCard(ch, question, ctx.context);
      if (obj) {
        const built = CARD_SECTIONS.map((def) => {
          const raw = obj[def.field] ?? obj[def.label] ?? obj[def.key];
          const sec = sanitizeSection(raw, allowed, ctx.order);
          return sec ? { key: def.key, label: def.label, ...sec } : { key: def.key, label: def.label, missing: true };
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
    sections = fallbackSections(direct);
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
    }
  } catch (e) {
    log('判级失败:', e.message);
  }

  emit({
    type: 'card',
    card: {
      char: ch,
      question,
      mode,
      note,
      glyph: glyph
        ? { doc: glyph.doc, variants: glyph.variants, files: glyph.files, photos: glyph.photos || [], from: glyphFrom }
        : null,
      root: rootInfo ? rootInfo.root : null,
      roots: rootGlyphs,
      sections,
      claims: direct.length + rootClaims.length,
    },
  });
  emit({ type: 'done' });
  res.end();
}

// ---------- 限流 ----------

const buckets = new Map();

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

async function handleAsk(req, res, ip) {
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
  if (asked && mode !== 'chat') return await handleCard(emit, res, question, asked, ip);

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
      body: JSON.stringify({ model: MODEL, messages, stream: true, temperature: 0.2, max_tokens: 800 }),
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
          const delta = json.choices?.[0]?.delta?.content;
          if (delta) emit({ type: 'delta', text: delta });
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
  // 字形图目录是中文名，URL 里是百分号编码，必须先解码
  let rel;
  try {
    rel = decodeURIComponent(pathname);
  } catch {
    rel = pathname;
  }
  rel = rel === '/' ? 'index.html' : rel.replace(/^\/+/, '');
  const target = normalize(join(PUBLIC, rel));
  if (!target.startsWith(PUBLIC + sep) && target !== join(PUBLIC, 'index.html')) {
    res.writeHead(403).end('forbidden');
    return;
  }
  try {
    const data = await readFile(target);
    res.writeHead(200, {
      'content-type': MIME.get(extname(target).toLowerCase()) || 'application/octet-stream',
      'cache-control': 'no-cache',
      'content-length': data.length,
    });
    res.end(data);
  } catch {
    res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' }).end('404');
  }
}

const server = createServer(async (req, res) => {
  const ip = (req.socket.remoteAddress || '0.0.0.0').replace('::ffff:', '');
  const url = new URL(req.url || '/', `http://${HOST}:${PORT}`);
  const path = url.pathname;

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

    if (path === '/api/ask' && req.method === 'POST') {
      if (rateLimited(ip)) {
        res.writeHead(429, { 'content-type': 'application/json; charset=utf-8' });
        return res.end(JSON.stringify({ ok: false, error: '问得太快了，歇一分钟再来。' }));
      }
      return await handleAsk(req, res, ip);
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

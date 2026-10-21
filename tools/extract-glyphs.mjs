#!/usr/bin/env node
// extract-glyphs.mjs — 从《系统汉语》各卷 Word 文档里抽出「字形图」，生成网页用字形库。
//
// 用法：
//   node tools/extract-glyphs.mjs --src "D:\字谱智能体" --out web/public/glyphs
//   node tools/extract-glyphs.mjs --out web/public/glyphs --families-only
//     ↑ 只把「字族表」补进已有 index.json，不重抽图片（源文档比图库新时用）
//
// 文档结构（各卷一致）：
//   字头段：  矢（𠂕𠓡𥎨𠤕𥬟）：致郅𨖹…            ← 收录该字的异体与字族
//   字形行：（𠂕𠓡𥎨𠤕𥬟shǐ）：[图]、[图]、[图]…   ← 按时代先后排列，图内自带出处
//   本義段：  本義：象箭形。…
//
// 做法：把每段切成「文字 / 图片」记号流；字形行以「（…）：」开头，
// 用括号里的异体串挂回前面同异体串的字头，得到 字 → 字形图列表。
// 零依赖：只用 node 内置 zlib 解析 docx（zip）。

import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync, rmSync } from 'node:fs';
import { inflateRawSync } from 'node:zlib';
import { join, extname, basename } from 'node:path';

// ---------- 参数 ----------
const argv = process.argv.slice(2);
function arg(name, fallback) {
  const i = argv.indexOf('--' + name);
  return i >= 0 && argv[i + 1] ? argv[i + 1] : fallback;
}
const SRC = arg('src', 'D:\\字谱智能体');
const OUT = arg('out', join(process.cwd(), 'web', 'public', 'glyphs'));
const MAX_PER_CHAR = Number(arg('max', '8'));
const MAX_BYTES = Number(arg('maxbytes', String(300 * 1024)));
// --only 吉：只抽这几个字（补抽用，不清空输出目录）
let ONLY = new Set();

// ---------- 最小 ZIP 读取 ----------
function readZip(buf) {
  let eocd = -1;
  for (let i = buf.length - 22; i >= Math.max(0, buf.length - 66000); i--) {
    if (buf.readUInt32LE(i) === 0x06054b50) { eocd = i; break; }
  }
  if (eocd < 0) throw new Error('不是有效的 zip/docx');
  const count = buf.readUInt16LE(eocd + 10);
  let p = buf.readUInt32LE(eocd + 16);
  const entries = new Map();
  for (let k = 0; k < count; k++) {
    if (buf.readUInt32LE(p) !== 0x02014b50) break;
    const method = buf.readUInt16LE(p + 10);
    const csize = buf.readUInt32LE(p + 20);
    const nlen = buf.readUInt16LE(p + 28);
    const elen = buf.readUInt16LE(p + 30);
    const clen = buf.readUInt16LE(p + 32);
    const name = buf.toString('utf8', p + 46, p + 46 + nlen);
    const lho = buf.readUInt32LE(p + 42);
    entries.set(name, { method, csize, lho });
    p += 46 + nlen + elen + clen;
  }
  return {
    has: (n) => entries.has(n),
    read(n) {
      const e = entries.get(n);
      if (!e) return null;
      const nlen = buf.readUInt16LE(e.lho + 26);
      const elen = buf.readUInt16LE(e.lho + 28);
      const start = e.lho + 30 + nlen + elen;
      const data = buf.subarray(start, start + e.csize);
      if (e.method === 0) return Buffer.from(data);
      return inflateRawSync(data);
    },
  };
}

function unescapeXml(s) {
  return s
    .replace(/&#x([0-9a-fA-F]+);/g, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(Number(d)))
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&apos;/g, "'")
    .replace(/&amp;/g, '&');
}

// 一段 XML → 记号流：{t:'text'} / {t:'img', rid}
function tokenize(xml) {
  const out = [];
  const re = /<w:t(?:\s[^>]*)?>([\s\S]*?)<\/w:t>|<(?:a:blip|v:imagedata)((?:\s[^>]*)?)\/?>/g;
  let m;
  while ((m = re.exec(xml))) {
    if (m[1] !== undefined) out.push({ t: 'text', s: unescapeXml(m[1]) });
    else {
      const rid = ((m[2] || '').match(/r:(?:embed|id)\s*=\s*"([^"]+)"/) || [])[1];
      if (rid) out.push({ t: 'img', rid });
    }
  }
  return out;
}

// 按 <w:p> 深度切段（文本框嵌套也能正确闭合）
function paragraphs(docXml) {
  const out = [];
  const re = /<w:p\b[^>]*?(\/?)>|<\/w:p>/g;
  let m, depth = 0, start = -1;
  while ((m = re.exec(docXml))) {
    if (m[0] === '</w:p>') {
      depth -= 1;
      if (depth === 0 && start >= 0) {
        out.push(docXml.slice(start, re.lastIndex));
        start = -1;
      }
    } else if (m[1] === '/') {
      if (depth === 0) out.push(m[0]);
    } else {
      if (depth === 0) start = m.index;
      depth += 1;
    }
  }
  return out;
}

// ---------- 单个文档解析 ----------
const HAN = /[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u{20000}-\u{2FA1F}]/u;
const HAN_G = /[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u{20000}-\u{2FA1F}]/gu;

function onlyHan(s) {
  return (s.match(HAN_G) || []).join('');
}

// 字头：X（异体串）：…（也有无括注的写法：奚：谿…）
const HEAD = /^\s*([^\s（(]{1,4})\s*[（(]([^）)]*)[）)]\s*[：:]/;
const HEAD2 = /^\s*([\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u{20000}-\u{2FA1F}])[：:]\s*\S/u;
// 字形行：（异体串+拼音）：图、图…
const ROW = /^\s*[（(]([^）)]*)[）)]\s*[：:]/;

function parseDocx(file) {
  const buf = readFileSync(file);
  const zip = readZip(buf);
  const docXml = (zip.read('word/document.xml') || Buffer.alloc(0)).toString('utf8');
  const relXml = (zip.read('word/_rels/document.xml.rels') || Buffer.alloc(0)).toString('utf8');
  const rels = new Map();
  for (const m of relXml.matchAll(/<Relationship\b([^>]*?)\/?>/g)) {
    const attrs = m[1];
    const id = (attrs.match(/Id="([^"]+)"/) || [])[1];
    const target = (attrs.match(/Target="([^"]+)"/) || [])[1];
    if (!id || !target) continue;
    rels.set(id, basename(target.replace(/\\/g, '/')));
  }
  const paras = [];
  for (const px of paragraphs(docXml)) {
    const toks = tokenize(px);
    if (!toks.length) continue;
    let text = '';
    const imgs = [];
    for (const t of toks) {
      if (t.t === 'text') text += t.s;
      else imgs.push(t.rid);
    }
    if (text.trim() || imgs.length) paras.push({ text, imgs, toks });
  }
  return { paras, rels, zip };
}

// 字形行里的分组标签：图片串后面跟一个单字，标的是它前面那组图
const LABEL = /^[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u{20000}-\u{2FA1F}]$/u;

// 部头，如「9.士部」：字形行里没写异体字时，用它兜底
const PART = /^\s*\d+\s*[.．、]\s*([\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u{20000}-\u{2FA1F}])\s*部\s*$/u;

function extractChars({ paras }) {
  const heads = [];
  const entries = [];
  const photos = [];
  const families = new Map();
  let rows = 0;
  let unmatched = 0;
  let lastHead = null;
  let lastPart = null;
  let owner = null;
  let sectionOwner = null;
  let inFamily = false;
  let partHeads = [];
  const usedHeads = new Set();

  const captionOf = (p) => {
    const t = (p.text || '').trim();
    return t.startsWith('▲') ? t.replace(/^▲\s*/, '').trim() : '';
  };

  for (let pi = 0; pi < paras.length; pi++) {
    const p = paras[pi];
    const mPart = p.text.match(PART);
    if (mPart) {
      lastPart = mPart[1];
      partHeads = []; // 换部了，按出现顺序重新排队
    }

    const mHead = p.text.match(HEAD) || p.text.match(HEAD2);
    if (mHead) {
      const ch = onlyHan(mHead[1]);
      if (ch) {
        const at = p.text.search(/[：:]/);
        // 冒号后是字族表；括号里是异体或交叉引用（如「鯉（參209《土部》）」），先剔掉
        const famText = (at >= 0 ? p.text.slice(at + 1) : '').replace(/[（(][^）)]*[）)]/g, '');
        // 「X：Y部」「X：467《圭部》」是目录里的部名索引行，不是字族表
        const isCrossRef = /[《》]/.test(famText) || famText.includes('部');
        lastHead = {
          char: ch[0],
          variants: mHead[2] ? onlyHan(mHead[2]) : '',
          // 字族表：冒号后面那串（牡 社 仕…），用来给没写异体的字形行认主
          family: isCrossRef ? '' : famText,
        };
        heads.push(lastHead);
        partHeads.push(lastHead);
        // 字族表：冒号后面那串字头，按原稿顺序记下来（配图要挂到各自的字头后面）
        const famChars = isCrossRef ? [] : [...new Set(onlyHan(famText))];
        if (famChars.length) families.set(lastHead.char, famChars);
        lastHead.familyChars = famChars;
        owner = lastHead.char;
        sectionOwner = lastHead.char;
        inFamily = false;
      }
    }

    const t0 = (p.text || '').trim();
    if (/^字族衍義/.test(t0)) inFamily = true;
    // 字族衍義里每个衍生字的定义行（「牡（𡉯𤚴𪋂）mǔ《說文》…」），配图跟着它走
    if (inFamily) {
      const mDef = t0.match(/^([\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\u{20000}-\u{2FA1F}])(?:[（(][^）)]*[）)])?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+\s*[《【]/u);
      if (mDef) owner = mDef[1];
    }

    // 实物配图：单独一张图，紧跟一段「▲说明」
    if (p.imgs.length === 1 && !ROW.test(p.text) && owner) {
      const next = paras.slice(pi + 1, pi + 3).find((q) => q.text.trim() || q.imgs.length);
      const caption = next ? captionOf(next) : '';
      if (caption) photos.push({ char: owner, rid: p.imgs[0], caption });
      continue;
    }

    if (!p.imgs.length || !ROW.test(p.text)) continue;
    rows += 1;
    const variants = onlyHan(p.text.match(ROW)[1]);
    let head = null;
    if (variants) {
      head = heads.find((h) => h.variants && h.variants === variants) ||
        heads.find((h) => h.variants && [...h.variants].every((c) => variants.includes(c)));
    } else {
      // 行里只有拼音（如「（shì）：」）：看下面的分组标签在谁的字族表里
      const labels = [...p.text].filter((c) => LABEL.test(c));
      if (labels.length) {
        head = [...heads].reverse().find((h) => h.family && labels.every((c) => h.family.includes(c))) || null;
      }
      if (!head && lastPart) {
        head = heads.find((h) => h.char === lastPart && !usedHeads.has(h)) || null;
      }
    }
    // 还认不出来：按字头出现顺序取下一个没用过的（原稿里字形行与字族表是分开排的）
    if (!head) head = partHeads.find((h) => !usedHeads.has(h)) || heads.find((h) => !usedHeads.has(h)) || null;
    if (head) usedHeads.add(head);
    if (!head) unmatched += 1;
    if (head) {
      owner = head.char;
      sectionOwner = head.char;
      inFamily = false;
    }

    const groups = [];
    let cur = [];
    const flush = (label) => {
      if (cur.length) groups.push({ label, rids: cur });
      cur = [];
    };
    for (const t of p.toks) {
      if (t.t === 'img') { cur.push(t.rid); continue; }
      for (const c of (t.s || '')) {
        if (c === '。') flush('');
        else if (LABEL.test(c)) flush(c);
      }
    }
    flush('');

    for (const g of groups) {
      const canonical = g.label || (head ? head.char : '');
      if (!canonical) continue;
      entries.push({ char: canonical, variants: g.label ? '' : variants, rids: g.rids });
    }
  }
  return { entries, photos, families, rows, unmatched };
}

// ---------- 主流程 ----------

// 数字命名的文档（2.docx…）用首段「2.奚部」当标题
function docTitleOf(docName, parsed) {
  const base = docName.replace(/\.docx$/i, '');
  if (!/^\d+$/.test(base)) return base.trim();
  const first = (parsed.paras.find((p) => p.text.trim()) || {}).text || '';
  return first.replace(/^\d+\s*[.．、]\s*/, '').trim() || base;
}

function main() {
  if (!existsSync(SRC)) {
    console.error('源目录不存在：' + SRC);
    process.exit(1);
  }
  const docs = readdirSync(SRC)
    .filter((f) => f.toLowerCase().endsWith('.docx') && !f.startsWith('~$'))
    .sort((a, b) => (a.startsWith('卷') === b.startsWith('卷') ? a.localeCompare(b, 'zh') : a.startsWith('卷') ? -1 : 1));
  ONLY = new Set(onlyHan(arg('only', '')));

  // --families-only：只补索引里的「字族表」，不动已抽好的图片（源文档比图库新时用）
  if (argv.includes('--families-only')) {
    const indexPath = join(OUT, 'index.json');
    if (!existsSync(indexPath)) {
      console.error('索引不存在，无法只补字族表：' + indexPath);
      process.exit(1);
    }
    const idx = JSON.parse(readFileSync(indexPath, 'utf8'));
    // 字族表完全由原稿推导，整表重建，避免旧索引里残留的错条
    const fam = {};
    let added = 0;
    for (const docName of docs) {
      let res;
      try {
        res = extractChars(parseDocx(join(SRC, docName)));
      } catch {
        continue;
      }
      for (const [c, arr] of res.families) {
        if (fam[c]) continue;
        fam[c] = arr;
        added += 1;
      }
    }
    idx.families = fam;
    writeFileSync(indexPath, JSON.stringify(idx));
    console.log(JSON.stringify({ families: Object.keys(fam).length, added, chars: Object.keys(idx.chars).length }));
    return;
  }

  // 每次重建都清空，否则上一轮多出来的图会留在磁盘上（索引里已经没有它们）
  if (!ONLY.size) {
    rmSync(OUT, { recursive: true, force: true });
  }
  mkdirSync(OUT, { recursive: true });

  const index = { generated: new Date().toISOString(), source: '《系统汉语》各卷 Word 原稿', chars: {}, photos: {}, families: {} };
  const report = { docs: 0, rows: 0, unmatched: 0, chars: 0, photos: 0, families: 0, files: 0, bytes: 0 };

  for (const docName of docs) {
    const file = join(SRC, docName);
    let parsed, res;
    try {
      parsed = parseDocx(file);
      res = extractChars(parsed);
    } catch (e) {
      console.error('跳过（解析失败）', docName, e.message);
      continue;
    }
    if (!res.rows) continue;
    report.docs += 1;
    report.rows += res.rows;
    report.unmatched += res.unmatched;
    for (const [c, arr] of res.families) if (!index.families[c]) index.families[c] = arr;

    // 同一字的多组图合并；异体共用一份图片：落在主字目录下，其余作别名指向它
    const byChar = new Map();
    for (const e of res.entries) {
      if (!HAN.test(e.char)) continue;
      if (!byChar.has(e.char)) byChar.set(e.char, { char: e.char, variants: '', rids: [] });
      const cur = byChar.get(e.char);
      cur.rids.push(...e.rids);
      if (e.variants) cur.variants = e.variants;
    }

    for (const [ch, entry] of byChar) {
      if (ONLY.size && !ONLY.has(ch)) continue;
      const prev = index.chars[ch];
      if (prev && !prev.alias) continue; // 已有正条（别名可以被正条取代）
      const dir = join(OUT, ch);
      const files = [];
      for (const rid of [...new Set(entry.rids)]) {
        const media = parsed.rels.get(rid);
        if (!media) continue;
        const ext = extname(media).toLowerCase();
        if (!['.png', '.jpg', '.jpeg', '.webp', '.gif'].includes(ext)) continue;
        const data = parsed.zip.read('word/media/' + media);
        if (!data || data.length > MAX_BYTES) continue;
        mkdirSync(dir, { recursive: true });
        const name = String(files.length + 1).padStart(2, '0') + (ext === '.jpeg' ? '.jpg' : ext);
        writeFileSync(join(dir, name), data);
        files.push(`${ch}/${name}`);
        report.files += 1;
        report.bytes += data.length;
        if (files.length >= MAX_PER_CHAR) break;
      }
      if (!files.length) continue;
      const docTitle = docTitleOf(docName, parsed);
      index.chars[ch] = { doc: docTitle, variants: entry.variants, files };
      for (const v of onlyHan(entry.variants)) {
        if (v === ch || index.chars[v]) continue;
        index.chars[v] = { doc: docTitle, variants: entry.variants, alias: ch, files };
      }
    }

    // 实物配图（图下带 ▲ 说明）：单独放 photos/<字>/，说明文字进索引
    for (const ph of res.photos) {
      if (!HAN.test(ph.char)) continue;
      if (ONLY.size && !ONLY.has(ph.char)) continue;
      const media = parsed.rels.get(ph.rid);
      if (!media) continue;
      const ext = extname(media).toLowerCase();
      if (!['.png', '.jpg', '.jpeg', '.webp', '.gif'].includes(ext)) continue;
      const data = parsed.zip.read('word/media/' + media);
      if (!data || data.length > MAX_BYTES) continue;
      const list = (index.photos[ph.char] = index.photos[ph.char] || []);
      if (list.length >= 6) continue;
      const dir = join(OUT, 'photos', ph.char);
      mkdirSync(dir, { recursive: true });
      const name = String(list.length + 1).padStart(2, '0') + (ext === '.jpeg' ? '.jpg' : ext);
      writeFileSync(join(dir, name), data);
      list.push({ file: `photos/${ph.char}/${name}`, caption: ph.caption });
      report.files += 1;
      report.bytes += data.length;
    }
  }

  report.chars = Object.keys(index.chars).length;
  report.photos = Object.values(index.photos).reduce((n, a) => n + a.length, 0);
  report.families = Object.keys(index.families).length;
  // --merge：与已有索引合并（配合 --only 补抽个别字），已有条目保留、只补缺的
  const indexPath = join(OUT, 'index.json');
  if (argv.includes('--merge') && existsSync(indexPath)) {
    const old = JSON.parse(readFileSync(indexPath, 'utf8'));
    for (const [k, v] of Object.entries(index.chars)) if (!old.chars[k]) old.chars[k] = v;
    for (const [k, v] of Object.entries(index.photos)) if (!old.photos[k]) old.photos[k] = v;
    old.families = { ...index.families, ...(old.families || {}) };
    writeFileSync(indexPath, JSON.stringify(old));
    report.merged = true;
    report.chars = Object.keys(old.chars).length;
    console.log(JSON.stringify(report, null, 2));
    return;
  }
  writeFileSync(indexPath, JSON.stringify(index));
  console.log(JSON.stringify(report, null, 2));
}

main();

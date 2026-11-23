#!/usr/bin/env node
// check-spa-render.mjs — 站内页面（SPA）渲染体检：用 stub DOM 在 Node 里跑 index.html 的 cardBody，
// 逐张卡看是否抛错 / 渲染为空 / 表格渲染失败。专抓 verify-card 抓不到的数据形状问题
// （典型：族表行被多包一层，row[3] 是 list → esc() 拿到非字符串，整页只剩 "[异步出错]"）。
//
// 用法：
//   node tools/check-spa-render.mjs 宿 束 索          # 指定字
//   node tools/check-spa-render.mjs --buses 371-379   # 按部号段，可逗号分隔多段
//   node tools/check-spa-render.mjs --all             # 全库（约 1.8 万卡，一两分钟）
//
// 退出码：有 bad 即 1。零依赖，只用 node 内置模块。

import { readFileSync, readdirSync } from 'node:fs';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import vm from 'node:vm';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, '..');
const PUB = join(ROOT, 'web', 'public');
const CARDS = join(PUB, 'cards');
const SKIP = new Set(['index.json', 'variants.json', 'alias-index.json', 'root-variants.json']);

// ---------- stub DOM / fetch ----------
function el(id) {
  return {
    id, innerHTML: '', textContent: '', value: '', dataset: {},
    querySelectorAll: () => [], addEventListener: () => {}, appendChild: () => {},
  };
}
const els = new Map();
const getEl = (sel) => { if (!els.has(sel)) els.set(sel, el(sel)); return els.get(sel); };

globalThis.document = {
  querySelector: (s) => getEl(s),
  querySelectorAll: () => [],
  getElementById: (s) => getEl('#' + s),
  createElement: () => el('tmp'),
  body: { appendChild: () => {} },
  addEventListener: () => {},
};
globalThis.window = globalThis;

async function fetchStub(url) {
  let clean = String(url).split('?')[0].replace(/^\//, '');
  try { clean = decodeURIComponent(clean); } catch { /* keep raw */ }
  const p = resolve(PUB, clean);
  if (!p.startsWith(PUB)) throw new Error('bad path ' + url);
  try {
    const text = readFileSync(p, 'utf8');
    return { ok: true, status: 200, json: async () => JSON.parse(text), text: async () => text };
  } catch {
    return { ok: false, status: 404, json: async () => null, text: async () => '' };
  }
}
globalThis.fetch = fetchStub;

// ---------- 载入 SPA 脚本 ----------
const html = readFileSync(join(PUB, 'index.html'), 'utf8');
const blocks = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]);
const app = blocks.find((b) => b.includes('const $=s=>document.querySelector'));
if (!app) {
  console.error('index.html 里找不到应用脚本');
  process.exit(1);
}
const unhandled = [];
process.on('unhandledRejection', (e) => { unhandled.push(e); });
vm.runInThisContext(app, { filename: 'index.html:script' });
await new Promise((r) => setTimeout(r, 800));

// ---------- 目标字 ----------
const argv = process.argv.slice(2);
let chars = [];
if (argv[0] === '--all') {
  chars = readdirSync(CARDS).filter((f) => f.endsWith('.json') && !SKIP.has(f)).map((f) => f.slice(0, -5));
} else if (argv[0] === '--buses' && argv[1]) {
  const ranges = argv[1].split(',').map((s) => s.split('-').map(Number));
  for (const f of readdirSync(CARDS)) {
    if (!f.endsWith('.json') || SKIP.has(f)) continue;
    try {
      const c = JSON.parse(readFileSync(join(CARDS, f), 'utf8'));
      const n = c && c.bus && c.bus.num;
      if (typeof n === 'number' && ranges.some((r) => n >= r[0] && n <= (r[1] ?? r[0]))) chars.push(c.char);
    } catch { /* 坏卡交给 verify-card */ }
  }
} else {
  chars = argv.filter((a) => !a.startsWith('-'));
}
if (!chars.length) {
  console.error('用法：check-spa-render.mjs <字...> | --buses 371-379 | --all');
  process.exit(2);
}

// ---------- 逐张跑 ----------
let bad = 0;
for (const ch of chars) {
  try {
    await globalThis.open(ch);
    const h = getEl('#main').innerHTML;
    if (!h || h.length < 50) { console.log('EMPTY', ch, h.length); bad += 1; }
    else if (h.includes('表格渲染失败')) { console.log('TABLE-ERR', ch); bad += 1; }
  } catch (e) {
    console.log('THROW', ch, e && e.message);
    bad += 1;
  }
}
for (const e of unhandled.slice(0, 10)) console.log('UNHANDLED', e && e.message);
console.log(`checked ${chars.length} bad ${bad}`);
process.exit(bad ? 1 : 0);

// tools/zigen-index.mjs — 从「全书目录与结构」生成字根分级索引（构建期工具，不入运行时链路）
//
// 目的：释字要先定性——一级字根＝609 部的部首字，二级、三级字根与谐声字都在部内。
// 这个脚本只做一件事：把 `knowledge/hanzi-origin/mulu.md` 里 100 个卷条目正文中的
// 「8 㠯部（p22）」这类部名，抽成 `web/public/zigen.json`，供字卡按字查级。
//
// 用法：node tools/zigen-index.mjs [--check]

import { readFile, writeFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SRC = join(ROOT, 'knowledge', 'hanzi-origin', 'mulu.md');
const OUT = join(ROOT, 'web', 'public', 'zigen.json');

const CN = { 一: 1, 二: 2, 三: 3, 四: 4, 五: 5, 六: 6, 七: 7, 八: 8, 九: 9, 十: 10 };
function cn2num(s) {
  if (/^\d+$/.test(s)) return Number(s);
  if (s === '一百') return 100;
  if (s.startsWith('十')) return 10 + (CN[s[1]] || 0);
  if (s.endsWith('十')) return (CN[s[0]] || 0) * 10;
  if (s.includes('十')) {
    const [a, b] = s.split('十');
    return (CN[a] || 1) * 10 + (CN[b] || 0);
  }
  return CN[s] || 0;
}

const text = await readFile(SRC, 'utf8');
const claims = [...text.matchAll(/<!-- CLAIM:START (clm_[0-9A-Fa-f]+) -->\r?\n([\s\S]*?)<!-- CLAIM:END \1 -->/g)];

const chapters = [];
const juan = [];
let bad = [];

for (const [, id, chunk] of claims) {
  const title = (chunk.match(/^### (.+)$/m) || [])[1] || '';
  const mCh = title.match(/^第(.+?)章 (\S+?)：卷(\S+?)至卷(\S+?)，第(\d+)–(\d+)部/);
  if (mCh) {
    chapters.push({ no: cn2num(mCh[1]), name: mCh[2], from: Number(mCh[5]), to: Number(mCh[6]) });
    continue;
  }
  const mJ = title.match(/^卷(\S+?) (\S+?)：第(\d+)–(\d+)部（p(\d+)–p(\d+)）/);
  if (!mJ) continue;
  const body = chunk;
  const entries = [...body.matchAll(/(\d+)\s+(\S+?)部（p(\d+)）/g)]
    .map((m) => ({ no: Number(m[1]), name: m[2], p: Number(m[3]) }))
    .filter((e) => e.name && !/[（）、，。；]/.test(e.name));
  if (!entries.length) { bad.push(title); continue; }
  // 部首字本身没能转录的部（如第554部用符号字排印）：保留部号与页码，name 置 null
  for (const m of body.matchAll(/(\d+)\s+部（p(\d+)/g)) {
    const no = Number(m[1]);
    if (!entries.some((e) => e.no === no)) entries.push({ no, name: null, p: Number(m[2]) });
  }
  entries.sort((a, b) => a.no - b.no);
  juan.push({
    no: cn2num(mJ[1]),
    name: mJ[2],
    from: Number(mJ[3]),
    to: Number(mJ[4]),
    p: [Number(mJ[5]), Number(mJ[6])],
    claim: id,
    bu: entries,
  });
}

juan.sort((a, b) => a.no - b.no);
const byName = {};
const unnamed = [];
const nums = [];
for (const j of juan) {
  for (const b of j.bu) {
    nums.push(b.no);
    if (b.name) byName[b.name] = { no: b.no, juanNo: j.no, juanName: j.name, p: b.p, claim: j.claim };
    else unnamed.push(b.no);
  }
}
nums.sort((a, b) => a - b);
const missing = [];
for (let i = 1; i <= 609; i++) if (!nums.includes(i)) missing.push(i);

const out = {
  source: 'knowledge/hanzi-origin/mulu.md',
  generated: new Date().toISOString(),
  total: nums.length,
  expected: 608, // 609 部中第223部原书目录即缺
  missing,
  unnamed,
  chapters,
  juan,
  byName,
};

// 完整性自检：部数、章数、卷数、部号连续
const problems = [];
if (nums.length !== 608) problems.push(`部数 ${nums.length} ≠ 608`);
if (juan.length !== 100) problems.push(`卷数 ${juan.length} ≠ 100`);
if (chapters.length !== 12) problems.push(`章数 ${chapters.length} ≠ 12`);
if (missing.join(',') !== '223') problems.push(`缺部号 ${missing.join(',')}`);

if (process.argv.includes('--check')) {
  console.log(JSON.stringify({ total: out.total, juan: juan.length, chapters: chapters.length, missing, problems }, null, 2));
} else {
  await writeFile(OUT, JSON.stringify(out), 'utf8');
  console.log(`写出 ${OUT}：${out.total} 部 / ${juan.length} 卷 / ${chapters.length} 章`);
  if (problems.length) console.log('自检问题：\n- ' + problems.join('\n- '));
}
if (problems.some((p) => p.startsWith('部数'))) process.exitCode = 1;

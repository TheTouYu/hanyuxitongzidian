import io, json, re, sys, collections, glob, os

ROOT = r'D:\系统汉字'
OUT = ROOT + r'\intake\_tmp_bound_map.json'

# ---------- 1. 目录：卷 -> [(部号, 部首字)] ----------
mulu = io.open(ROOT + r'\knowledge\hanzi-origin\mulu.md', encoding='utf-8').read()
vols = {}
for m in re.finditer(r'### 卷([一二三四五六七八九十百]+) ([^\s：]+)：第(\d+)–(\d+)部[^\n]*\n\n(.*?)\n\n####', mulu, re.S):
    parts = re.findall(r'(\d+) ([^\s（）、]+)部（p\d+）', m.group(5))
    if parts:
        vols[m.group(1)] = [(int(n), ch) for n, ch in parts]

file_vol = {
    '01-ji.md': '一', '02a-yi.md': '二', '02b-shi-shi.md': '二', '02c-di.md': '二',
    '03a-shi.md': '三', '03b-shi-shu.md': '三', '03c-qi-ci-zi.md': '三', '03d-yi-jie.md': '三',
    '04a-yi.md': '四',
}
vol_label = {'一': '卷一「雞」', '二': '卷二「㠯」', '三': '卷三「矢」', '四': '卷四「弋」'}

# ---------- 2. claims ----------
claim_re = re.compile(
    r'<!-- CLAIM:START (clm_\w+) -->\s*\n+### (.*?)\n\n(.*?)\n\n#### 适用边界\n\n(.*?)\n\n<!-- CLAIM:END', re.S)
rows = []
for path in sorted(glob.glob(ROOT + r'\knowledge\**\*.md', recursive=True)):
    rel = os.path.relpath(path, ROOT).replace('\\', '/')
    text = io.open(path, encoding='utf-8').read()
    for i, m in enumerate(claim_re.finditer(text)):
        rows.append({'id': m.group(1), 'file': rel, 'idx': i,
                     'title': m.group(2).strip(), 'statement': m.group(3).strip(),
                     'old_boundary': m.group(4).strip()})

# ---------- 3. 逐条定部：按标题主语字 ----------
def subject_of(title):
    t = title.strip()
    if t.startswith('卷首'):
        return None
    if t and t[0] in '「『':
        return t[1] if len(t) > 1 else None
    return t[0] if t else None

by_file = collections.OrderedDict()
for r in rows:
    by_file.setdefault(os.path.basename(r['file']), []).append(r)

report = io.open(ROOT + r'\intake\_tmp_bound_report.txt', 'w', encoding='utf-8')
for base, items in by_file.items():
    vol = file_vol.get(base)
    if vol is None:
        kind = '目录' if base == 'mulu.md' else '绪论'
        for r in items:
            r['kind'] = kind
        continue
    parts = vols.get(vol, [])
    bu_by_char = {ch: (n, ch) for n, ch in parts}
    cur = None
    seq = []
    for r in items:
        title = r['title']
        if title.startswith('卷首'):
            r['kind'] = '卷首'
            r['vol'] = vol
            seq.append('首')
            continue
        subj = subject_of(title)
        hit = bu_by_char.get(subj) if subj else None
        if hit:
            if cur and cur[0] != hit[0]:
                report.write('JUMP %s %s : %s -> %s | %s\n' % (r['id'], base, cur, hit, title[:40]))
            cur = hit
        if cur is None or (base == '01-ji.md' and not hit):
            r['kind'] = '卷首'
        else:
            r['kind'] = '部'; r['bu_num'], r['bu_char'] = cur
        r['vol'] = vol
        seq.append(cur[0] if cur else '首')
    # 压缩显示序列
    runs = []
    for s in seq:
        if runs and runs[-1][0] == s:
            runs[-1][1] += 1
        else:
            runs.append([s, 1])
    report.write('%s: %s\n' % (base, ' '.join('%s×%d' % (s, n) if n > 1 else str(s) for s, n in runs)))

def new_boundary(r):
    k = r['kind']
    if k == '部':
        return '源自《系统汉语》第%d部「%s部」。' % (r['bu_num'], r['bu_char'])
    if k == '卷首':
        return '源自《系统汉语》%s卷首。' % vol_label[r['vol']]
    if k == '目录':
        return '源自《系统汉语》全书目录。'
    return '源自《系统汉语》绪论。'

for r in rows:
    r['new_boundary'] = new_boundary(r)
    if 'kind' not in r:
        r['kind'] = '?'
json.dump(rows, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

c = collections.Counter((os.path.basename(r['file']), r['new_boundary']) for r in rows)
report.write('\n=== 新 boundary 分布 ===\n')
for (f, b), n in sorted(c.items()):
    report.write('%s | %s | %d\n' % (f, b, n))
report.write('\n=== 卷首条目 ===\n')
for r in rows:
    if r['kind'] == '卷首':
        report.write('%s %s | %s\n' % (r['id'], os.path.basename(r['file']), r['title'][:46]))
report.close()
print('rows', len(rows))

"""Parse the extracted 目录 text into a chapter/volume/section tree; diagnostics."""
import json, re, sys, io

SRC = r'intake\_tmp_mulu.txt'
lines = io.open(SRC, encoding='utf-8').read().split('\n')

chapters, volumes, sections = [], [], []
cur_ch = cur_vol = None
bad = []
for i, raw in enumerate(lines, 1):
    s = raw.strip()
    if not s or s == '目 錄':
        continue
    m = re.match(r'^第([一二三四五六七八九十]+)章\s*(\S+)$', s)
    if m:
        cur_ch = {'no': m.group(1), 'name': m.group(2), 'line': i, 'volumes': []}
        chapters.append(cur_ch)
        continue
    m = re.match(r'^卷([^\s\d]+)\s*(\S*?)\s*(\d+)?$', s)
    if m and (m.group(2) or m.group(3)):
        no, name, page = m.group(1), m.group(2), m.group(3)
        cur_vol = {'no': no, 'name': name, 'page': int(page) if page else None, 'line': i, 'sections': []}
        volumes.append(cur_vol)
        if cur_ch is not None:
            cur_ch['volumes'].append(cur_vol)
        continue
    m = re.match(r'^(\d+)\.\s*(\S*?)\s*部\s*(\d+)$', s)
    if m:
        num, name, page = int(m.group(1)), m.group(2), int(m.group(3))
        sec = {'num': num, 'name': name, 'page': page, 'line': i}
        sections.append(sec)
        if cur_vol is not None:
            cur_vol['sections'].append(sec)
        continue
    bad.append((i, s))

out = {'chapters': chapters, 'volumes': volumes, 'sections': sections, 'unparsed': bad}
io.open(r'intake\_tmp_mulu.json', 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=1))

rep = []
rep.append('chapters=%d volumes=%d sections=%d unparsed=%d' % (len(chapters), len(volumes), len(sections), len(bad)))
for ch in chapters:
    rep.append('CH 第%s章 %s: volumes=%s sections=%d..%s' % (
        ch['no'], ch['name'], ' '.join(v['no'] + v['name'] for v in ch['volumes']), 
        ch['volumes'][0]['sections'][0]['num'] if ch['volumes'] and ch['volumes'][0]['sections'] else '-',
        ch['volumes'][-1]['sections'][-1]['num'] if ch['volumes'] and ch['volumes'][-1]['sections'] else '-'))
nums = [s['num'] for s in sections]
rep.append('section numbers monotonic: %s' % all(b == a + 1 for a, b in zip(nums, nums[1:])))
for a, b in zip(nums, nums[1:]):
    if b != a + 1:
        rep.append('BREAK %d -> %d' % (a, b))
for s in sections:
    if not s['name']:
        rep.append('EMPTY NAME at num=%d line=%d' % (s['num'], s['line']))
for v in volumes:
    if not v['name']:
        rep.append('EMPTY VOL NAME at 卷%s line=%d' % (v['no'], v['line']))
rep.append('UNPARSED:')
for i, s in bad:
    rep.append('  %d: %s' % (i, s))
io.open(r'intake\_tmp_mulu_report.txt', 'w', encoding='utf-8').write('\n'.join(rep))
print('ok')

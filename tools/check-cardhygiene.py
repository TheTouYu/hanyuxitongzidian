# -*- coding: utf-8 -*-
"""卡片卫生检查：①栏首标签残留（text/paras）②zizu.text 与组题重复"""
import io, json, os, re, sys

sys.stdout.reconfigure(encoding='utf-8')
CARD_DIR = 'web/public/cards'
LABEL = re.compile(r'^\s*(本義|轉義|辯證|音源|字形|字族衍義|聲母擬態|所属卷|釋義)[：:]')
skip = {'index.json', 'variants.json', 'alias-index.json'}
bad_label, dup = [], []
for f in sorted(os.listdir(CARD_DIR)):
    if not f.endswith('.json') or f in skip:
        continue
    c = json.load(io.open(os.path.join(CARD_DIR, f), encoding='utf-8'))
    for s in c.get('sections', []):
        t = s.get('text')
        if isinstance(t, str):
            for line in t.split('\n'):
                if LABEL.match(line):
                    bad_label.append((f, s['key'], line[:20]))
                    break
        for p in (s.get('paras') or []):
            if isinstance(p, str) and LABEL.match(p):
                bad_label.append((f, s['key'] + '.paras', p[:20]))
                break
        if s.get('key') == 'zizu' and isinstance(t, str) and t.strip():
            for g in s.get('groups', []):
                if t.strip() == (g.get('title') or '').strip():
                    dup.append((f, t[:24]))
                    break
print('label', len(bad_label))
for x in bad_label[:10]:
    print('  ', x)
print('dup-zizu', len(dup))
for x in dup[:10]:
    print('  ', x)

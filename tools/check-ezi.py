# -*- coding: utf-8 -*-
"""校验：讹字组（标题含 訛/譌/形近）的落点必须是原文全录，不得带搭桥（——）。"""
import io, json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
C = 'web/public/cards'
bad = []
for f in os.listdir(C):
    if not f.endswith('.json') or f in ('index.json', 'alias-index.json', 'variants.json'):
        continue
    try:
        d = json.load(io.open(os.path.join(C, f), encoding='utf-8'))
    except Exception:
        continue
    for s in d.get('sections', []):
        if s.get('key') != 'zizu':
            continue
        for g in s.get('groups', []):
            if not any(k in g.get('title', '') for k in ('訛', '譌', '形近')):
                continue
            for r in g.get('rows', []):
                lp = r[3] if len(r) > 3 else ''
                if '——' in lp:
                    bad.append((f[:-5], r[0], lp[:50]))
for b in bad:
    print(b)
print('bad', len(bad))

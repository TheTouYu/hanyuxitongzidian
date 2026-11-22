# -*- coding: utf-8 -*-
import io, json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, 'web', 'public', 'cards')


def rowtail(t):
    cut = min([i for i in (t.find('《'), t.find('“'), t.find('「')) if i > 0] or [0])
    return t[cut:]


cm = json.load(io.open(os.path.join(ROOT, '.tmp-charmap.json'), encoding='utf-8'))
fixed = skipped = 0
for fn in sorted(os.listdir(CARDS)):
    if not fn.endswith('.json'):
        continue
    p = os.path.join(CARDS, fn)
    try:
        c = json.load(io.open(p, encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(c, dict) or c.get('level') != 3:
        continue
    ch = c.get('char') or fn[:-5]
    info = cm.get(ch) or cm.get(fn[:-5])
    if not info:
        continue
    tail = rowtail(info['txt'])
    if not tail:
        continue
    changed = False
    for s in c.get('sections') or []:
        if s.get('key') != 'shiyi':
            continue
        cur = s.get('text') or ''
        if '{{' in cur or '{{' in tail:
            skipped += 1
            break
        if cur != tail:
            s['text'] = tail
            s['paras'] = [tail]
            changed = True
    if changed:
        json.dump(c, io.open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        fixed += 1
print('fixed', fixed, 'skipped(inline)', skipped)

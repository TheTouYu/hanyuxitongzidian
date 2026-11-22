# -*- coding: utf-8 -*-
"""校验族卡「釋義」是否为原稿整行照录（只允许剥去行首的字头与拼音）。

用法：python tools/check-shiyi.py [--limit N] [--fix-list out.json]
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, 'web', 'public', 'cards')


def norm(s):
    s = re.sub(r'\s+', '', s or '')
    s = s.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    s = s.replace('：', ':').replace('，', ',')
    return s


PINYIN = 'a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹḿ'
HEAD_RE = re.compile(
    r'^[\u3400-\u9fff\U00020000-\U0002a6df]{1,4}'
    r'(?:[（(][^）)]*[）)])?'
    r'[\s、，,]*[%s]+(?:[\s、，,]+[%s]+)*[\s、，,：:]*' % (PINYIN, PINYIN))


def rowtail(t):
    """剥去行首字头（含括注）与拼音，返回原文剩余部分。"""
    t = (t or '').strip()
    m = HEAD_RE.match(t)
    if m:
        rest = t[m.end():]
        if rest:
            return rest
    # 没有拼音的行：字头后直接是书证或冒号
    cut = min([i for i in (t.find('《'), t.find('“'), t.find('「')) if 0 < i <= 12] or [0])
    if cut:
        return t[cut:]
    m2 = re.match(r'^[\u3400-\u9fff\U00020000-\U0002a6df]{1,4}[：:]?', t)
    return t[m2.end():] if m2 else t


def main():
    cm = json.load(io.open(os.path.join(ROOT, '.tmp-charmap.json'), encoding='utf-8'))
    bad = []
    total = 0
    for fn in sorted(os.listdir(CARDS)):
        if not fn.endswith('.json'):
            continue
        ch = fn[:-5]
        try:
            c = json.load(io.open(os.path.join(CARDS, fn), encoding='utf-8'))
        except Exception:
            continue
        if not isinstance(c, dict) or c.get('level') != 3:
            continue
        shiyi = None
        for s in c.get('sections') or []:
            if s.get('key') == 'shiyi':
                shiyi = s.get('text') or ''
        if shiyi is None:
            continue
        info = cm.get(ch) or cm.get(c.get('char', ''))
        if not info:
            continue
        total += 1
        tail = norm(rowtail(info['txt']))
        if norm(shiyi) != tail:
            bad.append({'char': ch, 'card': norm(shiyi)[:80], 'orig': tail[:80]})
    print('checked', total, 'violations', len(bad))
    for b in bad[:40]:
        print(' -', b['char'], '|', b['card'], '||', b['orig'])
    if len(sys.argv) > 2 and sys.argv[1] == '--fix-list':
        json.dump(bad, io.open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()

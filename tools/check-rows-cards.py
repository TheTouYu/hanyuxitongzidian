# -*- coding: utf-8 -*-
"""逐行核卡：部头字族表的每一行，首字必须有卡或别名路由。

用法：
    python tools\\check-rows-cards.py --bu 入 --bu 須 --bu 二 --bu 弱 --bu 惢
    python tools\\check-rows-cards.py --bu 入 --json .tmp-rows.json

红：有行无卡 → exit 1；绿：全部有落点 → exit 0。
"""
import argparse
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, 'web', 'public', 'cards')
SKIP = {'index.json', 'alias-index.json', 'variants.json'}
HAN = '\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323AF'
HEAD_RE = re.compile(r'^([%s]{1,4})(?:[（(]([^）)]*)[）)])?' % HAN)


def load(path):
    with io.open(path, encoding='utf-8') as f:
        return json.load(f)


def rows_of(card):
    out = []
    for s in card.get('sections') or []:
        if s.get('key') != 'zizu':
            continue
        for g in s.get('groups') or []:
            for r in g.get('rows') or []:
                if r and r[0]:
                    out.append((g.get('title') or '', r[0]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bu', action='append', required=True, help='部头字，可重复')
    ap.add_argument('--json')
    args = ap.parse_args()

    alias = load(os.path.join(CARDS, 'alias-index.json'))
    report = {'tool': 'check-rows-cards', 'version': 1, 'bus': [], 'missing': []}
    for bu in args.bu:
        p = os.path.join(CARDS, bu + '.json')
        if not os.path.exists(p):
            report['missing'].append({'bu': bu, 'char': bu, 'why': '部头无卡'})
            continue
        card = load(p)
        rows = rows_of(card)
        own = routed = 0
        for title, label in rows:
            m = HEAD_RE.match(label)
            ch = m.group(1) if m else label
            if os.path.exists(os.path.join(CARDS, ch + '.json')):
                own += 1
                continue
            if ch in alias:
                routed += 1
                continue
            report['missing'].append({'bu': bu, 'group': title, 'char': ch, 'row': label})
        report['bus'].append({'bu': bu, 'rows': len(rows), 'own': own, 'alias': routed,
                              'missing': len([x for x in report['missing'] if x['bu'] == bu])})
        print('部 %s：行 %d，有卡 %d，别名路由 %d，缺 %d' % (
            bu, len(rows), own, routed,
            len([x for x in report['missing'] if x['bu'] == bu])))

    for x in report['missing']:
        print('  缺: %s %s（%s）' % (x.get('bu'), x.get('char'), x.get('row', '')))
    if args.json:
        with io.open(args.json, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
            f.write('\n')
    print('RESULT %s · missing %d' % ('PASS' if not report['missing'] else 'FAIL',
                                      len(report['missing'])))
    sys.exit(1 if report['missing'] else 0)


if __name__ == '__main__':
    main()

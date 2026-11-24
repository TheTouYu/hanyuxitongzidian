# -*- coding: utf-8 -*-
"""扫「简体索引」缺口：拿 Windows LCMapStringW 把每个卡字/别名转成简体，
看 variants.json（简→繁）里有没有这一对。缺的列出来，人工确认后再 --apply。

用法：
    python tools/check-variants.py                 # 全库体检（只报数）
    python tools/check-variants.py --bu 371-379    # 只看某些部（卡 bus.num 段，逗号分隔）
    python tools/check-variants.py --json .tmp-var.json
    python tools/check-variants.py --apply         # 把「缺、且不在黑名单、且不撞车」的写进 variants.json
    python tools/check-variants.py --aliases       # 连卡的 aliases 一起扫（旧卡 aliases 有脏数据，慎用）

为什么不用手列：手写会漏（2026-11-23「辄」等 6 字就没进表，主人报「简化字没有建立索引」）。
LCMap 也有坑：个别字会给出非规范简化（坰→垧、牪→瘪 之类），所以默认只报不改，--apply 时跳过 BLOCK。
"""
import argparse
import ctypes
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, 'web', 'public', 'cards')
SKIP = {'index.json', 'variants.json', 'alias-index.json', 'root-variants.json'}
LCMAP_SIMPLIFIED_CHINESE = 0x02000000

# LCMap 明显错映射（简体不是该字的规范简化，或另有正字已收）
BLOCK = {
    '坰': '垧', '牪': '瘪', '脧': '睃', '芐': '苄', '鉆': '钻', '鐽': '钽',
    '戉': '钺', '啣': '衔', '廱': '痈', '鐉': '铣', '懍': '檩',
}

try:
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
except OSError:  # 非 Windows：工具不可用
    _k32 = None


def simp(ch):
    if _k32 is None or len(ch) != 1 or ord(ch) > 0xFFFF:
        return ch
    buf = ctypes.create_unicode_buffer(16)
    n = _k32.LCMapStringW(0x0804, LCMAP_SIMPLIFIED_CHINESE, ch, 1, buf, 16)
    return (buf.value[:1] or ch) if n else ch


def load_cards():
    cards = {}
    for f in glob.glob(os.path.join(CARDS, '*.json')):
        b = os.path.basename(f)[:-5]
        if b in SKIP:
            continue
        try:
            c = json.load(open(f, encoding='utf-8'))
        except Exception:
            continue
        if isinstance(c, dict):
            cards[c.get('char') or b] = c
    return cards


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bu', help='只扫这些部号，如 371-379 或 371,375')
    ap.add_argument('--json')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--aliases', action='store_true')
    args = ap.parse_args()

    if _k32 is None:
        print('非 Windows：LCMapStringW 不可用，退回手查')
        return 2

    cards = load_cards()
    vp = os.path.join(CARDS, 'variants.json')
    variants = json.load(open(vp, encoding='utf-8'))
    alias_owner = {}
    for ch, c in cards.items():
        for a in (c.get('aliases') or []):
            alias_owner.setdefault(a, ch)
    have = set(cards)

    wanted = None
    if args.bu:
        wanted = set()
        for part in args.bu.split(','):
            a, _, b = part.partition('-')
            lo, hi = int(a), int(b or a)
            wanted.update(range(lo, hi + 1))

    missing, blocked, collide = [], [], {}
    for ch, c in cards.items():
        if wanted is not None and (c.get('bus') or {}).get('num') not in wanted:
            continue
        s = simp(ch)
        if s == ch:
            continue
        if BLOCK.get(ch) == s:
            blocked.append((ch, s))
            continue
        if s in have or s in alias_owner:
            continue
        if s in variants:
            if variants[s] != ch:
                collide.setdefault(s, []).append(ch)
            continue
        missing.append((ch, s))

    print('cards', len(cards), 'variants', len(variants))
    print('missing', len(missing), 'blocked', len(blocked), 'collide', len(collide))
    for ch, s in sorted(missing):
        print('  MISS %s -> %s' % (ch, s))
    for ch, s in sorted(blocked):
        print('  SKIP %s -> %s（黑名单）' % (ch, s))
    for s, ts in sorted(collide.items()):
        print('  COLLIDE %s <- %s（已在表：%s）' % (s, ts, variants.get(s)))

    if args.json:
        with open(args.json, 'w', encoding='utf-8', newline='\n') as f:
            json.dump({'missing': missing, 'blocked': blocked, 'collide': collide},
                      f, ensure_ascii=False, indent=1)
            f.write('\n')

    if args.apply and missing:
        added = {}
        for ch, s in missing:
            if s in variants:
                continue
            variants[s] = ch
            added[s] = ch
        with open(vp, 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(variants, ensure_ascii=False, separators=(',', ':')))
        print('applied', len(added), '→ 记得跑 tools/build-card-index.py 同步 root variants 与 index')

    return 0


if __name__ == '__main__':
    sys.exit(main())

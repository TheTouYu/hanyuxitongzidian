#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""全卷插图总账：原稿独立图片段 vs 卡/photos 四处清单。

用法（零依赖，只用 stdlib）：
  python tools/audit-photos.py --doc "D:/字谱智能体/卷五十四  网.docx"
  python tools/audit-photos.py --doc ... --json .tmp-photo/audit.json
  python tools/audit-photos.py --doc ... --all      # 全库普查（默认只查本卷各部的字）

查五件事：
 1. 每部原稿独立图片段数 vs 该部各字照片数（取 顶层 photos ∪ 卡 photos，按文件名去重）；
    卷首段（首个 `NNN.X部` 之前）按规矩挂**紧随其后的部头卡**，计入该部。
 2. 图注：卡里/顶层写的图注必须能在本卷原稿 ▲ 段里找到；找不到 → 自造。
 3. 卡 photos 与 glyphs/index.json 顶层 photos 不同步（E054 的同一件事）。
 4. SPA 两清单（photos/index.json、photos/captions.json）缺条目 / 断链。
 5. 盘上有文件但两张清单都没引用（孤儿图）。

退出码：未落位 / 自造图注 / 卡不同步 / SPA 断链 任一 > 0 为 1。
"""
import argparse
import glob
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
PHOTOS = os.path.join('web', 'public', 'glyphs', 'photos')
GLYPH_INDEX = os.path.join('web', 'public', 'glyphs', 'index.json')
CARDS = os.path.join('web', 'public', 'cards')
BU_RE = re.compile(r'^\s*(\d{1,3})[.．]\s*(.+?)部\s*$')


def img_size(blob):
    """返回 (w, h)；认 PNG/JPEG/GIF/BMP，认不出返回 (0, 0)。"""
    try:
        if blob[:8] == b'\x89PNG\r\n\x1a\n':
            return int.from_bytes(blob[16:20], 'big'), int.from_bytes(blob[20:24], 'big')
        if blob[:2] == b'\xff\xd8':
            i = 2
            while i < len(blob) - 9:
                if blob[i] != 0xFF:
                    i += 1
                    continue
                m = blob[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3):
                    h = int.from_bytes(blob[i + 5:i + 7], 'big')
                    w = int.from_bytes(blob[i + 7:i + 9], 'big')
                    return w, h
                if m in (0xD8, 0xD9, 0x01) or 0xD0 <= m <= 0xD7:
                    i += 2
                    continue
                seg = int.from_bytes(blob[i + 2:i + 4], 'big')
                i += 2 + seg
            return 0, 0
        if blob[:6] in (b'GIF87a', b'GIF89a'):
            return int.from_bytes(blob[6:8], 'little'), int.from_bytes(blob[8:10], 'little')
        if blob[:2] == b'BM':
            return int.from_bytes(blob[18:22], 'little'), int.from_bytes(blob[22:26], 'little')
    except Exception:
        pass
    return 0, 0


def scan_docx(path):
    """→ [{para, text, images:[{rid, media, w, h, bytes}]}]，按段落顺序。"""
    z = zipfile.ZipFile(path)
    rels = ET.fromstring(z.read('word/_rels/document.xml.rels'))
    rmap = {}
    for rel in rels:
        rmap[rel.get('Id')] = rel.get('Target')
    root = ET.fromstring(z.read('word/document.xml'))
    body = root.find(W + 'body')
    out = []
    # 只取 body 的直接子段落：文本框（w:pict/w:txbxContent）里的嵌套 w:p 不是原稿段落，
    # 卷五十五 巫.docx 有 20 个这样的嵌套段，会把卷首/字形段的图重复计一遍（2026-11-22 修）。
    for pi, p in enumerate(p for p in body if p.tag == W + 'p'):
        text = ''.join(t.text or '' for t in p.iter(W + 't'))
        imgs = []
        seen = set()
        for el in p.iter():
            for k, v in el.attrib.items():
                if k.startswith(R) and v and v in rmap:
                    if v in seen:
                        continue
                    seen.add(v)
                    tgt = rmap[v]
                    media = 'word/' + tgt.lstrip('/')
                    if not media.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.emf', '.wmf')):
                        continue
                    try:
                        blob = z.read(media)
                    except KeyError:
                        continue
                    w, h = img_size(blob)
                    imgs.append({'rid': v, 'media': media, 'w': w, 'h': h, 'bytes': len(blob)})
        out.append({'para': pi, 'text': text, 'images': imgs})
    z.close()
    return out


def load_json(fp):
    with open(fp, encoding='utf-8') as f:
        return json.load(f)


def load_cards():
    cards = {}
    for fp in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        name = os.path.basename(fp)
        if name in ('index.json', 'alias-index.json', 'variants.json'):
            continue
        try:
            d = load_json(fp)
        except Exception:
            continue
        if isinstance(d, dict) and d.get('char'):
            cards[d['char']] = d
    return cards


def norm(s):
    return re.sub(r'\s+', '', s or '')


def base(f):
    return os.path.basename(str(f)) if f else ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--doc', required=True)
    ap.add_argument('--json')
    ap.add_argument('--all', action='store_true', help='全库普查（默认只查本卷各部的字）')
    ap.add_argument('--max', type=int, default=40)
    args = ap.parse_args()

    paras = scan_docx(args.doc)
    cards = load_cards()
    gi = load_json(GLYPH_INDEX)
    top = gi.get('photos') or {}
    spa = (load_json(os.path.join(PHOTOS, 'index.json')).get('photos') or {})
    caps = (load_json(os.path.join(PHOTOS, 'captions.json')).get('captions') or {})

    bus = []
    for pp in paras:
        m = BU_RE.match(pp['text'])
        if m:
            bus.append({'num': int(m.group(1)), 'name': m.group(2).strip(), 'para': pp['para']})

    def bu_of(para):
        cur = None
        for b in bus:
            if b['para'] < para:
                cur = b
        return cur

    # 独立图片段（有图无字）/ ▲ 图注段
    solo, capsegs = {}, []
    for pp in paras:
        if pp['images'] and not pp['text'].strip():
            b = bu_of(pp['para'])
            solo.setdefault(b['num'] if b else 0, []).append(pp)
        t = pp['text'].strip()
        if t.startswith('▲'):
            b = bu_of(pp['para'])
            capsegs.append({'para': pp['para'], 'bu': b['num'] if b else 0, 'text': t})
    doc_caps = set()
    for c in capsegs:
        # 一段可能有多条 ▲ 图注（卷首 P0035 即此例），▲ 与「两个以上空格」都算分隔
        for part in re.split(r'▲|\s{2,}', c['text']):
            part = part.strip()
            if part:
                doc_caps.add(norm(part))
                # 一注管两图，按左／右拆注（exegesis §二）
                m = re.match(r'^(.+?（左）)與(.+?（右）)$', part)
                if m:
                    doc_caps.add(norm(m.group(1)))
                    doc_caps.add(norm(m.group(2)))

    # 卷首段：按技能 §3.3 挂该卷卷卡（2026-11-22 主人裁）；无卷卡时退回首个部
    head_bu = bus[0]['num'] if bus else 0
    front = solo.pop(0, [])

    # 每字照片：顶层 ∪ 卡（按文件名去重）
    def photos_of(ch):
        out = {}
        for x in (top.get(ch) or []):
            f = x.get('file') if isinstance(x, dict) else x
            if f:
                out[base(f)] = (x.get('caption') if isinstance(x, dict) else '') or ''
        for x in (cards.get(ch, {}).get('photos') or []):
            f = x.get('file') if isinstance(x, dict) else x
            if f:
                out.setdefault(base(f), (x.get('caption') if isinstance(x, dict) else '') or '')
        return out

    by_bu = {}
    for ch, d in cards.items():
        n = (d.get('bus') or {}).get('num')
        by_bu.setdefault(n, []).append(ch)

    vol_chars = set()
    for b in bus:
        vol_chars.update(by_bu.get(b['num'], []))
    scope_chars = set(cards) if args.all else vol_chars

    problems = {'unplaced': [], 'extra': [], 'fakecap': [], 'unsync': [],
                'spa_missing': [], 'spa_bad': [], 'orphan': []}
    # 卷首图对账：doc 文件名去空格即该卷卷卡名（卷六十  𦟀 → 卷六十𦟀）；
    # 文件名带「部」而卷卡名不带（卷七十一  聿部.docx → 卷七十一聿）时回退一次。
    vol_card = re.sub(r'\s+', '', os.path.splitext(os.path.basename(args.doc))[0])
    if vol_card not in cards and vol_card.endswith('部') and vol_card[:-1] in cards:
        vol_card = vol_card[:-1]
    front_imgs = sum(len(pp['images']) for pp in front)
    if front:
        if vol_card in cards:
            vk = len(photos_of(vol_card))
            if vk < front_imgs:
                for pp in front:
                    problems['unplaced'].append({
                        'bu': 0, 'name': '卷首(%s)' % vol_card, 'para': pp['para'],
                        'images': [{'media': i['media'], 'w': i['w'], 'h': i['h'], 'bytes': i['bytes']}
                                   for i in pp['images']],
                    })
            elif vk > front_imgs:
                problems['extra'].append({'bu': 0, 'name': '卷首(%s)' % vol_card,
                                          'doc': front_imgs, 'cards': [(vol_card, vk)]})
        else:
            solo.setdefault(head_bu, [])[:0] = front
    rows = []
    for b in bus:
        n = b['num']
        n_doc = sum(len(pp['images']) for pp in solo.get(n, []))
        chs = by_bu.get(n, [])
        n_card = 0
        listed = []
        for ch in chs:
            k = len(photos_of(ch))
            if k:
                listed.append((ch, k))
            n_card += k
        rows.append((n, b['name'], n_doc, n_card, listed))
        if n_card < n_doc:
            for pp in solo.get(n, []):
                problems['unplaced'].append({
                    'bu': n, 'name': b['name'], 'para': pp['para'],
                    'images': [{'media': i['media'], 'w': i['w'], 'h': i['h'], 'bytes': i['bytes']}
                               for i in pp['images']],
                })
        if n_card > n_doc:
            problems['extra'].append({'bu': n, 'name': b['name'], 'doc': n_doc, 'cards': listed})

    # 卡 photos 与顶层 photos 同步
    for ch in sorted(vol_chars):
        tk = photos_of(ch)
        ck = {}
        for x in (cards[ch].get('photos') or []):
            f = x.get('file') if isinstance(x, dict) else x
            if f:
                ck[base(f)] = (x.get('caption') if isinstance(x, dict) else '') or ''
        tk_top = {base((x.get('file') if isinstance(x, dict) else x)): (x.get('caption') if isinstance(x, dict) else '') or ''
                  for x in (top.get(ch) or [])}
        if not tk_top:
            if ck:
                problems['unsync'].append({'char': ch, 'why': '卡有 photos，顶层没有'})
            continue
        if set(tk_top) != set(ck):
            problems['unsync'].append({'char': ch, 'why': '文件集不同',
                                       'top': sorted(tk_top), 'card': sorted(ck)})
        elif any(tk_top[k] != ck.get(k, '') for k in tk_top):
            problems['unsync'].append({'char': ch, 'why': '图注不同', 'top': tk_top, 'card': ck})

    # 图注必须来自本卷 ▲
    for ch in sorted(scope_chars):
        for name, cap in sorted(photos_of(ch).items()):
            if cap and norm(cap) not in doc_caps:
                problems['fakecap'].append({'char': ch, 'caption': cap})

    # SPA 两清单
    for ch in sorted(scope_chars):
        if not photos_of(ch):
            continue
        sp = spa.get(ch)
        if not sp:
            problems['spa_missing'].append(ch)
            continue
        names = [base(x.get('file') if isinstance(x, dict) else x) for x in sp]
        bad = [f for f in names if f and not os.path.exists(os.path.join(PHOTOS, ch, f))]
        if bad:
            problems['spa_bad'].append({'char': ch, 'files': bad})

    # 孤儿文件
    for dirp in sorted(glob.glob(os.path.join(PHOTOS, '*', ''))):
        ch = os.path.basename(dirp.rstrip('/\\'))
        if ch not in scope_chars:
            continue
        files = [f for f in os.listdir(dirp) if os.path.isfile(os.path.join(dirp, f))]
        ref = set()
        for x in (top.get(ch) or []):
            ref.add(base(x.get('file') if isinstance(x, dict) else x))
        for x in (spa.get(ch) or []):
            ref.add(base(x.get('file') if isinstance(x, dict) else x))
        miss = sorted(f for f in files if f and f not in ref)
        if miss:
            problems['orphan'].append({'char': ch, 'files': miss})

    print('audit-photos · %s' % args.doc)
    print('部 %d 个，独立图片段 %d 段（%d 张）· 卷首 %d 张 → 卷卡 %s' % (
        len(bus), sum(len(v) for v in solo.values()),
        sum(len(pp['images']) for v in solo.values() for pp in v),
        front_imgs, vol_card))
    print('%-5s %-8s %6s %6s  %s' % ('部号', '部名', '原稿', '卡里', '字'))
    for n, name, nd, nc, listed in rows:
        flag = '' if nd == nc else ('  ← 差 %+d' % (nc - nd))
        print('%-5d %-8s %6d %6d  %s%s' % (n, name, nd, nc,
                                           ' '.join('%s×%d' % (c, k) for c, k in listed), flag))

    def show(title, items, fmt):
        print('\n%s %d' % (title, len(items)))
        for it in items[:args.max]:
            print('  ' + fmt(it))
        if len(items) > args.max:
            print('  … 还有 %d 条' % (len(items) - args.max))

    show('未落位图片段', problems['unplaced'],
         lambda x: '部%d %s 段%d %s' % (x['bu'], x['name'], x['para'],
                                        ' '.join('%s %dx%d %dB' % (i['media'].split('/')[-1], i['w'], i['h'], i['bytes'])
                                                 for i in x['images'])))
    show('多出的部', problems['extra'],
         lambda x: '部%d %s 原稿%d 卡里 %s' % (x['bu'], x['name'], x['doc'], x['cards']))
    show('卡/顶层不同步', problems['unsync'],
         lambda x: '%s %s%s' % (x['char'], x['why'],
                                '' if x['why'] == '卡有 photos，顶层没有'
                                else ' top=%s card=%s' % (x.get('top'), x.get('card'))))
    show('自造图注（原稿无此 ▲）', problems['fakecap'],
         lambda x: '%s「%s」' % (x['char'], x['caption']))
    show('SPA 缺条目', problems['spa_missing'], lambda x: x)
    show('SPA 断链', problems['spa_bad'], lambda x: '%s %s' % (x['char'], x['files']))
    show('孤儿文件（两清单都没引用）', problems['orphan'],
         lambda x: '%s %s' % (x['char'], x['files']))

    if args.json:
        with open(args.json, 'w', encoding='utf-8', newline='\n') as f:
            json.dump({'doc': args.doc, 'bus': bus, 'rows': rows, 'problems': problems},
                      f, ensure_ascii=False, indent=1)
            f.write('\n')
        print('\njson → %s' % args.json)

    bad = (len(problems['unplaced']) + len(problems['unsync']) +
           len(problems['spa_bad']) + len(problems['fakecap']))
    print('\nRESULT %s · 未落位 %d · 不同步 %d · 自造注 %d · SPA缺 %d · SPA断链 %d · 孤儿 %d' % (
        'FAIL' if bad else 'PASS', len(problems['unplaced']), len(problems['unsync']),
        len(problems['fakecap']), len(problems['spa_missing']), len(problems['spa_bad']),
        len(problems['orphan'])))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

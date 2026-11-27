# -*- coding: utf-8 -*-
"""把插图（web/public/glyphs/photos/）缩到与页面相配的像素。

卡页插图按 max-height 220px 显示（web/public/*.html 的 .pscroll img），
server 端 /card/ 页按 height:170px 显示；故取 2 倍屏尺寸作上限：
高 ≤ --max-h（默认 440）、宽 ≤ --max-w（默认 1600）。

- 超限的图等比缩小（只缩不放），按原格式重存（JPEG q85 progressive、PNG optimize）
- 未超限但字节臃肿（> --bloated，默认 250KB）的图，原尺寸重编码瘦身
- 文件名、目录、扩展名一律不改：cards/*.json、glyphs/index.json、photos/index.json
  都按文件名引用，改名会断链
- 写盘走临时文件再替换；新文件不比旧的省就直接跳过（不劣化）

用法：
    python tools\\normalize-photos.py --dry-run
    python tools\\normalize-photos.py --dry-run --only 蚣 --only 輦
    python tools\\normalize-photos.py --json .tmp-photos-report.json

需要 Pillow（用自带 python：C:\\Users\\...\\dependencies\\python\\python.exe）。
"""
import argparse
import io
import json
import os
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit('需要 Pillow：用 DSH 自带 python 跑本脚本')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(ROOT, 'web', 'public', 'glyphs', 'photos')
EXTS = ('.jpg', '.jpeg', '.png', '.webp')


def encode(im, fmt, quality):
    buf = io.BytesIO()
    if fmt == 'PNG':
        im.save(buf, 'PNG', optimize=True)
    elif fmt == 'WEBP':
        im.save(buf, 'WEBP', quality=quality, method=6)
    else:
        if im.mode not in ('RGB', 'L'):
            im = im.convert('RGB')
        im.save(buf, 'JPEG', quality=quality, optimize=True, progressive=True)
    return buf.getvalue()


def target_size(w, h, max_h, max_w):
    """等比缩到 max_h/max_w 之内，只缩不放。"""
    scale = min(1.0, max_h / float(h), max_w / float(w))
    if scale >= 1.0:
        return w, h
    return max(1, int(round(w * scale))), max(1, int(round(h * scale)))


def flatten(im):
    """P/LA 之类带透明的，转成可重采样且不丢透明的模式。"""
    if im.mode in ('RGBA', 'LA'):
        return im
    if im.mode == 'P':
        return im.convert('RGBA' if 'transparency' in im.info else 'RGB')
    if im.mode in ('1', 'I;16', 'I', 'F'):
        return im.convert('RGB')
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--max-h', type=int, default=440)
    ap.add_argument('--max-w', type=int, default=1600)
    ap.add_argument('--quality', type=int, default=85)
    ap.add_argument('--bloated', type=int, default=250 * 1024)
    ap.add_argument('--only', action='append', default=[], help='只处理这些字（目录名），可重复')
    ap.add_argument('--json')
    ap.add_argument('--limit', type=int, default=0, help='只处理前 N 张（调试）')
    args = ap.parse_args()

    only = set(args.only)
    rows = []
    for dirpath, _dirnames, filenames in os.walk(PHOTOS):
        ch = os.path.basename(dirpath)
        if only and ch not in only:
            continue
        for fn in sorted(filenames):
            if not fn.lower().endswith(EXTS):
                continue
            rows.append((ch, os.path.join(dirpath, fn)))
    if args.limit:
        rows = rows[:args.limit]

    stats = {'resize': 0, 'reencode': 0, 'skip': 0, 'fail': 0}
    before = after = 0
    changed = []
    for ch, path in rows:
        rel = os.path.relpath(path, PHOTOS).replace('\\', '/')
        try:
            size0 = os.path.getsize(path)
            before += size0
            with Image.open(path) as im:
                im.load()
                w, h = im.size
                fmt = im.format
                work = flatten(im)
                nw, nh = target_size(w, h, args.max_h, args.max_w)
                resized = (nw, nh) != (w, h)
                if not resized and size0 <= args.bloated:
                    stats['skip'] += 1
                    after += size0
                    continue
                if resized:
                    work = work.resize((nw, nh), Image.LANCZOS)
                data = encode(work, fmt, args.quality)
            if len(data) >= size0 and not resized:
                stats['skip'] += 1
                after += size0
                continue
            after += len(data)
            stats['resize' if resized else 'reencode'] += 1
            changed.append({'file': rel, 'from': [w, h], 'to': [nw, nh],
                            'bytes_from': size0, 'bytes_to': len(data)})
            if not args.dry_run:
                tmp = path + '.tmp'
                with open(tmp, 'wb') as f:
                    f.write(data)
                os.replace(tmp, path)
        except Exception as e:  # noqa: BLE001
            stats['fail'] += 1
            print('FAIL %s %s' % (rel, e))

    print('=== %s  max_h=%d max_w=%d q=%d bloated=%dKB' % (
        'DRY-RUN' if args.dry_run else 'APPLIED', args.max_h, args.max_w,
        args.quality, args.bloated // 1024))
    print('文件 %d：缩小 %d，瘦身 %d，不动 %d，失败 %d' % (
        len(rows), stats['resize'], stats['reencode'], stats['skip'], stats['fail']))
    print('字节 %.1f MB → %.1f MB（%.0f%%）' % (
        before / 1048576.0, after / 1048576.0, 100.0 * after / max(before, 1)))
    for r in sorted(changed, key=lambda r: -(r['bytes_from'] - r['bytes_to']))[:8]:
        print('  %-28s %5dx%-5d → %4dx%-4d  %6.0fKB → %5.0fKB' % (
            r['file'], r['from'][0], r['from'][1], r['to'][0], r['to'][1],
            r['bytes_from'] / 1024.0, r['bytes_to'] / 1024.0))
    if args.json:
        with io.open(args.json, 'w', encoding='utf-8', newline='\n') as f:
            json.dump({'tool': 'normalize-photos', 'version': 1, 'dry_run': args.dry_run,
                       'max_h': args.max_h, 'max_w': args.max_w, 'quality': args.quality,
                       'stats': stats, 'before': before, 'after': after,
                       'changed': changed}, f, ensure_ascii=False, indent=1)
            f.write('\n')
    return 0 if not stats['fail'] else 1


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.exit(main())

# -*- coding: utf-8 -*-
import sys, io, os, json, re, shutil
sys.stdout.reconfigure(encoding='utf-8')
from docx import Document
G, C = 'web/public/glyphs', 'web/public/cards'
D = Document('D:/字谱智能体/卷五十四  网.docx').paragraphs
NS = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'
IDX = json.load(io.open(G + '/index.json', encoding='utf-8'))
LAB = re.compile(r'^(本義|轉義|辯證|音源|字族衍義|聲母擬態|所属卷|釋義)[：:]')


def txt(i):
    t = D[i].text.strip()
    return LAB.sub('', t).strip()


def blobs(i):
    return [D[i].part.related_parts[b.get(RID)].blob for b in D[i]._p.findall('.//' + NS + 'blip')]


def glyphs(ch, items):
    d = G + '/' + ch
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        os.remove(os.path.join(d, f))
    out = []
    for k, (pi, bi) in enumerate(items, 1):
        b = blobs(pi)[bi]
        ext = 'png' if b[:4] == b'\x89PNG' else 'jpg'
        fn = '%02d.%s' % (k, ext)
        io.open(d + '/' + fn, 'wb').write(b)
        out.append(fn)
    if out:
        IDX['chars'][ch] = {'doc': '卷五十四  网', 'files': ['%s/%s' % (ch, f) for f in out]}
    return out


ROW = re.compile(r'^([\u3400-\U0002FFFF]+)(?:（([^）]*)）)?\s*([a-zA-Züǖǘǚǜāáǎàēéěèīíǐìōóǒòūúǔùńňǹ]+)?')


def rows(start, end, cls, bridge):
    out = []
    for i in range(start, end + 1):
        t = D[i].text.strip()
        if not t:
            continue
        m = ROW.match(t)
        if not m:
            continue
        ch, al, py = m.group(1), m.group(2) or '', m.group(3) or ''
        q = re.search(r'(《[^》]{1,10}》)?[：:]?“([^”]{2,40})', t)
        quote = (q.group(1) or '') + '「' + (q.group(2) if q else '') + '」' if q else '（原文無引文）'
        base = ch
        out.append([ch + ('（' + al + '）' if al else ''), py, cls.get(base, ''), quote + '——' + bridge.get(base, ''), ''])
    return out
print('lib ready')

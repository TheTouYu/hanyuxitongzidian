# -*- coding: utf-8 -*-
"""把 .docx 抽成纯文本：段落按 <w:p> 切，保留 w:t 文字，图片记 [图]。

用法：python tools\\docx2txt.py <输入.docx> <输出.txt>
（.doc / OLE2 用 tools\\doc2txt.py，不要混用）
"""
import re, sys, zipfile

def unescape(s):
    s = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)), s)
    s = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), s)
    return (s.replace('&lt;', '<').replace('&gt;', '>')
             .replace('&quot;', '"').replace('&apos;', "'").replace('&amp;', '&'))

TOK = re.compile(r'<w:t(?:\s[^>]*)?>([\s\S]*?)</w:t>|<(?:a:blip|v:imagedata)((?:\s[^>]*)?)\/?>')

def paragraphs(xml):
    out = []
    re_p = re.compile(r'<w:p\b[^>]*?(/?)>|</w:p>')
    depth = 0
    start = -1
    for m in re_p.finditer(xml):
        if m.group(0) == '</w:p>':
            depth -= 1
            if depth == 0 and start >= 0:
                out.append(xml[start:m.end()])
                start = -1
        elif m.group(1) == '/':
            if depth == 0:
                out.append(m.group(0))
        else:
            if depth == 0:
                start = m.start()
            depth += 1
    return out

path = sys.argv[1]
zp = zipfile.ZipFile(path)
xml = zp.read('word/document.xml').decode('utf-8')

lines = []
for p in paragraphs(xml):
    buf = []
    for m in TOK.finditer(p):
        if m.group(1) is not None:
            buf.append(unescape(m.group(1)))
        else:
            buf.append('[图]')
    text = ''.join(buf).strip()
    if text:
        lines.append(text)

out = sys.argv[2]
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('paragraphs with text:', len(lines))
print('chars:', sum(len(x) for x in lines))
print('images:', sum(x.count('[图]') for x in lines))

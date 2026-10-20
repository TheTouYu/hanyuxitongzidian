"""Build the 目录 intake draft (claims) from the extracted TOC text.
Outputs ASCII-safe report to intake\_tmp_mulu_report2.txt and the draft JSON.
"""
import json, re, io

SRC = r'intake\_tmp_mulu.txt'
DST = r'intake\20261020-目录-全书结构.json'

CN = '一二三四五六七八九十廿卅卌百'
def numerals():
    m = {}
    base = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十'}
    for i, ch in base.items():
        m[ch] = i
    for i in range(1, 10):
        m['十' + base[i]] = 10 + i
    m['二十'] = 20
    for i in range(1, 10):
        m['廿' + base[i]] = 20 + i
    m['三十'] = 30
    for i in range(1, 10):
        m['卅' + base[i]] = 30 + i
    m['四十'] = 40
    for i in range(1, 10):
        m['卌' + base[i]] = 40 + i
    for tens, word in ((5,'五十'),(6,'六十'),(7,'七十'),(8,'八十'),(9,'九十')):
        m[word] = tens * 10
        for i in range(1, 10):
            m[base[tens] + base[i]] = tens * 10 + i
    m['一百'] = 100
    return m
NUMS = numerals()

lines = io.open(SRC, encoding='utf-8').read().split('\n')
chapters, volumes, sections, unparsed = [], [], [], []
cur_ch = cur_vol = None
for idx, raw in enumerate(lines, 1):
    s = raw.strip()
    if not s or s == '目 錄':
        continue
    m = re.match(r'^第([一二三四五六七八九十]+)章\s*(\S+)$', s)
    if m:
        cur_ch = {'no': m.group(1), 'name': m.group(2), 'volumes': []}
        chapters.append(cur_ch); continue
    if s.startswith('卷'):
        body = s[1:]
        pm = re.search(r'(\d+)$', body)
        page = int(pm.group(1)) if pm else None
        head = body[:pm.start()].strip() if pm else body.strip()
        num = name = None
        for k in sorted(NUMS, key=len, reverse=True):
            if head.startswith(k):
                num = NUMS[k]; name = head[len(k):].strip(); break
        if num is not None:
            cur_vol = {'num': num, 'name': name, 'page': page, 'sections': []}
            volumes.append(cur_vol)
            if cur_ch is not None:
                cur_ch['volumes'].append(cur_vol)
            continue
    m = re.match(r'^(\d+)\.\s*(\S*?)\s*部\s*(\d+)$', s)
    if m:
        sec = {'num': int(m.group(1)), 'name': m.group(2), 'page': int(m.group(3))}
        sections.append(sec)
        if cur_vol is not None:
            cur_vol['sections'].append(sec)
        continue
    if s.startswith('附') or re.match(r'^(漢字基本筆劃|後記|《系統漢字舘》|文旅策劃書|疑難雜字筆劃檢字表|\d+|PAGE)', s):
        unparsed.append((idx, s)); continue
    unparsed.append((idx, s))

notes = []
# fix numbering
for i, sec in enumerate(sections):
    prev = sections[i-1]['num'] if i else 0
    if sec['num'] != prev + 1:
        if i and sec['num'] < prev and str(sec['num']).endswith(str(prev + 1)[-1]):
            notes.append('FIX num %d -> %d (line %d)' % (sec['num'], prev + 1, sec['num']))
            sec['num'] = prev + 1
        else:
            notes.append('GAP before %d (prev %d)' % (sec['num'], prev))
for sec in sections:
    if sec['name'] and '\ue000' <= sec['name'][0] <= '\uf8ff':
        notes.append('PUA name at %d' % sec['num'])
        sec['name'] = ''
        sec['pua'] = True
    if not sec['name']:
        sec['name'] = ''

vol_nums = [v['num'] for v in volumes]
if vol_nums != list(range(1, 101)):
    notes.append('VOL NUMBERS: %s' % vol_nums)

# chapter numbering
for i, ch in enumerate(chapters, 1):
    ch['num'] = i

def vol_label(v):
    return '卷%s %s' % (v['cn'] if 'cn' in v else '', v['name'])

# 卷号统一用汉语数字（二十一、三十四、四十六…），原书目录印「廿/卅/卌」
def cn_num(n):
    digits = '零一二三四五六七八九'
    if n == 100:
        return '一百'
    if n < 10:
        return digits[n]
    if n == 10:
        return '十'
    if n < 20:
        return '十' + digits[n - 10]
    tens, ones = divmod(n, 10)
    return digits[tens] + '十' + (digits[ones] if ones else '')

for v in volumes:
    v['cn'] = cn_num(v['num'])

SEC_TXT = lambda s: ('%d %s部（p%d）' % (s['num'], s['name'], s['page'])) if s['name'] else ('%d 部（p%d，部首字原文用符號字，未能轉錄）' % (s['num'], s['page']))

claims = []
def add(cid, title, statement, boundary=None):
    claims.append({
        'id': cid, 'node': 'hanzi-origin', 'topic_id': 'topic-mulu',
        'title': title, 'statement': statement,
        'boundary': boundary or '部號、頁碼、部名均依《系統漢語》目錄頁與該書字形，不作增補。',
        'permission': 'public', 'fact_classes': ['evidence_scope'],
        'duplicate_resolution': 'create_distinct_with_boundary',
    })

first = True
def add_first(**kw):
    global first
    add(**kw)
    if first:
        c = claims[-1]
        c['topic_path'] = 'knowledge/hanzi-origin/mulu.md'
        c['topic_title'] = '全书目录与结构'
        c['topic_summary'] = '《系统汉语》的全书目录：十二章（章音源字）、一百卷（卷音源字）、六百零九部的编号与页码，以及书末附录与目录校记，是后续各卷录入与部号引用的框架依据。'
        c['topic_keywords'] = ['目录', '结构', '十二章', '一百卷', '部号', '音源字']
        first = False

total_pages = 'p2–1752'
add_first(cid='jm-001',
    title='总览：《系统汉语》十二章、一百卷、六百零九部，正文 p2–1752',
    statement=('《系统汉语》全书分十二章、一百卷、六百零九部，正文自 p2 至 p1752。章以音源字命名（士、谷、冓、孕、屰、因、兒、子、大、卝、兄、老），'
               '每章辖若干卷，卷亦以音源字命名并辖若干部（部即以该部部首字立目）；每部之下再按声符、形符诸字分条训释。'
               '书末另有附录：漢字基本筆劃（p1755）、後記（p1757）、疑難雜字筆劃檢字表（p1765）。'),
    boundary='章数、卷数、部数与页码依《系统汉语》目录页；「每部之下再分条」据正文体例概括。')

add(cid='jm-002',
    title='部号：1–609 是全书统一的引用编号，可据部号与页码定位',
    statement=('《系统汉语》给每部一个全书统一的序号（1–609），正文与各卷注释常用「見 24《射部》」这类写法互指；'
               '每部另在目录中注明起始页码。因此「部号 + 部首字」是全书结构的最小定位单位，卷与章只是部的分级容器。'),
    boundary='属对全书编号体例的说明；引用写法见卷三正文实例。')

for ch in chapters:
    vols = ch['volumes']
    secs = [s for v in vols for s in v['sections']]
    lo, hi = secs[0]['num'], secs[-1]['num']
    p0 = vols[0]['page'] or secs[0]['page']
    add(cid='jm-%03d' % (3 + ch['num'] - 1),
        title='第%s章 %s：卷%s至卷%s，第%d–%d部（p%d 起）' % (ch['no'], ch['name'], vols[0]['cn'], vols[-1]['cn'], lo, hi, p0),
        statement='第%s章以「%s」为音源字，辖%s，共%d部（第%d–%d部），正文自 p%d 起：%s。' % (
            ch['no'], ch['name'],
            '、'.join('卷%s %s' % (v['cn'], v['name']) for v in vols),
            len(secs), lo, hi, p0,
            '、'.join('%s（%d部）' % (v['name'], len(v['sections'])) for v in vols)),
        boundary='章的音源字取章题；所辖卷、部数与页码依目录页。')

base = 15
for i, v in enumerate(volumes):
    secs = v['sections']
    lo, hi = secs[0]['num'], secs[-1]['num']
    add(cid='jm-%03d' % (base + i),
        title='卷%s %s：第%d–%d部（p%d–p%d）' % (v['cn'], v['name'], lo, hi, v['page'] or secs[0]['page'], secs[-1]['page']),
        statement='卷%s「%s」（第%d–%d部，p%d 起）：%s。' % (
            v['cn'], v['name'], lo, hi, v['page'] or secs[0]['page'],
            '、'.join(SEC_TXT(s) for s in secs)),
        boundary='部号、部首字、页码依目录页；本卷尚未录入正文。')

add(cid='jm-115',
    title='附录：漢字基本筆劃、後記、疑難雜字筆劃檢字表',
    statement=('《系统汉语》正文之后附：漢字基本筆劃（p1755，笔画名称与写法）、後記（p1757，著者自述）、'
               '疑難雜字筆劃檢字表（p1765，按笔画检索难字）。'
               '目录页另列《系統漢字舘》文旅策劃書（p1762），属宣传策划材料，不属本书知识结构，未收入。'),
    boundary='篇目与页码依目录页；各篇内容据篇题概括；策划书按主人意见排除。')

add(cid='jm-116',
    title='目录校记：第223部原缺、第353部目录误作「53」、第554部部首字为符号字、卷号转写',
    statement=('据《系统汉语》目录页校读：一、部号 222「兆部」之后直接是 224「午部」，第223部原缺（疑为排印脱漏，正文卷四十「午」前应有一部）；'
               '二、卷六一「犀」下「犀部」目录印作「53.犀部」，据前后序号当为第353部；'
               '三、第554部（p1594，卷九一「火」内）的部首字原书用符号字排印，本次转写未能辨认，暂缺其名；'
               '四、目录页卷号作「卷廿一」「卷卅四」「卷卌六」，本库统一写作「卷二十一」「卷三十四」「卷四十六」，字形不同而卷次相同。'),
    boundary='校记据目录页字面与序号连续性推得，原书未作说明；第223部与第554部之名待查正文；卷号仅改写法，不改卷次。')

add(cid='jm-117',
    title='已录入卷次对照：卷一至卷三已入库，其余卷待录',
    statement=('按本目录，已录入《系统汉语》卷一「雞」（第1–7部）、卷二「㠯」（第8–15部）、卷三「矢」（第16–25部）共 28 部；'
               '卷四「弋」（第26–33部）起至卷一百「壽」（第602–609部）尚未录入。各卷录入后，可按本目录的部号与页码接续。'),
    boundary='已录卷次以知识库现有 Claim 为准；部号范围依目录页。')

out = {'schema_version': 1,
       'intent': '新增：《系统汉语》全书目录与结构 %d 条（12 章、100 卷、609 部及附录；卷号统一汉语数字，附录排除文旅策劃書）' % len(claims),
       'risk': 'medium', 'claims': claims}
io.open(DST, 'w', encoding='utf-8').write(json.dumps(out, ensure_ascii=False, indent=2))

rep = ['chapters=%d volumes=%d sections=%d claims=%d unparsed=%d' % (len(chapters), len(volumes), len(sections), len(claims), len(unparsed))]
rep += notes
rep.append('unparsed: ' + ' | '.join('%d:%s' % (i, s) for i, s in unparsed))
rep.append('vol1: ' + json.dumps(volumes[0], ensure_ascii=False))
rep.append('vol100: ' + json.dumps(volumes[-1], ensure_ascii=False))
rep.append('ch12: ' + json.dumps(chapters[-1], ensure_ascii=False)[:400])
io.open(r'intake\_tmp_mulu_report2.txt', 'w', encoding='utf-8').write('\n'.join(rep))
print('ok claims=%d' % len(claims))

# -*- coding: utf-8 -*-
import json,io,os,html,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"web\public\cards"; OUT=os.path.join(C,"html"); CH=r"web\public\glyphs\chars"
def load(ch): return json.load(io.open(os.path.join(C,ch+".json"),encoding="utf-8"))
def save(d):
    json.dump(d,io.open(os.path.join(C,d["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
def ext(s):
    o=[]
    for c in str(s or ""):
        cp=ord(c); o.append('<img class="cim" src="/glyphs/chars/%x.png">'%cp if 0x20000<=cp<=0x2FFFF and os.path.exists(os.path.join(CH,"%x.png"%cp)) else html.escape(c))
    return "".join(o)
TOP=chr(60)+"!doctype html"+chr(62)
CSS=('body{font-family:"Microsoft YaHei",sans-serif;font-size:16px;line-height:1.85;max-width:1000px;margin:22px auto;padding:0 18px}'
 'h2{font-size:40px;margin:0 0 4px}h3{color:#a33;margin:24px 0 6px}small{font-size:16px;color:#666}'
 'table{border-collapse:collapse;width:100%}td,th{border:1px solid #dcdcdc;padding:7px 9px;vertical-align:top;font-size:15px}'
 'th{background:#f3ece0;text-align:left}td:first-child,th:first-child{white-space:nowrap;width:1%}'
 '.cim{height:1.12em;vertical-align:-.2em}a{color:#06c}.bx{background:#faf6ee;border-left:4px solid #c9a96a;padding:8px 12px;margin:8px 0}.cap{font-size:13px;color:#888}')
def render(d):
    ch=d["char"]; h=[TOP+'<meta charset="utf-8"><title>'+html.escape(ch)+'</title>','<style>'+CSS+'</style>','<a href="/test.html">'+chr(8592)+' 返回检索</a>',
       '<h2>'+ext(d.get("head") or ch)+' <small>'+(d.get("pinyin") or "")+'</small></h2>']
    gs=os.path.join(r"web\public\glyphs",ch)
    if os.path.isdir(gs):
        fs=sorted(os.listdir(gs))[:40]
        h.append('<h3>字形</h3><div style="display:flex;gap:6px;overflow-x:auto">'+''.join(f'<figure style="margin:0;text-align:center;font-size:12px;color:#888"><img src="/glyphs/{ch}/{f}" style="height:110px"><figcaption>{i+1:02d}</figcaption></figure>' for i,f in enumerate(fs))+'</div>')
    ph=json.load(io.open(r"web\public\glyphs\photos\index.json",encoding="utf-8")).get("photos") or {}
    if ph.get(ch):
        caps=(json.load(io.open(r"web\public\glyphs\photos\captions.json",encoding="utf-8")).get("captions") or {}).get(ch) or []
        h.append('<h3>插图</h3><div style="display:flex;gap:8px;overflow-x:auto">'+''.join(
          f'<figure style="margin:0;text-align:center"><img src="/glyphs/photos/{ch}/{f}" style="height:150px"><figcaption class="cap">{ext(caps[i]) if i<len(caps) else ""}</figcaption></figure>' for i,f in enumerate(ph[ch]))+'</div>')
    for s in d["sections"]:
        if s.get("key")=="zigen": continue
        h.append('<h3>'+html.escape(s["label"])+'</h3>')
        if s.get("groups"):
            for g in s["groups"]:
                h.append('<p><b>'+ext(g.get("title",""))+'</b></p>')
                if g.get("rows"):
                    h.append('<table><tr><th>字</th><th>读音</th><th>类属</th><th>取义落点</th></tr>')
                    for r in g["rows"]: h.append('<tr>'+''.join('<td>'+ext(x)+'</td>' for x in r)+'</tr>')
                    h.append('</table>')
        elif s.get("text"): h.append('<div class="bx">'+ext(s["text"])+'</div>')
    io.open(os.path.join(OUT,ch+".html"),"w",encoding="utf-8").write("\n".join(h))
# 1) 市 补所属卷
d=load("市")
if not any(s.get("key")=="suoshujuan" for s in d["sections"]):
    d["sections"].append({"key":"suoshujuan","label":"所属卷","text":"卷十「㠯」（部 10 示）","cites":[],"links":[{"ch":"卷十㠯","label":"卷十㠯"}]})
    save(d)
# 2) 柰 补转义（p454 原文）
d=load("柰")
if not any(s.get("key")=="zhuanyi" for s in d["sections"]):
    idx=[i for i,s in enumerate(d["sections"]) if s.get("key")=="benyi"][0]
    d["sections"].insert(idx+1,{"key":"zhuanyi","label":"转义","text":"轉義：柰果香氣濃郁、味道甘酸。《洛陽伽藍記·報德寺》：“奈（柰）味甚美，冠于京師。”說明其味雖酸澀而能經受，故引申指忍得住、受得了、經得起。nài，《玉篇》：“柰何也……”","cites":[]})
    save(d)
for ch in ("示","柰","祟","款","祡","市"):
    render(load(ch))
print("rendered 6")
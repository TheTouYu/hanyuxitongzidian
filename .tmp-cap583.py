# -*- coding: utf-8 -*-
import json,io,os,sys,glob,html,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
SRC=r"web\public\cards"; OUT=os.path.join(SRC,"html"); CH=r"web\public\glyphs\chars"
CSS='body{font-family:"Microsoft YaHei",sans-serif;font-size:16px;line-height:1.85;max-width:1000px;margin:22px auto;padding:0 18px}h2{font-size:40px;margin:0 0 4px}h3{color:#a33;margin:24px 0 6px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #dcdcdc;padding:7px 9px;vertical-align:top;font-size:15px}th{background:#f3ece0;text-align:left}.cim{height:1.12em;vertical-align:-.2em}a{color:#06c}'
def ext(s):
    o=[]
    for c in str(s or ""):
        cp=ord(c)
        o.append('<img class="cim" src="/glyphs/chars/%x.png">'%cp if 0x20000<=cp<=0x2FFFF and os.path.exists(os.path.join(CH,"%x.png"%cp)) else html.escape(c))
    return "".join(o)
TOP=chr(60)+"!doctype html"+chr(62)
n=0
for fp in glob.glob(os.path.join(SRC,"*.json")):
    b=os.path.basename(fp)
    if b in ("index.json","variants.json","captions.json"): continue
    try: d=json.load(io.open(fp,encoding="utf-8"))
    except Exception: continue
    ch=d.get("char") or b[:-5]
    p=[TOP+'<meta charset="utf-8"><title>'+html.escape(str(d.get("head") or ch))+'</title>','<style>'+CSS+'</style>',
       '<a href="/test.html">'+chr(8592)+' 返回检索</a>','<h2>'+ext(d.get("head") or ch)+' <small>'+html.escape(str(d.get("pinyin") or ""))+'</small></h2>']
    for s in d.get("sections",[]):
        if s.get("label")=="所属卷": continue
        p.append('<h3>'+html.escape(str(s.get("label") or s.get("key") or ""))+'</h3>')
        if s.get("groups"):
            for g in s["groups"]:
                if g.get("title"): p.append('<p><b>'+ext(g["title"])+'</b></p>')
                hd=g.get("header") or ['字','读音','类属','取义落点']
                p.append('<table><tr>'+''.join('<th>'+html.escape(str(t))+'</th>' for t in hd)+'</tr>')
                for r in g.get("rows",[]): p.append('<tr>'+''.join('<td>'+ext(x)+'</td>' for x in r)+'</tr>')
                p.append('</table>')
        elif s.get("text"): p.append('<p>'+ext(s["text"])+'</p>')
    io.open(os.path.join(OUT,ch+".html"),"w",encoding="utf-8").write("\n".join(p)); n+=1
print("pages",n)
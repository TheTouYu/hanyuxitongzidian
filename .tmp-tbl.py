import sys,glob,json,re,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
pat=re.compile(r"([\u3400-\u9fff\U00020000-\U0002ffff]{1,3})（([^）]{1,14})）([^；。\n]{1,46})")
n=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    if os.path.basename(fp)=="index.json": continue
    try: d=json.load(open(fp,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    ch=False
    for s in d.get("sections",[]):
        if s.get("key")!="hengxiang": continue
        rows=[[m.group(1),m.group(2),m.group(3).strip()] for m in pat.finditer(s.get("text",""))]
        if len(rows)>=3:
            s["rows"]=rows; ch=True; n+=1
    if ch: json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("贴表格 rows 的卡",n)
h=open(ROOT+r"\web\public\test.html",encoding="utf-8").read()
old="const secs=(d.sections||[]).map(s=>`<div class=\"sec\"><h3>${esc(s.label||s.key)}</h3><p>${esc(s.text)}</p>"
new='''const tbl=s=>{ if(!s.rows||s.rows.length<3) return '';
  const head='<tr><th>字</th><th>形旁</th><th>取义落点</th></tr>';
  return `<table class="ct"><thead>${head}</thead><tbody>${s.rows.map(r=>`<tr><td class="zc">${esc(r[0])}</td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}</tbody></table>`;
};
const secs=(d.sections||[]).map(s=>`<div class="sec"><h3>${esc(s.label||s.key)}</h3>${tbl(s)}<p>${esc(s.text)}</p>'''
if "class=\"ct\"" not in h:
    h=h.replace("""const secs=(d.sections||[]).map(s=>`<div class="sec"><h3>${esc(s.label||s.key)}</h3><p>${esc(s.text)}</p>""",new)
    h=h.replace("</style>",""".ct{width:100%;border-collapse:collapse;margin:4px 0 10px;font-size:14.5px}
.ct th,.ct td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
.ct th{background:#f4ecdf;font-weight:600;color:#5c4a37;font-size:13px}
.ct td.zc{font-size:20px;width:56px;text-align:center}
</style>""")
    open(ROOT+r"\web\public\test.html","w",encoding="utf-8").write(h)
    print("patched html")
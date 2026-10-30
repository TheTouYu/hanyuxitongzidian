import sys,glob,os,json,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
h=open(ROOT+r"\web\public\test.html",encoding="utf-8").read()
if "parentBlock" not in h:
    ins='''
  const parentBlock = (d.level===3 && d.parent) ? await (async()=>{ try{
      const pr=await fetch('cards/'+encodeURIComponent(d.parent)+'.json'); if(!pr.ok) return '';
      const p=await pr.json();
      const inner=(p.sections||[]).map(s=>`<div class="sec"><h3>${esc(s.label||s.key)}</h3><p>${esc(s.text)}</p></div>`).join('');
      return `<div class="sec rootbox"><h3>字理分析·字根「${esc(d.parent)}」</h3>${inner}</div>`;
    }catch(e){ return ''; } })() : '';
  const lvlTag = d.level?`<span class="tag">${d.level===1?'一級字根':d.level===2?'二級字根':'字根衍生字'}</span>`:'';
'''
    h=h.replace("  const b=(d.bus||[])[0]||{};", ins+"  const b=(d.bus||[])[0]||{};")
    h=h.replace('<div class="bu">第${esc(String(b.num||\'?\'))}部 ${esc(b.name||\'\')}</div></div>','<div class="bu">${lvlTag}第${esc(String(b.num||\'?\'))}部 ${esc(b.name||\'\')}</div></div>')
    h=h.replace('${secs}<div class="sec"><h3>古文字字形</h3>${glyph}</div></div>`;','${secs}${parentBlock}<div class="sec"><h3>古文字字形</h3>${glyph}</div></div>`;')
    h=h.replace("</style>",".rootbox{background:#f7f1e6;border:1px dashed #d9c9b2;border-radius:10px;padding:10px 14px}\n</style>")
    open(ROOT+r"\web\public\test.html","w",encoding="utf-8").write(h)
    print("patched")
out=[]
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    if os.path.basename(fp)=="index.json": continue
    try: d=json.load(open(fp,encoding="utf-8"))
    except: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or os.path.basename(fp)[:-5]; b=d.get("bus") or []; b0=b[0] if b and isinstance(b[0],dict) else {}
    out.append({"c":ch,"p":d.get("pinyin",""),"b":b0.get("num",""),"n":b0.get("name",""),"lv":d.get("level",0),
                "t":[s.get("text","")[:30] for s in d.get("sections",[]) if isinstance(s,dict)]})
out.sort(key=lambda x:(x["b"] if isinstance(x["b"],int) else 999, x["c"]))
json.dump(out,open(ROOT+r"\web\public\cards\index.json","w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("index",len(out))
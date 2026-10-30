import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
helper=("const secHTML=(s,ch2)=>{const g2=(GLYPH[ch2]&&(GLYPH[ch2].files||[]))||[];"
 "const st=g2.length?`<div class=\"gscroll\">${g2.map((f,i)=>`<figure><img loading=\"lazy\" src=\"${encodeURI('glyphs/'+ch2+'/'+(String(f).startsWith(ch2+'/')?String(f).slice(ch2.length+1):f))}\"><figcaption>${String(i+1).padStart(2,'0')}</figcaption></figure>`).join('')}</div>`:'';"
 "const zx=(s.key==='zixing'||/字形|古文字/.test(s.label||''))?st:'';"
 "return `<div class=\"sec\"><h3>${esc(s.label||s.key)}</h3>${grp(s)}${tbl(s)}<p>${esc(s.text)}</p>${zx}</div>`;};\n")
if "const secHTML=" not in t:
    t=t.replace("async function open(ch){",helper+"async function open(ch){",1)
old="const inner=(p.sections||[]).map(s=>`<div class=\"sec\"><h3>${esc(s.label||s.key)}</h3><p>${esc(s.text)}</p></div>`).join('');"
if old in t:
    t=t.replace(old,"const inner=(p.sections||[]).map(s=>secHTML(s,d.parent)).join('');",1)
else:
    t=re.sub(r"const inner=\(p\.sections\|\|\[\]\)\.map\([^\n]*\n", "const inner=(p.sections||[]).map(s=>secHTML(s,d.parent)).join('');\n", t, count=1)
io.open(p,"w",encoding="utf-8").write(t)
print("helper",t.count("const secHTML="),"inner",t.count("secHTML(s,d.parent)"))
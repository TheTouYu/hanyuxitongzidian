import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
# ensure helper
if "const gsrc=" not in t:
    t=t.replace("const strip=","const gsrc=f=>encodeURI('glyphs/'+ch+'/'+(String(f).startsWith(ch+'/')?String(f).slice(ch.length+1):f));\nconst strip=",1)
# replace src expression
t=re.sub(r'src="glyphs/\$\{[^}]*startsWith\(ch[^"]*"', 'src="${gsrc(f)}"', t, count=1)
io.open(p,"w",encoding="utf-8").write(t)
print("gsrc" in t, t.count('src="${gsrc(f)}"'))
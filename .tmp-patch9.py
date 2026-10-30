import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-chjuan.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace('''        rows.append([x["name"]+"部","第%d部"%x["no"],"p%d"%x["p"]]); links.append(x["name"])''',
'''        n=x["name"] or ""
        rows.append([(n+"部") if n else "（部首未转录）","第%d部"%x["no"],"p%d"%x["p"]]); links.append(n)''')
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched")
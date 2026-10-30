import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"; t=io.open(p,encoding="utf-8").read()
ls=t.split("\n")
si=[i for i,l in enumerate(ls) if l.strip().startswith("const strip=")]
gi=[i for i,l in enumerate(ls) if l.strip().startswith("const g=(GLYPH[ch]")]
print("strip line",si,"g line",gi)
if si and gi:
    s=ls.pop(si[0])
    gi=[i for i,l in enumerate(ls) if l.strip().startswith("const g=(GLYPH[ch]")][0]
    ls.insert(gi+1,s)
io.open(p,"w",encoding="utf-8").write("\n".join(ls))
print("moved")
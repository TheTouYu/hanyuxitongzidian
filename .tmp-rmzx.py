import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
t=io.open(h,encoding="utf-8").read()
bad="""${hasZX?'':'<div class="sec"><h3>古文字字形</h3>'+strip+'</div>'}"""
n=t.count(bad)
t=t.replace(bad,"")
io.open(h,"w",encoding="utf-8",newline="\n").write(t)
print("removed",n,"| 古文字字形 remain:", t.count("古文字字形"))
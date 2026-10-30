import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"
s=io.open(h,encoding="utf-8").read()
i=s.index("  const vhtml=await variantsFor(ch);")
j=s.index("main.innerHTML=`",i)
k=s.index("`;",j)+2
pre=s[i:j]; tpl=s[j+2:k-1]   # tpl 含 ...` 内容
assert tpl.rstrip().endswith("`;") or True
# open() 剩余尾部（从 main.innerHTML 赋值后到 open 的结束）
rest=s[k:]
# 新结构
body_fn="async function cardBody(ch,d){\n"+pre+"\n  return "+tpl+";\n}\n"
s=s[:i]+"main.innerHTML = await cardBody(ch,d);"+rest
# 在 open 前插入 cardBody 定义
anchor="async function open(ch){"
s=s.replace(anchor, body_fn+anchor,1)
# parentBlock 改为直接调用 cardBody
old=re.search(r"const inner=`<div class=\"ph\">.*?\.join\(''\);", s, re.S)
assert old, "parentBlock block not found"
s=s[:old.start()]+"const inner=await cardBody(d.parent,p);"+s[old.end():]
s=s.replace("字根「${esc(d.parent)}」","字根「${esc(d.parent)}」",1)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("rewritten; cardBody count:",s.count("async function cardBody"),"| inner:",s.count("const inner=await cardBody"))
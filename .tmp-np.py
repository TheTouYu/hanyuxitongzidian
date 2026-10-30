import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for h in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    s=io.open(h,encoding="utf-8").read()
    if "async function cardBody(ch,d,opt)" not in s:
        s=s.replace("async function cardBody(ch,d){","async function cardBody(ch,d,opt){",1)
    s=s.replace("${photoBlock}${parentBlock}</div>`;","${(opt&&opt.noPhoto)?'':photoBlock}${parentBlock}</div>`;",1)
    s=s.replace("const inner=await cardBody(d.parent,p);","const inner=await cardBody(d.parent,p,{noPhoto:true});",1)
    io.open(h,"w",encoding="utf-8",newline="\n").write(s)
    print("patched",h, "noPhoto" in s, "cardBody(ch,d,opt)" in s)
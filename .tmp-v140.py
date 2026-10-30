import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=0
    anchor="const parentBlock = (d.level>1 && d.parent)"
    if anchor in h:
        h=h.replace(anchor,"const rootLink = (d.level===2 && d.parent) ? `<div class=\"sec\"><h3>所属字根</h3><p class=\"lks\"><a href=\"javascript:void(0)\" onclick=\"goCard('${d.parent}')\">${esc(d.parent)}</a></p></div>` : ''; const parentBlock = (d.level>2 && d.parent)",1); n+=1
    if "${parentBlock}" in h:
        h=h.replace("${parentBlock}","${rootLink}${parentBlock}"); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)
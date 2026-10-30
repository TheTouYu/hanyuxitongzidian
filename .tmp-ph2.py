import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const photoBlock=(()=>{const P=(window.PHOTO||{})[ch]||[];if(!P.length)return '';"
new="const photoBlock=(()=>{let P=(window.PHOTO||{})[ch]||[];let own=true;if(!P.length&&d.level===3&&d.parent){P=(window.PHOTO||{})[d.parent]||[];own=false;}if(!P.length)return '';"
for h in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    s=io.open(h,encoding="utf-8").read()
    assert old in s, h
    s=s.replace(old,new,1)
    s=s.replace("'<div class=\"sec\"><h3>插图</h3>","'<div class=\"sec\"><h3>插图'+(own?'':'（字根）')+'</h3>",1)
    io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("photo fallback added")
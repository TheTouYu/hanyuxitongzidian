# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
old="""return '<figure><img src="/glyphs/photos/'+encodeURIComponent(d.char)+'/'+encodeURIComponent(f)+'" alt="'+escH(cap||'插图')+'" style="height:170px"><figcaption>'+escH(cap||'')+'</figcaption></figure>';"""
new="""return '<figure><img src="'+escH(String(f).startsWith('/')?f:('/glyphs/photos/'+encodeURIComponent(d.char)+'/'+encodeURIComponent(f)))+'" alt="'+escH(cap||'插图')+'" style="height:170px"><figcaption>'+escH(cap||'')+'</figcaption></figure>';"""
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched2")
# -*- coding: utf-8 -*-
import json,io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
# 1) 把插图内联进卡
p=r"D:\系统汉字\web\public\cards\尸.json"; d=json.load(io.open(p,encoding="utf-8"))
d["photos"]=["01.jpg"]; d["captions"]=["廣西全州遺存的戴面具“尸祭”祖宗儀式"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 2) 渲染优先用卡内 photos/captions；所属卷无 links 时显示 text
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); o=h
    h=h.replace("const own=window.PHOTO[d.char]||[]","const own=d.photos||(window.PHOTO&&window.PHOTO[d.char])||[]")
    h=h.replace("const cap=(window.CAPS&&window.CAPS[d.char])||[]","const cap=d.captions||(window.CAPS&&window.CAPS[d.char])||[]")
    h=h.replace("""${ss?'<div class="sec"><h3>所属卷</h3>'+LKR(ss)+'</div>':''}""",
                """${ss?'<div class="sec"><h3>所属卷</h3>'+(LKR(ss)||(ss.text?'<p>'+esc(ss.text)+'</p>':''))+'</div>':''}""")
    if h!=o: io.open(f,"w",encoding="utf-8",newline="\n").write(h); print("patched",f.split(chr(92))[-1])
# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def add(ch,al):
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    cur=set(d.get("aliases") or []); cur.update(al); cur.discard(ch)
    d["aliases"]=sorted(cur); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(ch,d["aliases"])
add("𩦽",["駘","骀"]); add("駘",["𩦽","骀"]); add("𤐽",["炱"]); add("炱",["𤐽"])
# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-rel2.py"
t=io.open(p,encoding="utf-8").read()
if "seen_c" not in t:
    anchor='items=[x for x in items if x["c"]]'
    add=anchor+'\nseen_c=set(); _out=[]\nfor x in sorted(items,key=lambda y:(os.path.basename(""),)):\n    pass\n'
    # 简单去重：优先保留文件名==c 的条目
    dedup='''items=[x for x in items if x["c"]]
import os as _os, glob as _glob
_by={}
for _f in _glob.glob(C+r"\\\\*.json"):
    _b=_os.path.basename(_f)[:-5]
    _by[_b]=_f
_seen={}
for x in items:
    k=x["c"]
    cur=_seen.get(k)
    if cur is None: _seen[k]=x; continue
    # 相同 c：优先保留 c 自身为文件名的条目
    if k in _by:
        _seen[k]=x if _os.path.basename(_by[k])[:-5]==k else cur
items=list(_seen.values())'''
    t=t.replace(anchor,dedup,1)
    t=t.replace('print("index",len(items),"with parent",sum(1 for x in items if x["pr"]))','items.sort(key=lambda x:x["c"]); json.dump(items,open(C+r"\\index.json","w",encoding="utf-8"),ensure_ascii=False)\nprint("index",len(items),"with parent",sum(1 for x in items if x["pr"]))')
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
    print("builder patched")
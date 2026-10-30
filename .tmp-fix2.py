# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-huo.py"
t=io.open(p,encoding="utf-8").read()
old_sm = t[t.find("def sm(py_):"):t.find("head={")]
new_sm = '''def sm(py_,ch,grp):
    x=re.sub(r'[^a-z]','',py_.lower())
    key=None
    for k in ("zh","ch","sh"):
        if x.startswith(k): key=k
    if key is None: key=x[:1]
    if key not in MB: return 'y「零聲母」不系：零聲母，緒論七組未列（照實）。'
    g,f=MB[key]
    return '%s「%s」取「%s」：%s從%s一面取「%s」之義（推）。'%(key,g,f,ch,grp,f)

'''
t=t.replace(old_sm,new_sm)
t=t.replace('"text":sm(p)','"text":sm(p,c,grp_title)')
# 传入组名
t=t.replace('for c,ann,p,g in members:','for c,ann,p,g,grp_title in members:')
t=t.replace('members.append((c,ann,p,g))','members.append((c,ann,p,g,title))')
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched")
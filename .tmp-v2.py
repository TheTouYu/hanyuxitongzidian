# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-rel2.py"
t=io.open(p,encoding="utf-8").read()
if "_simp" in t:
    print("already patched"); raise SystemExit
ins = '''_simp={}
try:
    _vj=json.load(open(r"D:\\系统汉字\\web\\public\\variants.json",encoding="utf-8"))
    _vj=_vj.get("variants",_vj) if isinstance(_vj,dict) else {}
    for _s,_ts in _vj.items():
        for _t in (_ts if isinstance(_ts,list) else [_ts]):
            _simp.setdefault(_t,[]).append(_s)
except Exception:
    pass
'''
assert "items=[]" in t
t=t.replace("items=[]", ins+"items=[]",1)
old='"rc2":d.get("rootChain2",[]),'
new='"rc2":d.get("rootChain2",[]),"v":_simp.get(d.get("trad") or d.get("char",""),[]),'
assert old in t
t=t.replace(old,new,1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("patched rel2")
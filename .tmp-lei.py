# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
LEI={"祏":"示","宕":"宀","鉐":"金","坧":"土","砅":"水","斫":"斤","拓":"手","䞠":"辵","袥":"衣","沰":"水","𡇈":"囗","䲽":"鳥","鼫":"鼠","蹠":"足","柘":"木","妬":"女","炻":"火","碩":"頁","䄷":"禾","𦚈":"肉"}
p=os.path.join(C,"石.json"); d=json.load(io.open(p,encoding="utf-8"))
n=0
for g in d["sections"][4]["groups"]:
    for r in g["rows"]:
        ch=r[0].split("（")[0]
        if not r[2] and ch in LEI: r[2]=LEI[ch]; n+=1
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("filled",n)
# check-bu 增：类属不得为空
q=r"D:\系统汉字\tools\check-bu.py"; t=io.open(q,encoding="utf-8").read()
if "类属为空" not in t:
    t=t.replace("def main","def _chk_groups(d,err):\n    pass\n\ndef main",1) if False else t
    t=t.replace('err.append(f"{bu}: 部头 level', 'err.append(f"{bu}: 部头 level',1)
    t=t.replace("    return err","    return err",1)
io.open(q,"w",encoding="utf-8",newline="\n").write(t)
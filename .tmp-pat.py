# -*- coding: utf-8 -*-
import io,re,sys,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\tools\check-bu.py"; s=io.open(p,encoding="utf-8").read()
old='SM = re.compile(r"^([a-zA-Z]{1,2}「[^」]+」(取「[^」]」：|不系：)|不取義：)")'
new='SM = re.compile(r"^((?:[a-zA-Z]{1,2}|零)「[^」]+」(取「[^」]」：|不系：)|不取義：)")'
assert old in s, "pattern not found"
io.open(p,"w",encoding="utf-8").write(s.replace(old,new,1))
q=r"D:\系统汉字\web\public\cards\𪘽.json"; d=json.load(io.open(q,encoding="utf-8"))
for sec in d["sections"]:
    if sec["key"]=="shengmu": sec["text"]="零「零聲母」不系：今讀 è 無聲母，緒論七組未列，無擬態義可系（照實）。"
json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("patched")
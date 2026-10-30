# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\宅.json"
d=json.load(io.open(p,encoding="utf-8"))
alias={"挓":"挓（磔）","䯔":"䯔（𩨛）","𧧉":"𧧉（託）","䖳":"䖳（𩶱）","𨀟":"𨀟（踱）","𣳥":"𣳥（渡）","㤞":"㤞（𢖲𢜬）","𤵾":"𤵾（𤶮）","𥭌":"𥭌（𥯖）","𨀸":"𨀸（踱𨁕踧）"}
n=0
for g in d["sections"][4]["groups"]:
    for r in g["rows"]:
        if r[0] in alias: r[0]=alias[r[0]]; n+=1
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("updated",n)
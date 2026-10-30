import json
p=r"web\public\cards\慍.json"
c=json.load(open(p,encoding="utf-8"))
c["bus"]=[{"num":282,"name":"囗","sub":"𥁕（昷）"}]
for s in c["sections"]:
    if s["key"]=="bengen":
        s["text"]="【第282部「囗部」之𥁕（昷）支·二級字根】𥁕（昷）＝从囚从皿，象嬰兒在澡盆中、水溫，為「溫」之初文；慍从心𥁕聲，怒而含於心（《說文》「怒也。从心𥁕聲」）。非心部。"
    if s["key"]=="hengxiang":
        s["text"]="𥁕支諸字：溫（水暖）、蕰（草積）、縕（亂麻）、醞（釀酒）、慍（怒含），皆取「溫積於內」一面；故聲符給義、形符定落點。"
json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("card fixed")
import json
p=r"web\public\cards\慍.json"
c=json.load(open(p,encoding="utf-8"))
for s in c["sections"]:
    if s["key"]=="bengen":
        s["text"]="【第282部「囗部」之𥁕（昷）支·二級字根】𥁕（昷）與「囚」同源：从人在囗中，象人在封閉之處（避寒保暖）；小篆疊加「皿」為聲，取與器皿一樣密不透風，故有溫熱之意（《玉篇》「和也。或作溫」）。慍从心𥁕聲：怒含於心而不發（《說文》「怒也」）。"
    if s["key"]=="hengxiang":
        s["text"]="𥁕支諸字：溫（水暖）、蕰（草積）、縕（亂麻）、醞（釀酒）、慍（怒含），皆取「密閉積於內」一面；故聲符給義、形符定落點。"
json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
import json
p=r"web\public\cards\字.json"
c=json.load(open(p,encoding="utf-8"))
for s in c["sections"]:
    if s["key"]=="zigen":
        s["text"]="字形：古文字字形庫未收；原稿該條有「▲彩瓷繈褓俑（宋）」圖（photos/子/01.jpg），正見「象身子被包裹、雙手在外」之形，隨卡附出。"
        s["cites"]=[]
json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")
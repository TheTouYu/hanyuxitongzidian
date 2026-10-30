import json,os
p=r"web\public\cards\杞.json"
c=json.load(open(p,encoding="utf-8"))
for s in c["sections"]:
    if s["key"]=="zigen" and os.path.exists(r"web\public\glyphs\photos\杞\01.jpg"):
        s["text"]="字形：古文字字形庫未收；原稿該條有「▲杞柳」圖（photos/杞/01.jpg），枝條細長下垂，正見「可編箱筐」之形。"
json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("杞 photo:", os.path.exists(r"web\public\glyphs\photos\杞\01.jpg"))
print("cards:", len(os.listdir(r"web\public\cards")))
import json
upd={"鐖":"字形：古文字字形庫未收；原稿該條前有「▲鄭州大河村遺址出土的骨制魚鉤（6000年前）」圖（photos/鐖/01.jpg），隨卡附出。",
     "璣":"字形：古文字字形庫未收；原稿該條前有「▲渾天儀（東漢 張衡）」圖（photos/璣/01.jpg），隨卡附出。"}
for ch,t in upd.items():
    p=rf"web\public\cards\{ch}.json"
    c=json.load(open(p,encoding="utf-8"))
    for s in c["sections"]:
        if s["key"]=="zigen": s["text"]=t; s["cites"]=[]
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("updated",len(upd))
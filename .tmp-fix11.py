import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def card(ch,py_,bus,secs):
    d={"char":ch,"pinyin":py_,"level":0,"parent":"","bus":[{"num":bus[0],"name":bus[1]}],"sections":secs}
    json.dump(d,open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
card("松","sōng",(0,""),[
 {"key":"benyi","label":"本义","text":"松，sōng：从木公聲，松樹，取公之聲（原稿字卡條）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为松散、放松（后起义）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"s「失收」取「收」：松针聚而收（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"松与「鬆」为同音借用关系（今「松」兼作鬆之简化），非本字。","cites":[]}])
card("姜","jiāng",(523,"羊"),[
 {"key":"benyi","label":"本义","text":"姜（jiāng）从女羊聲：神農居姜水以為姓（《說文》），借為女子美稱（原稿字卡條）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"姓姜；又为女子美称。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：族聚而决（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"今「姜」又借作「薑」（生姜）之简化，属同音借用，非本字，须另立薑卡。","cites":[]}])
print("ok")
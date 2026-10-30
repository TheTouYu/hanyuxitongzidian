import json
B="源自《系統漢語》第383部「糸部」；字卡五步规程。"
K="topic-zika-shizi"
datas=[
("糸","糸 mì：部頭，从幺的兩頭出緒，象多股絲絞合之形，指拈出的紗線；五忽為絲，最細最末。"),
("縻","縻 mí：从糸麻聲（應从麻糸聲），牛韁繩，本指麻繩；《廣雅》系也、《小爾雅》縛也，取「線繩之用」一組。"),
("銯","銯 sī：从金糸聲，鋦子扒釘，即補綴陶瓷玻璃的細金屬絲，又紐帶；取「細而可繫」，以金為之。"),
("𢬡","𢬡 xì：从手系聲，杭越之間謂換曰㨙，《集韻》挾也扶也揭也；線繩之用移於手部。"),
("𦄐","𦄐 mí／kǔn：从糸，或作縻（分也）、或作稇（束也），一形兩用，一繩之解與扎兩面。"),
("𡱏","𡱏 mò：从糸戶聲，原稿謂戶為尸之訛表類別（與履屨屐同）、聲應為糸；青絲或麻製的鞋。"),
("細","細 xì：从糸囟聲（原稿疑从囟糸聲），《說文》微也，謂思考之具體入微，取絲細之狀。"),
("𦅔","𦅔 mò：从糸，《字彙補》命伏切音墨，絲也；與細、絲同取「絲之細」。"),
("紎","紎 zī：从糸，黑色繒也（《龍龕》側持切音緇）；原稿疑指長毛犬，《正字通》謂䊷字之譌。"),
("𧧈","𧧈 lěi：从言，誄之譌，銘也謚也，敘述死者生前事蹟以哀悼；形近耒之訛，記作訛變借形。"),
]
cl=[]
for i,(ch,st) in enumerate(datas,1):
    cl.append({"id":f"bm-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（第383部糸部）","statement":st,"boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡383糸部首10字2026-10-22","risk":"low","claims":cl},open(r"intake\20261022-字卡383糸部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("draft ok",len(cl))
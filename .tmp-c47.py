import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
ZH=("部頭折（歽㪿）：甲骨文从斤（斧）从木之斷處，象意砍斷樹木。與「析」相對——析依木紋豎砍（破），折攔腰橫砍（斷）。轉義：折扣損失夭折、斷而猶連（shé）、彎曲倒伏回轉屈從、安舒。辯證金文訛斷木為艸、小篆連寫成手。音源源自折斷聲。字族①折損②分明③彎曲。")
DUO=("部頭多：从夕的二疊——「夕」象殘月，二疊表示極致；月除月中兩三天外皆不圓，故《釋名》「月，缺也」，多象缺口極大，表示張開、廣大，可謂「哆」之初文。一月之中月缺時多、月中才滿，且月月重複，故又象意數量多（《說文》「重也，从重夕」）。另一源：古「夕、肉」形近，也可謂从「肉」二疊，象肉之肥美，為「䏧」之初文。轉義：重、大、勝出、剩餘；由張大引申歪斜不正（多讀為哆）。辯證古文與「邑」相混，「爹」之「父多」不合群婚制解释且字晚出。音源借音，義音同「也」。字族①月缺張大②肉之肥美。")
def card(ch,py,bu,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":[bu],"sources":["卷六十二  蛇.docx "+bu],
            "sections":[S("bengen","字根（"+bu+"）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("𧋍","dì","369.折部",ZH,"𧋍＝虫（形旁）＋折（聲旁）。《玉篇》同「螮」虹；xué《廣韻》「江𧋍，似蝤蛑，生海中」——似蟹的海蟲。","①折損：𧋍（虫）虹／海蟹｜虹（虫）虹｜蟹（虫）蟹。","端母d，「囤動」取「囤」。"),
("䏳","zhè","369.折部",ZH,"䏳（𦠟）＝肉（形旁）＋折（聲旁）。《廣韻》「脟皮也」；《博雅》「胓䏳，脂也」——牛羊脂。","①折損：䏳（肉）脂｜脂（肉）脂｜肪（肉）肪。","照母zh，「鑿總」取「鑿」。"),
("哳","zhā","369.折部",ZH,"哳＝口（形旁）＋折（聲旁）。《廣韻》「嘲哳，鳥鳴也」——鳥聲雜亂。","①折損：哳（口）鳥鳴｜嘲（口）嘲｜噪（口）噪。","照母zh，「鑿總」取「鑿」。"),
("䇽","zhì","369.折部",ZH,"䇽＝竹（形旁）＋折（聲旁）。《廣韻》「簟也」；《集韻》「竹席」。","①折損：䇽（竹）竹席｜簟（竹）簟｜席（巾）席。","照母zh，「鑿總」取「鑿」。"),
("㝂","zhì","369.折部",ZH,"㝂＝虫（形旁）＋折（聲旁）。《玉篇》「蝗也」——蝗蟲後腿折；zhè《集韻》「螟蟲子」。","①折損：㝂（虫）蝗子｜蝗（虫）蝗｜螟（虫）螟。","照母zh，「鑿總」取「鑿」。"),
("𧻸","shì","369.折部",ZH,"𧻸（跩跇𨒧）＝走（形旁）＋折（聲旁）。《玉篇》「踰也」跳躍——先曲腿才能跳起。","③彎曲：𧻸（走）跳躍（先曲）｜跇（足）跇｜超（走）超。","審母sh，「失收」取「失」。"),
("多","duō","370.多部",DUO,"多＝重夕（殘月二疊），象缺口極大、張開廣大，為「哆」之初文；又重夕象月缺時多、月月重複，故為數量多；或从二肉，象肉肥美。轉義重、大、勝、餘、歪斜。","①張大：多（夕夕）多｜哆（口）張口｜侈（人）奢侈。","端母d，「囤動」取「囤」。"),
("㝖","yí","370.多部",DUO,"㝖（宜冝）＝宀（形旁）＋多（組件），从二肉象肉之肥美，本為「䏧」之初文；「宜」假借為適宜。","②肥美：㝖（宀）宜／肥美｜宜（宀）宜｜䏧（肉）肥美。","疑母y，今零聲母不系。"),
("哆","duō","370.多部",DUO,"哆＝口（形旁）＋多（聲旁）。《說文》「張口也」——張口、唇下垂；《爾雅》「離也」離散。","①張大：哆（口）張口｜侈（人）奢侈｜㗬（多）厚唇。","端母d，「囤動」取「囤」。"),
("㗬","zhā","370.多部",DUO,"㗬＝多＋尚（形旁）。《說文》「厚唇皃」，徐鍇「多即厚也」。","①張大：㗬（多尚）厚唇｜哆（口）張口｜厚（厂）厚。","照母zh，「鑿總」取「鑿」。"),
("痑","duò","370.多部",DUO,"痑＝疒（形旁）＋多（聲旁）。《說文》「馬病也」——《詩》「痑痑駱馬」；《玉篇》「力極也」，即打哆嗦、發抖。","①張大：痑（疒）馬病／力極｜疲（疒）疲｜抖（手）抖。","端母d，「囤動」取「囤」。"),
("侈","chǐ","370.多部",DUO,"侈＝人（形旁）＋多（聲旁）。《說文》「掩脅也，一曰奢也」——自高自大、盛氣凌人；奢侈浪費；《廣韻》「泰也、大也」。","①張大：侈（人）奢侈｜奢（大）奢｜哆（口）張。","穿母ch，「刺持」取「刺」。"),
]
for ch,py,bu,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,bu,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{425+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,bu,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡折部收尾+多部首6条 2026-10-23","risk":"low","claims":[]}
for i,(cid,title,stmt) in enumerate(cl):
    bu=rows[i][2]
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":f"源自《系統漢語》卷六十二「蛇」部之「{bu.split('.')[1]}」；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十四批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h)
print("applied", '"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h))
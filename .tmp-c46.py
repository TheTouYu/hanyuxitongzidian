import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
ZH=("部頭折（歽㪿）：甲骨文从斤（斧）从木之斷處，象意砍斷樹木。與「析」相對——析依木紋豎砍（破），折攔腰橫砍（斷）。轉義：折扣損失夭折、斷而猶連（shé）、彎曲倒伏回轉屈從、安舒（tí）。辯證西周金文訛斷木為艸、小篆連寫成手。音源源自折斷聲，因斷而猶連義音同「世」。字族①折損②分明③彎曲。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["369.折部"],"sources":["卷六十二  蛇.docx 369.折部"],
            "sections":[S("bengen","字根（第369部：折部）",ZH),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("㿱","xué","㿱＝皮（形旁）＋折（聲旁）。《集韻》「枯也，一曰撮取皮也」；《字彙補》「亂也」。","①折損：㿱（皮）枯／撮皮｜枯（木）枯｜剝（刀）剝。","心母x，「失收」取「失」。"),
("狾","zhì","狾＝犬（形旁）＋折（聲旁）。《說文》「狂犬也」——瘋狗。《春秋傳》「狾犬入華臣氏之門」。","①折損：狾（犬）瘋狗｜狂（犬）狂｜猘（犬）猘。","照母zh，「鑿總」取「鑿」。"),
("逝","shì","逝＝辵（形旁）＋折（聲旁）。《說文》「往也」過往；《正韻》「亡也」——一去不返。","①折損：逝（辵）往｜往（彳）往｜徂（彳）徂。","審母sh，「失收」取「失」：一去不回。"),
("哲","zhé","哲（悊嚞埑）＝口（形旁）＋折（聲旁）。《說文》「知也」——能把难事解开，即智慧。","②分明：哲（口）智｜悊（心）敬｜晢（日）明。","照母zh，「鑿總」取「鑿」。"),
("晢","zhé","晢（晣）＝日（形旁）＋折（聲旁）。《說文》「昭晣，明也」；《廣韻》「星光也」。","②分明：晢（日）明｜昭（日）昭｜晰（日）晰。","照母zh，「鑿總」取「鑿」。"),
("䀸","zhì","䀸（䀿）＝目（形旁）＋折（聲旁）。《玉篇》「瞥也」；《廣韻》「目光也」；《類篇》「目美也」。","②分明：䀸（目）瞥／目明｜瞥（目）瞥｜睇（目）睇。","照母zh，「鑿總」取「鑿」。"),
("悊","zhé","悊＝心（形旁）＋折（聲旁）。《說文》「敬也」；《玉篇》「與哲同」。","②分明：悊（心）敬／智｜哲（口）哲｜敬（攴）敬。","照母zh，「鑿總」取「鑿」。"),
("誓","shì","誓＝言（形旁）＋折（聲旁）。《說文》「約束也」——斬草木為誓，相互約束。","③彎曲：誓（言）約束｜約（糸）約｜盟（皿）盟。","審母sh，「失收」取「收」：收束。"),
("娎","xiè","娎（𡝊）＝女（形旁）＋折（聲旁）。《說文》「娎㛍也，洋洋自得」；《玉篇》「喜也」。","③彎曲：娎（女）自得｜喜（口）喜｜嫻（女）嫻。","心母x，「失收」取「失」。"),
("䋢","biē","䋢＝糸（形旁）＋折（聲旁）。《說文》「扁緒也，一曰弩腰鉤帶」——編繩、弓弩腰帶；《集韻》「禦左回曰䋢」。","③彎曲：䋢（糸）編繩／鉤帶｜繩（糸）繩｜結（糸）結。","幫母b，「閉剝」取「閉」：束而閉。"),
("䩢","zhì","䩢＝革（形旁）＋折（聲旁）。《玉篇》「刀鞞」刀鞘；dá 通「靼」，柔軟皮革。","①折損：䩢（革）刀鞘／柔皮｜鞘（革）鞘｜韃（革）韃。","照母zh，「鑿總」取「鑿」。"),
("浙","zhè","浙＝水（形旁）＋折（聲旁）。《說文》「江，水東至會稽山陰為浙江」即錢塘江，潮湧如折；《廣韻》「浙米」淘米。","①折損：浙（水）江潮／淘米｜潮（水）潮｜折（斤木）折。","照母zh，「鑿總」取「鑿」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{411+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡折部12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":"源自《系統漢語》卷六十二「蛇」部之「折部」（第369部）；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十三批.json"
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
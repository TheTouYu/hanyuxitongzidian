import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
CE=("部頭徹（彻）：甲骨文从又从鬲，象意搬動食器鬲——吃完後收拾空的鬲（《六書故》「屏去釜鬲徹饌之義」）。轉義：撤走→拆除、毀壞、陳設；由空盡→通達、透明（《廣韻》「通也、明也」）。辯證戰國古文鬲演作育、又演作攴，另加彳表行走。音源借音，義音同也。字族①撤除②空盡。")
ZH=("部頭折（歽㪿）：甲骨文从斤（斧）从木之斷處，象意砍斷樹木。與「析」相對——析依木紋豎砍（破），折攔腰橫砍（斷）。轉義：折扣損失夭折（木斷則用少）、斷而仍連（shé）、彎曲倒伏回轉屈從、安舒。辯證西周金文訛斷木為艸，小篆連寫成手，故《說文》「从斤斷艸」不確。音源音源字，源自折斷聲，因斷而猶連義音同「世」。字族①折損②折而猶連③為刀所斫。")
def card(ch,py,bu,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":[bu],"sources":["卷六十二  蛇.docx "+bu],
            "sections":[S("bengen","字根（"+bu+"）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("𦔞","zhé","368.徹部",CE,"𦔞＝耒（形旁）＋徹聲。《字彙》「稅名」；《正字通》「俗徹字」。","①撤除：𦔞（耒）稅名｜徹（彳）通｜稅（禾）稅。","照母zh，「鑿總」取「鑿」。"),
("㯙","zhé","368.徹部",CE,"㯙＝木（形旁）＋徹聲。《集韻》「楊㯙，棗木名，通作徹」——棗熟任其在樹風乾、葉盡落而棗掛枝頭之狀。","②空盡：㯙（木）棗乾｜棗（木）棗｜徹（彳）通。","照母zh，「鑿總」取「鑿」。"),
("折","zhé","369.折部",ZH,"折＝从斤从木（斷處），象意攔腰橫砍斷木。轉義折扣、斷而猶連（shé）、彎曲倒伏屈從、安舒（tí）。","①折損：折（斤木）斷｜析（斤木）剖｜伐（人戈）伐。","照母zh，「鑿總」取「鑿」：斤劈木斷。"),
("硩","chè","369.折部",ZH,"硩（擿）＝石（形旁）＋折（聲旁）。《說文》「上摘岩空青、珊瑚墮之」——以石投擲毀巢，摘取巖上珍物。","①折損：硩（石）投擲摘取｜擲（手）擲｜墮（土）墮。","穿母ch，「刺持」取「刺」：石擊而斷。"),
("銴","shì","369.折部",ZH,"銴＝金（形旁）＋折（聲旁）。《說文》「車樘結也，一曰銅生五色」——車幔鬆緊樞紐；又銅鏽。","①折損：銴（金）車樞／銅鏽｜錮（金）錮｜結（糸）結。","審母sh，「失收」取「收」：收束鬆緊。"),
("蜇","zhē","369.折部",ZH,"蜇（蛆）＝虫（形旁）＋折（聲旁）。《玉篇》「蟲螫也」——毒蟲叮刺，其刺常斷在肉中；又海蜇。","①折損：蜇（虫）螫刺（刺斷）｜螫（虫）螫｜蛆（虫）蛆。","照母zh，「鑿總」取「鑿」。"),
("𧶇","zhá","369.折部",ZH,"𧶇＝貝（形旁）＋折（聲旁）。《廣韻》「貨也」——財貨。","①折損：𧶇（貝）貨｜貨（貝）貨｜貝（貝）貝。","照母zh，「鑿總」取「鑿」。"),
("𥍭","zhì","369.折部",ZH,"𥍭＝矛（形旁）＋折（聲旁）。《廣韻》「矛謂之𥍭」。","①折損：𥍭（矛）矛｜矛（矛）矛｜矟（矛）矟。","照母zh，「鑿總」取「鑿」。"),
("䭁","zhì","369.折部",ZH,"䭁＝食（形旁）＋折（聲旁）。《玉篇》「臭敗之味」——食物腐敗，亦折損。","①折損：䭁（食）食敗｜腐（肉）腐｜敗（攴）敗。","照母zh，「鑿總」取「鑿」。"),
("焎","xiè","369.折部",ZH,"焎（烲）＝火（形旁）＋折（聲旁）。《廣韻》「火氣也」；chè《集韻》「火然也」——火斷而復燃。","①折損：焎（火）火氣／火然｜然（火）燃｜燼（火）燼。","心母x，「失收」取「失」：火散而滅。"),
]
for ch,py,bu,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,bu,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{401+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,bu,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡徹尾折首10条入库 2026-10-23","risk":"low","claims":[]}
for i,(cid,title,stmt) in enumerate(cl):
    bu=rows[i][2]
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":f"源自《系統漢語》卷六十二「蛇」部之「{bu.split('.')[1]}」；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十二批.json"
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
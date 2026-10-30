import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
DUO=("部頭多：从夕的二疊——「夕」象殘月，二疊表示極致；月除月中兩三天外皆不圓，故《釋名》「月，缺也」，多象缺口極大，表示張開、廣大，可謂「哆」之初文。月缺時多、月月重複，故又象意數量多（《說文》「重也，从重夕」）。另源：古「夕、肉」形近，或从「肉」二疊，象肉肥美，為「䏧」之初文。轉義：重、大、勝出、剩餘；由張大引申歪斜不正。辯證古文與「邑」相混。音源借音，義音同「也」。字族①月缺張大②肉多肥大。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["370.多部"],"sources":["卷六十二  蛇.docx 370.多部"],
            "sections":[S("bengen","字根（第370部：多部）",DUO),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("茤","jì","茤（芰）＝艸（形旁）＋多（聲旁）。《說文》「芰，蔆也」，杜林說「芰从多」——菱角，狀如牛角。","①張大：茤（艸）菱角（角張）｜菱（艸）菱｜角（角）角。","見母j，「聚決」取「聚」。"),
("𧩫","zhā","𧩫（詫）＝言（形旁）＋奓聲。《集韻》「譇詉，羞窮」；chà「詫，誇也」——誇張，通「侘」。","①張大：𧩫（言）誇張／羞窮｜誇（言）誇｜詫（言）詫。","照母zh，「鑿總」取「鑿」。"),
("扅","yí","扅（𢨹）＝戶（形旁）＋多（聲旁）。《廣韻》「扊扅，戶扃也」——門閂；《集韻》「門闗謂之扊扅」。","①張大：扅（戶）門閂｜扊（戶）扊｜閂（門）閂。","疑母y，今零聲母不系。"),
("拸","yí","拸（搋柂）＝手（形旁）＋多（聲旁）。《玉篇》「加也」施加；chǐ「析也、折也」——《莊子》「介者拸畫」；又「哆，大皃」。","①張大：拸（手）施加／析／拍拽｜搋（手）搋｜扯（手）扯。","疑母y，今零聲母不系。"),
("䏧","nà","䏧＝肉（形旁）＋多（聲旁）。《玉篇》「肥皃」；《廣韻》「膩也」；chǐ《集韻》「肉物肥美也」——**多从二肉一源的核心字**。","②肥美：䏧（肉）肥／膩｜肥（肉）肥｜膩（肉）膩。","泥母n，「納弄」取「納」：油脂納聚。"),
("䬷","shě","䬷＝食（形旁）＋舍聲。《集韻》「䬼飫也，或从舍」；「饜也」——飽食。","②肥美：䬷（食）飽食｜飽（食）飽｜饜（食）饜。","審母sh，「失收」取「收」。"),
("垑","chǐ","垑＝土（形旁）＋多（聲旁）。《說文》「恃也」——依賴土地之多；《玉篇》「治土」。","②肥大：垑（土）地多／恃｜多（夕夕）多｜恃（心）恃。","穿母ch，「刺持」取「刺」。"),
("黟","yī","黟＝黑（形旁）＋多（聲旁）。《說文》「黑木也」——烏木（陰沉木），長年水浸碳化，黑而重；丹陽有黟縣。","②肥大：黟（黑）烏木／黑｜黑（黑）黑｜墨（土）墨。","影母y，今零聲母不系。"),
("𥿫","mí","𥿫（貤）＝糸（形旁）＋多（聲旁）。《說文》「縻，牛轡也，或从多」；yì「貤，重次第物也」——重複、次第。","②肥大：𥿫（糸）牛轡／重疊｜縻（糸）縻｜轡（絲）轡。","明母m，「蒙末」取「蒙」：蒙覆而牽。"),
("陊","duò","陊（阤陁）＝阜（形旁）＋多（聲旁）。《說文》「落也」墜落；《玉篇》「壞也、小崩也」；《廣韻》「下坂皃」——**大字張開則下墜**。","①張大：陊（阜）墜落｜墮（土）墮｜崩（山）崩。","端母d，「囤動」取「囤」。"),
("姼","chǐ","姼（𡚼媞）＝女（形旁）＋多（聲旁）。《說文》「美女也」；《方言》「南楚謂父考曰父姼，母妣曰母姼」。","①張大：姼（女）美／尊稱｜美（羊）美｜媞（女）安。","穿母ch，「刺持」取「刺」。"),
("移","yí","移＝禾（形旁）＋多（聲旁）。《說文》「禾相倚移也」；《六書故》「移秧也，凡種稻先苗之後移之」——禾苗倚斜而移栽。","①張大：移（禾）移秧／遷移｜迻（辵）迻｜徙（彳）徙。","疑母y，今零聲母不系。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{449+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡多部后12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":"源自《系統漢語》卷六十二「蛇」部之「多部」（第370部）；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十六批.json"
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
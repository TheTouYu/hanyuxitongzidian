import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
DUO=("部頭多：从夕的二疊——「夕」象殘月，二疊表示極致；月除月中兩三天外皆不圓，故《釋名》「月，缺也」，多象缺口極大，表示張開、廣大，可謂「哆」之初文。月缺時多、月月重複，故又象意數量多（《說文》「重也，从重夕」）。另源：古「夕、肉」形近，或从「肉」二疊，象肉肥美，為「䏧」之初文。轉義：重、大、勝出、剩餘；由張大引申歪斜不正。辯證古文與「邑」相混。音源借音，義音同「也」。字族①月缺張大②肉多肥大。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["370.多部"],"sources":["卷六十二  蛇.docx 370.多部"],
            "sections":[S("bengen","字根（第370部：多部）",DUO),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("㒅","qǐ","㒅＝人（形旁）＋多（聲旁）。《廣韻》「開衣領也」——敞開衣領；「行張足」——走路張開腳。","①張大：㒅（人）敞領／張足｜張（弓）張｜啟（攴）啟。","溪母q，「親缺」取「缺」：開而不合。"),
("䇋","hài","䇋＝立（形旁）＋多（聲旁）。《篇海》「音亥，神名」。","①張大：䇋（立）神名｜神（示）神｜立（立）立。","曉母h，「豁活」取「豁」。"),
("𣃽","nuǒ","𣃽（旎）＝方（形旁）＋多（聲旁）。《集韻》「㫊𣃽，旌旗皃，或作旎」——旗幟展開飄動。","①張大：𣃽（方）旌旗｜旎（方）旖旎｜旗（方）旗。","泥母n，「納弄」取「納」。"),
("𣆚","nuǒ","𣆚（侈）＝日（形旁）＋多（聲旁）。《玉篇》「宬也」藏書室；chǐ《正字通》「與侈同」。","②肥美：𣆚（日）藏室／奢侈｜宬（宀）宬｜藏（艸）藏。","泥母n，「納弄」取「納」。"),
("𢡏","nuǒ","𢡏＝心（形旁）＋多（聲旁）。《龍龕》「窚也」——容受。","②肥美：𢡏（心）容受｜容（宀）容｜受（又）受。","泥母n，「納弄」取「納」：納而容之。"),
("𥭋","jì","𥭋＝竹（形旁）＋多（聲旁）。《漢典》「網罟一類的捕魚器物」。","①張大：𥭋（竹）魚具（張口）｜罟（网）罟｜笱（竹）笱。","見母j，「聚決」取「聚」。"),
("𠞎","jiū","𠞎（𠛩）＝刀（形旁）＋多（聲旁）。《龍龕》「二正，出罪也」。","①張大：𠞎（刀）出罪｜刑（刀）刑｜罰（网）罰。","見母j，「聚決」取「決」。"),
("栘","yí","栘＝木（形旁）＋多（聲旁）。《說文》「棠棣也」即唐棣，春末開黃花極繁盛；《古今注》「圓葉弱蒂，微風大搖，一名高飛」。","①張大：栘（木）唐棣（花繁葉搖）｜棣（木）棣｜搖（手）搖。","疑母y，今零聲母不系。"),
("迻","yí","迻（拪扡移）＝辵（形旁）＋多（聲旁）。《說文》「遷徙也」——遷移；《集韻》「古作拪，通作移」。","①張大：迻（辵）遷徙｜移（禾）移｜徙（彳）徙。","疑母y，今零聲母不系。"),
("𪀓","yí","𪀓＝鳥（形旁）＋多（聲旁）。《玉篇》「鳥名」；《五音集韻》「眾鳥總名」。","②肥大：𪀓（鳥）鳥名｜鳥（鳥）鳥｜群（羊）群。","疑母y，今零聲母不系。"),
("𦴌","jùn","𦴌＝皮（形旁）＋多（聲旁）。《字彙補》「獦之皮袴也」——獵裝皮褲。","②肥美：𦴌（皮）皮褲｜袴（衣）袴｜皮（皮）皮。","見母j，「聚決」取「聚」。"),
("㝖","yí","㝖（宐宜）＝宀（形旁）＋多（組件），从二肉象肉之肥美，本為「䏧」之初文；《說文》「所安也」，後假借為適宜。","②肥美：㝖（宀）肥美／安宜｜宜（宀）宜｜䏧（肉）䏧。","疑母y，今零聲母不系。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{461+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡多部末12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":"源自《系統漢語》卷六十二「蛇」部之「多部」（第370部）；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十七批.json"
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
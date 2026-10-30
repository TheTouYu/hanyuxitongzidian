import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
DUO=("部頭多：从夕的二疊——「夕」象殘月，二疊表示極致；月除月中兩三天外皆不圓，故《釋名》「月，缺也」，多象缺口極大，表示張開、廣大，可謂「哆」之初文。月缺時多、月月重複，故又象意數量多（《說文》「重也，从重夕」）。另源：古「夕、肉」形近，或从「肉」二疊，象肉肥美，為「䏧」之初文。轉義：重、大、勝出、剩餘；由張大引申歪斜不正。辯證古文與「邑」相混。音源借音，義音同「也」。字族①月缺張大②肉之肥美。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["370.多部"],"sources":["卷六十二  蛇.docx 370.多部"],
            "sections":[S("bengen","字根（第370部：多部）",DUO),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("誃","chǐ","誃（卶詑訑謻）＝言（形旁）＋多（聲旁）。《說文》「離別也」；周景王作洛陽「誃台」——離開、別處之台。","①張大：誃（言）離別／別台｜別（刀）別｜移（禾）移。","穿母ch，「刺持」取「刺」。"),
("袳","chǐ","袳（袲）＝衣（形旁）＋多（聲旁）。《說文》「衣張也」——衣服張開；《玉篇》「長衣皃」。","①張大：袳（衣）衣張｜張（弓）張｜裾（衣）裾。","穿母ch，「刺持」取「刺」。"),
("卶","chǐ","卶＝卩（形旁）＋多（聲旁）。《說文》「有大度也」——寬大的度量；《集韻》「慶也」。","①張大：卶（卩）大度｜度（又）度｜寬（宀）寬。","穿母ch，「刺持」取「刺」。"),
("㢋","chǐ","㢋＝广（形旁）＋侈聲。《說文》「廣也」——《春秋國語》「俠溝而㢋我」；《廣雅》「大也」。","①張大：㢋（广）廣大｜廣（广）廣｜宏（宀）宏。","穿母ch，「刺持」取「刺」。"),
("㶴","chǐ","㶴（𤈕）＝火（形旁）＋多（聲旁）。《說文》「盛火也」——大火；《玉篇》「盛也」。","①張大：㶴（火）盛火｜盛（皿）盛｜炎（火）炎。","穿母ch，「刺持」取「刺」。"),
("奓","shē","奓（奢偧）＝大（形旁）＋者聲。《說文》「奢，張也」——奢侈、過分；《篇海》「亦奢也，泰也，大也」。","①張大：奓（大）奢侈／張大｜奢（大）奢｜侈（人）侈。","審母sh，「失收」取「收」。"),
("㡅","nuǒ","㡅（𢄴𠕝）＝巾（形旁）＋多（聲旁）。《集韻》引《博雅》「宬，㡅也」——收藏物品的房屋。","②肥美：㡅（巾）藏室｜宬（宀）宬｜藏（艸）藏。","泥母n，「納弄」取「納」。"),
("𤝻","yí","𤝻（𧳁）＝犬（形旁）＋多（聲旁）。《廣韻》「獸名，似犬，尾白，目喙赤，出則大兵」；《山海經》「見則邑有火」。","①張大：𤝻（犬）異獸｜狾（犬）瘋狗｜狡（犬）狡。","疑母y，今零聲母不系。"),
("蛥","shé","蛥＝虫（形旁）＋多（聲旁）。《玉篇》「蛥蚗」；《方言》「蟬名」——齊謂螇螰、楚謂蟪蛄、秦謂蛥蚗。","①張大：蛥（虫）蟬｜蟬（虫）蟬｜蚗（虫）蚗。","審母sh，「失收」取「收」。"),
("䮈","chí","䮈（馳）＝馬（形旁）＋多（聲旁）。《集韻》「馳，《說文》大驅也」——策馬疾馳。","①張大：䮈（馬）疾馳｜馳（馬）馳｜驅（馬）驅。","穿母ch，「刺持」取「刺」。"),
("翗","ké","翗＝羽（形旁）＋多（聲旁）。《玉篇》「飛皃」——羽翼張開飛翔。","①張大：翗（羽）飛｜飛（飛）飛｜翹（羽）翹。","溪母k，「口控」取「控」。"),
("𠛫","duǒ","𠛫＝刀（形旁）＋多（聲旁）。《篇海》「摑也」——打耳光；《字彙》「批打也」。","①張大：𠛫（刀）摑打｜摑（手）摑｜批（手）批。","端母d，「囤動」取「囤」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{437+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡多部中12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":"源自《系統漢語》卷六十二「蛇」部之「多部」（第370部）；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十五批.json"
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
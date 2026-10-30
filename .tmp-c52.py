import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
SUO=("部頭索：甲骨文象繩索形，字有多體——或作「屮串」「木串」「竹串」，指用草莖、麻皮、竹篾、藤條、樹皮搓成的繩索；加「又、𠬞」表用手搓，或加「幺、糸」表用絲線搓。轉義：單調單獨（索然、離群索居，《廣雅》「獨也」）；搜求討取（探索、索取）、法度；散（《玉篇》「散也」）、盡空（《廣韻》「盡也」）。辯證《說文》「从𣎵糸」據小篆不確；一〇是束、兩〇是串，捆束與成串義別。音源：音源字，源自搓繩聲。字族①索狀長條②索用搜索③索聲連續。")
SHU=("部頭束：从木从〇，「〇」象捆纏形，象意將散亂木柴捆在一起，〇楷化作囗（《說文》「縛也，从囗木」）。轉義：捆束、聚集、控制（《玉篇》「約束」）；事情結束。辯證：「束」初形變化多——「娕、餗」所从實為「索」（艸束），故同束；「敕」所从為「柬」，形近而訛；「朿」亦與「束」訛混。音源：音源字，源自束縛聲；束縛必用繩索，故義音同「索」；又義音同「聿」（《禮記》注「宿讀為肅」）。字族①捆束②聚集③結束。")
def card(ch,py,bu,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":[bu],"sources":["卷六十三  索.docx "+bu],
            "sections":[S("bengen","字根（"+bu+"）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","聲母义",sm)]}
rows=[
("𪍟","suǒ","371.索部",SUO,"𪍟＝麥（形旁）＋索（聲旁）。《篇海》「𪍺𪍟也」——麻花、饊子一類油炸的索狀麵食（原稿 p47 配圖「饊子」）。","①索狀：𪍟（麥）饊子（麵如索）｜饊（食）饊｜麵（麥）麵。","心母s，「失收」取「收」。"),
("𩄜","sè","371.索部",SUO,"𩄜（䨛）＝雨（形旁）＋索（聲旁）。《集韻》「䨛，雨也」；「䨛䨛，小雨，一曰霰皃」——雨絲如索。","①索狀：𩄜（雨）小雨／霰｜霰（雨）霰｜雨（雨）雨。","心母s，「失收」取「收」。"),
("𡩡","suǒ","371.索部",SUO,"𡩡＝宀（形旁）＋索（聲旁）。《說文》「入家𢯱也」入室搜索；《廣韻》「盡也、散也」；《集韻》「寂寞也」——**搜尽则寂**。","②搜索：𡩡（宀）搜索／寂寞｜搜（手）搜｜索（糸）索。","心母s，「失收」取「收」。"),
("𢱢","suǒ","371.索部",SUO,"𢱢＝手（形旁）＋索（聲旁）。《集韻》「摸𢱢也」摸索；sè《博雅》「取也、求也」，又「擇也」。","②搜索：𢱢（手）摸索／取擇｜摸（手）摸｜索（糸）索。","心母s，「失收」取「收」。"),
("𩌈","suǒ","371.索部",SUO,"𩌈＝革（形旁）＋索（聲旁）。《廣韻》「𩍜履也」；《釋名》「𩌈𩍜，鞾之缺前壅者，胡中所名也」——鞋頭不加護套的靴。","①索狀：𩌈（革）靴｜鞾（革）靴｜履（履）履。","心母s，「失收」取「收」。"),
("𠋲","sè","371.索部",SUO,"𠋲＝人（形旁）＋索（聲旁）。《集韻》「㒀𠋲，惡也」。","②搜索：𠋲（人）惡｜惡（心）惡｜㒀（人）㒀。","心母s，「失收」取「收」。"),
("䖛","suǒ","371.索部",SUO,"䖛＝虎（形旁）＋索（聲旁）。《玉篇》「虎皃」——虎紋如索。","①索狀：䖛（虎）虎貌｜虎（虍）虎｜彪（虎）彪。","心母s，「失收」取「收」。"),
("嗦","suō","371.索部",SUO,"嗦＝口（形旁）＋索（聲旁）。囉嗦、哆嗦；原稿「本義當指用嘴長吸狀」——如「嗦粉條」，索狀之物入口。","③索聲：嗦（口）長吸／囉嗦｜吸（口）吸｜嗖（口）嗖。","心母s，「失收」取「收」。"),
("𩘝","suǒ","371.索部",SUO,"𩘝＝風（形旁）＋索（聲旁）。《集韻》「風聲」——風如索之鳴。","③索聲：𩘝（風）風聲｜風（風）風｜颾（風）颾。","心母s，「失收」取「收」。"),
("𧛻","suǒ","371.索部",SUO,"𧛻＝衣（形旁）＋索（聲旁）。《集韻》「𧛻𧛻，衣聲」——衣索之聲。","③索聲：𧛻（衣）衣聲｜衣（衣）衣｜裘（衣）裘。","心母s，「失收」取「收」。"),
("束","shù","372.束部",SHU,"束＝从木从〇，〇象捆纏，象意把散亂木柴捆在一起。轉義：捆束、聚集、約束、結束。","①捆束：束（囗木）捆｜捆（手）捆｜縛（糸）縛。","審母sh，「失收」取「收」：收而束之。"),
("欶","shuò","372.束部",SHU,"欶（漱）＝欠（形旁）＋束（聲旁）。《說文》「吮也」——吮吸；又漱口。","②聚集：欶（欠）吮吸／漱｜吮（口）吮｜漱（水）漱。","審母sh，「失收」取「收」。"),
]
for ch,py,bu,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,bu,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{485+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,bu,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡索部余+束部首 2026-10-23","risk":"low","claims":[]}
for i,(cid,title,stmt) in enumerate(cl):
    bu=rows[i][2]
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":f"源自《系統漢語》卷六十三「索」部之「{bu.split('.')[1]}」；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十九批.json"
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
import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
SHU=("部頭束：从木从〇，「〇」象捆纏形，象意將散亂木柴捆在一起，〇楷化作囗（《說文》「縛也，从囗木」）。轉義：捆束、聚集、控制（《玉篇》「約束」）；事情結束。辯證：「娕、餗」所从實為「索」（艸束），故同束；「敕」所从為「柬」，形近而訛；「朿」亦與「束」訛混。音源：音源字，源自束縛聲；束縛必用繩索，故義音同「索」；又義音同「聿」。字族①捆縛收縮②聚集③結束。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["372.束部"],"sources":["卷六十三  索.docx 372.束部"],
            "sections":[S("bengen","字根（第372部：束部）",SHU),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("漱","shù","漱（涑）＝水（形旁）＋欶聲。《說文》「蕩口也」——含在口中一鼓一縮而蕩洗。","①收縮：漱（水）漱口（口一鼓一縮）｜盥（皿）盥｜洗（水）洗。","審母sh，「失收」取「收」。"),
("鏉","shòu","鏉（鎪）＝金（形旁）＋欶聲。《說文》「利也」；《集韻》「鏉鏽，鐵上衣」——鐵鏽；sōu「刻鏤」。","①收縮：鏉（金）利／鐵鏽（剝蝕）｜鏽（金）鏽｜鏤（金）鏤。","審母sh，「失收」取「收」。"),
("樕","sù","樕＝木（形旁）＋欶聲。《說文》「樸樕木」；徐鍇「即今小槲樹」——樹小而叢生，如被束。","①收縮：樕（木）小槲叢生｜槲（木）槲｜樸（木）樸。","心母s，「失收」取「收」。"),
("藗","sù","藗（蔌）＝艸（形旁）＋遬聲。《說文》「牡茅也」——白茅一類。","①收縮：藗（艸）牡茅｜茅（艸）茅｜菅（艸）菅。","心母s，「失收」取「收」。"),
("嗽","sòu","嗽（漱𠲿嗍）＝口（形旁）＋欶聲。咳嗽——《釋名》「促也，用口急促也」，喉如被束；shù 同漱。","①收縮：嗽（口）咳嗽（喉促）｜咳（口）咳｜喘（口）喘。","心母s，「失收」取「收」。"),
("凁","sōu","凁（𠘂）＝冫（形旁）＋束聲。《集韻》「冷也，一曰冰氣」——寒氣收縮。","①收縮：凁（冫）冷／冰氣｜冷（冫）冷｜凍（冫）凍。","心母s，「失收」取「收」。"),
("捒","shù","捒（摗竦駷）＝手（形旁）＋束聲。《廣韻》「裝捒」；《韻會》「與束同，縛也」。","①收縮：捒（手）裝束／縛｜縛（糸）縛｜束（囗木）束。","審母sh，「失收」取「收」。"),
("簌","sù","簌＝竹（形旁）＋束聲。《集韻》「篩也」；《康典》「茂密貌」——簌簌，葉落聲。","①收縮：簌（竹）篩／茂密｜篩（竹）篩｜蔌（艸）蔌。","心母s，「失收」取「收」。"),
("蔌","sù","蔌＝艸（形旁）＋束聲。《玉篇》「菜茹之揔名」——蔬菜總名。","①收縮：蔌（艸）菜蔬｜蔬（艸）蔬｜菜（艸）菜。","心母s，「失收」取「收」。"),
("速","sù","速（趚遬）＝辵（形旁）＋束聲。《說文》「疾也」——疾走時步間距離小而密，如腳被束縛。","①收縮：速（辵）快步（步密如束）｜疾（疒）疾｜急（心）急。","心母s，「失收」取「收」：步收而密則速。"),
("竦","sǒng","竦＝立（形旁）＋束（聲旁）。《說文》「敬也，束，自申束也」——四肢併攏而立；《爾雅》「懼也」；《廣雅》「上也」。","①收縮：竦（立）肅敬／聳立｜聳（耳）聳｜悚（心）悚。","心母s，「失收」取「收」。"),
("綀","shū","綀＝糸（形旁）＋束聲。《說文》「布屬」——一種像苧布的稀疏織物；《玉篇》「紡麤絲」。","①收縮：綀（糸）疏布｜疏（疋）疏｜布（巾）布。","審母sh，「失收」取「收」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{497+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡束部12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":"源自《系統漢語》卷六十三「索」部之「束部」（第372部）；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第五十批.json"
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
import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
SUO=("部頭索：甲骨文象繩索形，字有多體——或作「屮串」「木串」「竹串」，指用草莖、麻皮、竹篾、藤條、樹皮搓成的繩索；加「又、𠬞」表用手搓，或加「幺、糸」表用絲線搓。轉義：由繩索形→單調、單獨（索然無味、離群索居，《廣雅》「獨也」）；由用途→搜求、討取（探索、索取，《玉篇》「求也」）、法度；由零碎纖維構成→散（《玉篇》「散也」）、盡空（《廣韻》「盡也」）。辯證：《說文》「艸有莖葉可作繩索，从𣎵糸」據小篆析形不確；未加「又」的甲骨文或釋作「束」，但一是束、兩〇是串，捆束與成串義別，此字象繩索之形，加「又」者實即「𢱢」（搓繩）。音源：音源字，源自搓繩聲。字族①索狀長條②形近「束」之訛。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["371.索部"],"sources":["卷六十三  索.docx 371.索部"],
            "sections":[S("bengen","字根（第371部：索部）",SUO),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("索","suǒ","索＝象繩索形（屮串/木串/竹串），加又表搓——草麻竹藤搓成的繩；引申單獨、搜求、法度、散、盡。","①索狀：索（糸）繩索｜繩（糸）繩｜糾（糸）糾。","心母s，「失收」取「收」：搓而收束。"),
("鎍","suǒ","鎍＝金（形旁）＋索（聲旁）。《集韻》「鐵繩也」；sè「鐵丳」——烤肉鐵籤。","①索狀：鎍（金）鐵繩／鐵籤｜鍊（金）鍊｜籤（竹）籤。","心母s，「失收」取「收」。"),
("溹","suò","溹（𣽤洓）＝水（形旁）＋索（聲旁）。《集韻》「水名，在滎陽」；sè「溹溹，雨下皃」。","①索狀：溹（水）水名／雨下｜洓（水）小雨｜雨（雨）雨。","心母s，「失收」取「收」。"),
("𦵫","suǒ","𦵫＝艸（形旁）＋索（聲旁）。《玉篇》「艸名」。","①索狀：𦵫（艸）草名｜艸（艸）草｜藤（艸）藤。","心母s，「失收」取「收」。"),
("㮦","sè","㮦（梀）＝木（形旁）＋索（聲旁）。《廣韻》「白索，木名」；《爾雅》「赤栜，或作赤㮦」——木紋可作椀。","①索狀：㮦（木）木名（紋縷）｜梀（木）梀｜栜（木）栜。","心母s，「失收」取「收」。"),
("䅴","suǒ","䅴＝禾（形旁）＋索（聲旁）。《集韻》「禾皃」；sè「禾穗」。","①索狀：䅴（禾）禾穗｜穗（禾）穗｜禾（禾）禾。","心母s，「失收」取「收」。"),
("𤸴","suǒ","𤸴＝疒（形旁）＋索（聲旁）。《集韻》「脈動」。","①索狀：𤸴（疒）脈動（如索）｜脈（肉）脈｜動（力）動。","心母s，「失收」取「收」。"),
("𥰼","suǒ","𥰼＝竹（形旁）＋索（聲旁）。《集韻》「竹絙也」——竹索。","①索狀：𥰼（竹）竹索｜絙（糸）絙｜索（糸）索。","心母s，「失收」取「收」。"),
("𩮛","suǒ","𩮛＝髟（形旁）＋索（聲旁）。《集韻》「髮堅皃」；《類篇》「髮豎皃」——頭髮硬直如索。","①索狀：𩮛（髟）髮豎（如索）｜髮（髟）髮｜豎（豆）豎。","心母s，「失收」取「收」。"),
("䞽","suǒ","䞽＝走（形旁）＋索（聲旁）。《廣韻》「䞦䞽，僵仆」——仆倒。","①索狀：䞽（走）僵仆｜仆（人）仆｜僵（人）僵。","心母s，「失收」取「收」。"),
("𧎳","suǒ","𧎳＝虫（形旁）＋索（聲旁）。《玉篇》「先各切，音索，虫名」。","①索狀：𧎳（虫）蟲名｜蟲（虫）蟲｜蚓（虫）蚓。","心母s，「失收」取「收」。"),
("𥻨","sè","𥻨＝米（形旁）＋索（聲旁）。《類篇》「煑米為𥻨」；《食經》「取蒸米置沸湯……出著新籮內」——煮米多水。","①索狀：𥻨（米）煮米｜粥（米）粥｜飯（食）飯。","心母s，「失收」取「收」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
cl=[(f"zk-{473+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡371索部首12条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":"源自《系統漢語》卷六十三「索」部之「索部」（第371部）；字卡五步规程。","permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十八批.json"
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
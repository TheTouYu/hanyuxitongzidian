import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
M=("部頭名：从口从夕，夜晚昏暗互不相見而自報姓名（《說文》「自命也…冥不相見，故以口自名」）。轉義名稱、旌表、辨明、大而成人。音源：義音同「冥」。字族衍義：①夜晚朦朧 ②名字→銘刻辨明。")
Q=("部頭䏌（xì）：本「八月」合體，指八月；「八」亦表分開，从月（夕）表示月之圓缺，以十五日為序分上弦下弦、循環往復。轉義：月之變化→舞蹈行列有序，分化作「佾」。"
   "辯證：《說文》「振䏌也，从肉八聲」因「肉月」形近而誤。音源：本夕聲，因行列義而義音同「失」（佚、泆並作佾）。")
def card(ch,py,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["366.夕部"],"sources":["卷六十二  蛇.docx 366.夕部"],
            "sections":[S("bengen","字根（第366部：夕部／名／䏌）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("姳","mǐng",M,"姳＝女（形旁）＋名（聲旁）。《集韻》引「好也」。","①朦朧：姳（女）好｜佲（人）好｜酩（酉）醉。","明母m，「蒙末」取「蒙」。"),
("㚚","kōng",M,"㚚＝大（形旁）＋名（聲旁）。《集韻》「大也」；kuāng《篇海》「犬聲也」——狗叫。","①朦朧：㚚（大）大／犬聲｜名（口）名｜吠（犬）吠。","溪母k，「口控」取「控」。"),
("䊅","míng",M,"䊅＝米（形旁）＋名（聲旁）。《集韻》「漬米也」——浸米。","①朦朧：䊅（米）漬米｜𥿨（糸）細絲｜酩（酉）醉。","明母m，「蒙末」取「蒙」。"),
("𥿨","míng",M,"𥿨＝糸（形旁）＋名（聲旁）。《集韻》「細絲也」；《類篇》「絲也」。","①朦朧：𥿨（糸）細絲｜䊅（米）漬米｜絲（糸）絲。","明母m，「蒙末」取「蒙」。"),
("銘","míng",M,"銘＝金（形旁）＋名（聲旁）。《釋名》「銘，名也，記名其功也」——記載、刻鏤；《禮·檀弓》「銘，明旌也」。","②名字：銘（金）刻名｜名（口）名｜旌（㫃）明旌。","明母m，「蒙末」取「蒙」。"),
("洺","míng",M,"洺＝水（形旁）＋名（聲旁）。《說文新附》「水名」洺河（河北武安），季節性強；疑指水線如銘刻。","②名字：洺（水）水名｜銘（金）刻｜河（水）河。","明母m，「蒙末」取「蒙」。"),
("詺","míng",M,"詺＝言（形旁）＋名（聲旁）。《廣韻》「詺目」；《增韻》「辨別物名」——直言、真義。","②名字：詺（言）辨名｜名（口）名｜辨（辛）辨。","明母m，「蒙末」取「蒙」。"),
("𪗸","míng",M,"𪗸＝齒（形旁）＋名（聲旁）。《玉篇》「莫丁切，音名，齒也」。","②名字：𪗸（齒）齒｜齒（齒）齒｜名（口）名。","明母m，「蒙末」取「蒙」。"),
("肸","xì",Q,"肸＝十（形旁）＋䏌（聲旁）。《說文》「響，布也」；《康典》「肸蠁，盛作也」——聲響散布、盛作。","行列：肸（十）聲布｜佾（人）行列｜響（音）響。","曉母x，「續消」取「消」。"),
("佾","yì",Q,"佾＝人（形旁）＋䏌（聲旁）。《說文新附》「舞行列也」；行數人數縱橫皆同故曰佾（《左傳》「始用六佾」）。","行列：佾（人）舞列｜肸（十）聲布｜列（刀）列。","喻母y，不系。"),
]
for ch,py,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「夕部」（第366部）；字卡五步规程。"
cl=[(f"zk-{336+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡夕部第三10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十五批.json"
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
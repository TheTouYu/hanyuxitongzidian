import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
Y=("部頭易：甲骨文象傾盞注液之形，分化為「易」（施與）與「益」（受注）二系。轉義轉換、改變、容易。辯證：《說文》以蜥蜴為本義不確。音源：借音，義音同「也」。字族衍義：①改易 ②簡易 ③形近「昜」之訛。")
T=("部頭裼（xì）：甲骨文从又从衣，象意脫衣露體，是「裼」的初文（《說文》「裼，袒也」，《玉篇》「脫衣見體也」）。"
   "轉義：袒露→繈褓（緥）；赤身露體之北方部族→狄；借音，義音同「易」。字族衍義：多指改換、轉變。")
def card(ch,py,head,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["367.易部"],"sources":["卷六十二  蛇.docx 367.易部"],
            "sections":[S("bengen","字根（第367部：易部）",head),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("睗","shì",Y,"睗＝目（形旁）＋易（聲旁）。《說文》「目疾視也」——急速地看、眨巴眼；或同「賜」。","①改易：睗（目）疾視｜賜（貝）賜｜眴（目）眴。","審母sh，「失收」取「收」。"),
("踢","tī",Y,"踢（迭）＝足（形旁）＋易（聲旁）。《正字通》「以足蹵物」——用腳擊物；dié 更迭。","①改易：踢（足）踢｜蹵（足）蹴｜迭（辵）迭。","透母t，「涂突」取「突」：足突起而擊。"),
("掦","tì",Y,"掦＝手（形旁）＋易（聲旁）。《正字通》「挑掦也，亦借剔，與揚別」——挑出。","①改易：掦（手）挑｜剔（刀）剔｜揚（手）揚。","透母t，「涂突」取「突」。"),
("𩛿","xíng",Y,"𩛿（餳）＝食（形旁）＋易（聲旁）。《說文》「飴和饊者也」——飴糖和糯米粉熬成；熱軟冷硬，故从易。","①改易：𩛿（食）飴糖｜餳（食）同｜飴（食）飴。","心母x，「失收」取「失」。"),
("裼","xì",T,"裼＝衣（形旁）＋易（聲旁）。本義袒露（脫衣見體）；引申繈褓、狄（赤身部族）。","①改換：裼（衣）袒｜緥（糸）繈褓｜狄（犬）狄。","心母x，「失收」取「失」。"),
("㑥","yì",T,"㑥＝人（形旁）＋易（聲旁）。《說文》「輕也，一曰交㑥」——輕慢、交易。","①改換：㑥（人）輕慢／交｜易（皿）交易｜輕（車）輕。","喻母y，不系。"),
("埸","yì",T,"埸＝土（形旁）＋易（聲旁）。《說文新附》「疆也」——田界、邊境、道路。","①改換：埸（土）田界｜疆（田）疆｜畔（田）畔。","喻母y，不系。"),
("逷","tì",T,"逷＝辵（形旁）＋狄（聲旁）。《說文》「逖，遠也」，逷為古文逖。","①改換：逷（辵）遠｜逖（辵）同｜遠（辵）遠。","透母t，「涂突」取「突」。"),
("剔","tī",T,"剔＝刀（形旁）＋易（聲旁）。《說文》「解骨也」——分解骨肉；《集韻》「治也」「剃也」。","①改換：剔（刀）解骨｜剃（刀）剃｜解（角）解。","透母t，「涂突」取「突」。"),
("𩋌","yì",T,"𩋌＝韋（形旁）＋易（聲旁）。《集韻》「素𩋌，履也」——葦編草鞋，如今涼鞋。","①改換：𩋌（韋）草鞋｜屨（尸）屨｜屩（尸）屩。","喻母y，不系。"),
]
for ch,py,head,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,head,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「易部」（第367部）；字卡五步规程。"
cl=[(f"zk-{373+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,head,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡易部第二10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十九批.json"
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
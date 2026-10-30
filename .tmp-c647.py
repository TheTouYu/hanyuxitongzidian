import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第525部「羌部」】羌＝从人从羊，象牧羊之人或以羊為圖騰的西方部族。《說文》「西戎牧羊人也」。轉義：被拘系→強；遊牧褐膚→紅。字族分三面：羊狀（叫、咪眼、癢）／直接相關之物／形近「失」之訛。"
N="字形：古文字字形库未收。"
D=[("羌","qiāng",FY,"从人从羊：西方牧羊之族；引申強（《廣雅》）、紅色（《玉篇》）。","q「亲缺」取「亲」：族亲相聚。"),
("猐","qiāng",FY,"从犬羌聲：同「羌」（《廣韻》）。","q取亲缺：族聚而親。"),
("𡬎","qiāng",FY,"从宀羌聲：音羌，義同（《五侯鯖字海》）。","q取亲缺：居而亲。"),
("唴","qiàng",FY,"从口羌聲：秦晉謂兒泣不止曰唴（《說文》），如羊叫。","q取亲缺：哭而親。"),
("𥇉","liǎng",FY,"从目良聲：䀶，目病，斜視（《集韻》）。","l「拢离」取「离」：目斜而离。"),
("㳾","qiāng",FY,"从水羌聲：水名，本作羌（《正字通》）。","q取亲缺：水聚而親。"),
("琷","què",FY,"从玉羌聲：音闕，人名（《字彙補》）。","q取亲缺：借聲記名。"),
("𦏱","yǎng",FY,"从羊養聲：音癢；又與瘥同（疾愈）（《海篇》）。","y「圆容」取「圆」：病愈而周。"),
("蜣","qiāng",FY,"从虫羌聲：蜣蜋，啖糞蟲，所推糞球如羊屎（《玉篇》）。","q取亲缺：蟲聚而親。"),
("㛨","qiǎng",FY,"从女羌聲：亂貌（《字彙》）。","q取亲缺：女聚而乱。"),
("𥓌","qiǎng",FY,"从石羌聲：𥓌礰石，薑石，鈣質結核似乾薑（《本草綱目》）。","q取亲缺：石結而親。"),
("𪁸","qiāng",FY,"从鳥羌聲：鳥名；《正字通》謂「䳀」之譌（形近失）。","q取亲缺：借聲記鳥。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：羊狀（唴如羊叫／𥇉目病／𦏱音癢）、直接相關之物（蜣蜋／𥓌石／琷人名）、形近「失」之訛（𪁸為䳀之譌）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":525,"name":"羌"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqiang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）：{xp}",
 "boundary":"源自《系統漢語》第525部「羌部」（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡525a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡525a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡525a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
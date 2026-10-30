import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第527部「向部」·尚系（二级字根）】尚＝从八向聲：分開并開窗，為「敞」之初文；字族三面：敞開敞亮／推舉罩覆／來回反復。"
N="字形：古文字字形库未收。"
D=[("橖","táng",FY,"《唐韻》「車橖也」、《集韻》「車木」；又音 chēng，柱也。","t「涂突」取「涂」：木橫而鋪。"),
("嫦","cháng",FY,"《正字通》「俗姮字」，人名用字（嫦娥）。","ch「刺持」取「持」：借聲為名。"),
("䉎","táng",FY,"《廣韻》「罩也」，竹製罩具。","t取涂突：竹罩而鋪。"),
("鞝","zhǎng",FY,"《玉篇》「扇安皮也」，扇形鞍皮；或指縫合鞋幫。","zh「凿总」取「总」：皮合而總。"),
("償","cháng",FY,"《說文》「還也」；《廣韻》「報也、當也、復也」。","ch取刺持：報還而持。"),
("埫","chǒng",FY,"《廣韻》「埫塎，不安」；又音 shǎng，十畝為一埫。","ch取刺持：土高而持。"),
("𪄹","cháng",FY,"《集韻》「䳯𪄹，鳥名，或从隹」。","ch取刺持：鳥名而持。"),
("徜","cháng",FY,"《玉篇》「徜徉，猶徘徊也」，自由往來。","ch取刺持：行而徘徊。"),
("惝","tǎng",FY,"《玉篇》「惝怳，失志不悅皃」，失意無所適從。","t取涂突：心散而突。"),
("倘","tǎng",FY,"《集韻》「止皃，一曰自失皃」，驚疑欲止；又音 cháng，倘佯＝徜徉。","t取涂突：止而突。"),
("趟","tāng",FY,"《廣韻》「䞴趟，躍跳」；今音 tāng 從淺水走過、tàng 走動次數。","t取涂突：足踏而突。"),
("淌","tǎng",FY,"《玉篇》「大波」；今義流出、流下。","t取涂突：水流而突。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"尚系尾組諧聲字分三面：敞開敞亮（橖／䉎）／推舉罩覆（償／鞝／埫）／來回反復（徜／惝／倘／趟／淌）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshang2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
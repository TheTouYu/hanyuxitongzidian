import json,subprocess,os,glob
B="【418 亥部】亥＝甲骨文象直立的旱獭形，「鼥」之初文；转义：掘食草根→荄，直立放哨→警惕·防备（该）、受惊竖立（骇），爪尖善掘→刻镂，传播鼠疫近似疟疾→痎，借指地支末位（对应豕）。辯證：字形近「豕」且恰应生肖，故或混同，《说文》「从二，二古文上字」析形不确。音源：源自旱獭叫声，因有直挺义而义音同「介」。"
N="字形：古文字字形库未收。"
D=[
{"ch":"郂","p":"gāi","xp":"《说文》「陈留乡」——乡名；又邑名。","sm":"g「隔估」取「隔」：乡邑隔界。"},
{"ch":"陔","p":"gāi","xp":"《说文》「阶次也」——台阶、殿阶次序；又田埂、重也。","sm":"g「隔估」取「隔」：阶隔而升。"},
{"ch":"垓","p":"gāi","xp":"《说文》「兼垓八极地也」——本义当指高台，引申中心地带；垓下即其例。","sm":"g「隔估」取「隔」：高台隔四野。"},
{"ch":"晐","p":"gāi","xp":"《说文》「兼晐也」——日光普照，引申兼备、咸、兼。","sm":"g「隔估」取「隔」：日照无隔。"},
{"ch":"劾","p":"hé","xp":"《说文》「法有罪也」——定罪审判、检举罪状；又勤力。","sm":"h「豁活」取「豁」：发奸而豁。"},
{"ch":"賅","p":"gāi","xp":"《广韵》「赡也」——完备；《玉篇》「奇也，非常也」。","sm":"g「隔估」取「隔」：赅而无所隔。"},
{"ch":"㚊","p":"kāi","xp":"《玉篇》「多也、大也」。","sm":"k「口控」取「控」：多而控张。"},
{"ch":"㧡","p":"hài","xp":"《玉篇》「撼动也」；又担也。","sm":"h「豁活」取「豁」：撼而豁动。"},
{"ch":"絯","p":"gāi","xp":"《集韵》「拘束也」——拘束约束；又挂也、大丝。","sm":"g「隔估」取「隔」：丝隔而束。"},
{"ch":"峐","p":"gāi","xp":"《尔雅》「无草木峐」——草木不生的山。","sm":"g「隔估」取「隔」：山隔草木。"},
{"ch":"姟","p":"gāi","xp":"《集韵》「十经曰姟」——古代一万万为垓，同垓之数。","sm":"g「隔估」取「隔」：数隔而积。"},
{"ch":"輆","p":"kǎi","xp":"《集韵》「輆軩，不平也」——车行不平；又碍也。","sm":"k「口控」取「控」：车控而颠。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取亥部「旱獭直立——放哨／掘根／刻掘」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第418部「亥部」（卷七十 亥）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡418b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡418b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡418b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
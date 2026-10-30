import json,subprocess,os,glob
B="【418 亥部】亥＝甲骨文象直立的旱獭形，「鼥」之初文；转义：掘食草根→荄，直立放哨→警惕·防备（该）、受惊竖立（骇），爪尖善掘→刻镂，传播鼠疫近似疟疾→痎，借指地支末位。辯證：字形近「豕」且恰应生肖，故或混同，《说文》「从二，二古文上字」析形不确。音源：源自旱獭叫声，因有直挺义而义音同「介」。"
N="字形：古文字字形库未收。"
D=[
{"ch":"㤥","p":"hài","xp":"《说文》「苦也」——愁苦、患苦、愁畏。","sm":"h「豁活」取「豁」：心豁而苦。"},
{"ch":"該","p":"gāi","xp":"《说文》「军中约也」——军中警戒条约，引申备、咸、兼、皆。","sm":"g「隔估」取「隔」：约以隔限。"},
{"ch":"閡","p":"ài","xp":"《说文》「外闭也」——从外面关门，即耳门、栅栏。","sm":"h「豁活」取「豁」：闭而复豁。"},
{"ch":"咳","p":"hái","xp":"《说文》「小儿笑也」，古文从子作「孩」；ké/kài 同「欬」，嗽也。","sm":"h「豁活」取「豁」：笑则口豁。"},
{"ch":"欬","p":"kài","xp":"《说文》「屰气也」——胃气上逆，今谓咳嗽；又謦欬言笑。","sm":"k「口控」取「控」：气控而逆。"},
{"ch":"䬵","p":"gāi","xp":"《集韵》「饴也」——饴糖；ài 读通食气、打嗝、食久而变味。","sm":"g「隔估」取「隔」：食隔而饐。"},
{"ch":"痎","p":"jiē","xp":"《说文》「二日一发疟」——疟疾；旱獭易染鼠疫，症状近似。","sm":"j「聚决」取「聚」：寒热聚而发。"},
{"ch":"侅","p":"gāi","xp":"《说文》「奇侅，非常也」——不平常；又饮食至咽曰侅（噎）。","sm":"g「隔估」取「隔」：噎隔不下。"},
{"ch":"硋","p":"ài","xp":"《集韵》「碍，止也」——阻碍；《玉篇》「止石」。","sm":"h「豁活」取「豁」：石塞而碍。"},
{"ch":"䀭","p":"gāi","xp":"《集韵》「目大貌」——䀭瞩，众相视貌。","sm":"g「隔估」取「隔」：目张而视。"},
{"ch":"㱾","p":"gāi","xp":"《说文》「㱾改，大刚卯也，以逐精鬼」——汉代正月卯日所佩驱邪饰。","sm":"g「隔估」取「隔」：佩以隔鬼。"},
{"ch":"氦","p":"hài","xp":"极轻无色惰性气体元素 He——音译字。","sm":"h「豁活」取「活」：气活而轻。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取亥部「旱獭直立放哨——警惕·闭塞」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第418部「亥部」（卷七十 亥）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡418c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡418c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡418c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
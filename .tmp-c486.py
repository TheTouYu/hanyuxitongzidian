import json,subprocess,os,glob
B="【418 亥部（原属鼥）】亥＝甲骨文象直立的旱獭形，「鼥（bá）」之初文（《正字通》「鼧鼥鼠，生西番山泽中，穴土为窠，形似獭」），旱獭体粗壮、头大耳小、四肢粗短，常直立放哨。转义：喜掘食草根→草根（荄）；直立放哨→警惕防备（该）、受惊直立（骇）；爪尖善掘→刻镂（刻）；传播鼠疫近似疟疾→痎；借指地支末位（对应豕）。辯證：字形近「豕」且恰应生肖豕，故或混同，《说文》「荄也……从二，二古文上字」析形不确。音源：音源字，源自旱獭叫声；因有直挺义而义音同「介」。字族衍义：①牙尖爪利→刻镂 ②直立→惊起竖立 ③直立放哨→警惕依靠 ④掘食草根 ⑤鼠疫疟疾。"
N="字形：古文字字形库未收。"
D=[
{"ch":"亥","p":"hài","xp":"本部部首字，象直立旱獭——「鼥」之初文。","sm":"h「豁活」取「豁」：惊起而豁张。"},
{"ch":"刻","p":"kè","xp":"《说文》「镂也」——旱獭爪尖利善掘，故引申刻镂。","sm":"k「口控」取「控」：刀控而刻。"},
{"ch":"荄","p":"gāi","xp":"《说文》「草根也」——旱獭掘食草根。","sm":"g「隔估」取「隔」：根隔土而生。"},
{"ch":"核","p":"gāi","xp":"《说文》「蛮夷以木皮为箧」——树名；hé 读「果中实」；又檐也。","sm":"h「豁活」取「活」：果中有活。"},
{"ch":"駭","p":"hài","xp":"《说文》「惊也」——马受惊抬起前腿站立。","sm":"h「豁活」取「豁」：惊而豁起。"},
{"ch":"豥","p":"gāi","xp":"《尔雅》「豕四蹢皆白」——猪受惊，与骇义同。","sm":"g「隔估」取「隔」：惊而隔立。"},
{"ch":"骸","p":"hái","xp":"《说文》「胫骨也」——小腿骨，引申骨骼、身体。","sm":"h「豁活」取「活」：骨撑身活。"},
{"ch":"胲","p":"gāi","xp":"《说文》「足大指毛也」——足大指长毛处之肉；又颊下；又羟胺（译音）。","sm":"g「隔估」取「隔」：肉隔指间。"},
{"ch":"頦","p":"hái","xp":"《说文》「丑也」——直立时龇牙咧嘴故丑，又指下巴、脸颊。","sm":"h「豁活」取「豁」：口张齿豁。"},
{"ch":"𨀖","p":"hài","xp":"《集韵》「行急」——行走急促。","sm":"h「豁活」取「豁」：行急而豁。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取亥部「旱獭直立——放哨／掘根／惊起」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第418部「亥部」（卷七十 亥）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡418a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡418a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡418a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
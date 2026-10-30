import json,subprocess,os,glob
BZAI="【417 宰部（从宀从辛）】宰＝从宀从辛，象意家里负责主刀的人，即屠夫、杀牲畜者，为「𣪮」之初文；转义主管、主持→治理；古代宰杀兼用刀杀与沉、埋、缢，故又引申指坟墓、渣滓（分化作滓）。辯證：《说文》以「辛」为罪，故释「辠人在屋下执事者」，不确。音源：因水淹之意而义音同「甾」（滓／缁互作）。字族衍义：①主管统领 ②宰杀灭绝 ③淹死、形色如渣滓 ④形近「𡨧」之讹。"
N="字形：古文字字形库未收。"
D=[
{"ch":"𥻮","p":"cuì","xp":"《字汇补》「粉𥻮也」；又「𩝪，饵也」——糕饼，两字同义，取渣滓细末意。","sm":"z「凿总」取「总」：粉末总聚。"},
{"ch":"䮨","p":"zǎi","xp":"《集韵》「马杂毛骢色」——青白相间，正字通以为讹字；取「滓」意，指色如淤泥。","sm":"z「凿总」取「总」：毛色总杂。"},
{"ch":"𧪹","p":"xià","xp":"《字汇补》「诳也」——欺骗迷惑；所从「卒」本应为「乎」。","sm":"z「凿总」取「总」：言总而诳。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":BZAI,"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取宰部「主刀分肉／淹死成滓」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":"源自《系統漢語》第417部「宰部」（卷六十九 舄）；字卡五步规程。",
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡417b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡417b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡417b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
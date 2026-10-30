import json,subprocess,os,glob
F="【429 立部·顆粒】立之第二支取「粒」义：物分散成颗曰粒，故有摧折、崩裂诸字。"
FR="【430 戾部】戾＝从犬从立，立亦声——犬后腿直立、张牙舞爪欲扑；马抬前腿立义同（与亥、犮所指本同）。四足者抬腿直立为异常，故引申乖张背谬、凶残。辨证：战国古文讹「立」为「户」，小篆从之，《说文》「从犬在户下，身曲戾也」析形不确。字族多指立而不稳之状。"
N="字形：古文字字形库未收。"
D=[("粒","lì",F,"《说文》「糂也」——米粒；分散成颗。","l「拢离」取「离」：米散成颗。"),
("拉","lā",F,"《说文》「摧也」——折断、败；又招邀同行，拽离原处。","l取离：拽使离位。"),
("柆","lā",F,"《说文》「折木也」——折断树木。","l取离：木折而离。"),
("㕇","lā",F,"《说文》「石声也」——石头崩裂之声。","l取离：石裂而离。"),
("泣","qì",F,"《说文》「无声出涕曰泣」——不出声而流泪。","q「亲缺」取「缺」：泪缺而出。"),
("垃","lā",F,"垃圾——尘土与弃物。","l取离：弃物离散。"),
("啦","lá",F,"助词，作用略同「了」。","l取离：语助收句。"),
("砬","lā",F,"《广韵》「砬礘，石声」；一曰石药能制药毒。","l取离：石裂声离。"),
("鞡","lɑ",F,"靰鞡——东北垫靰鞡草的暖鞋。","l取离：草垫而离寒。"),
("戾","lì",FR,"犬立而欲扑，引申乖张背谬、凶残；字族指立而不稳。","l取离：犬立而离常。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取立部「散成颗／折使离」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第429－430部（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡429b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡429b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡429b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
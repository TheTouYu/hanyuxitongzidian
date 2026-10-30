import json,subprocess,os,glob
F="【472 𢌳部】𢌳＝从肉从𠬞（拱手），肉的状如拱手，即「頯」之初文，指顴骨；轉義为弓弩之柄（持弩拊）。"
FY="【473 癸部】癸＝甲骨文象測日影以定方位时所画的线条，为「揆」之初文（揆，度也）；古人建宫先以日影正方位，圭表圭臬即其器，故古「圭」「癸」可通。"
N="字形：古文字字形库未收。"
D=[("𢌳","kuí",F,"本部部首字：顴骨→弓弩柄（持弩拊）。","k「口控」取「控」：骨凸而控。"),
("頯","kuí",F,"从頁𢌳聲：《說文》「權也」，顴骨；《莊子》「其顙頯」。","k取控：顙骨外控。"),
("癸","guǐ",FY,"本部部首字：測影畫線（揆之初文）；天干第十，借為序數。","g「隔估」取「隔」：畫線分界。"),
("揆","kuí",FY,"从手癸聲：《說文》「葵也」，《廣雅》「度也」，揆度、揆理。","k取控：手度而控。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「骨相拱起／日影畫線」两面：頁取骨，手取度。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lca-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第472－473部（卷七十七 蛙）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡473a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡473a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡473a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
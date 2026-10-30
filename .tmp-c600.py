import json,subprocess,os,glob
F="【484 尾部】尾＝象人後有尾之形（古人或飾系尾，西南夷皆然），本指尾巴，引申末端、尾隨；音源借音，尾狀如穗，義音同「彗」（《書》「鳥獸孳尾」，《史記》作「微」）。"
FY="【485 毀部】毀＝从攴从臼从工，工指夯土之杵、臼指舂穀之臼、攴指擊打，象搗杵擊打破壞；轉義為毀謗、毀壞；音源字，取搗物之聲。"
N="字形：古文字字形库未收。"
D=[("尾","wěi",F,"本部部首字：人後之尾→末端、尾隨、尾數。","w「蒙末」取「末」：尾在末。"),
("娓","wěi",F,"从女尾聲：《說文》「順也」，娓娓而談、柔順。","w取末：女順而末。"),
("毀","huǐ",FY,"本部部首字：搗杵擊打→破壞、缺損、毀謗。","h「豁活」取「豁」：擊而豁破。"),
("燬","huǐ",FY,"从火毀聲：火焚、燒毀（《詩》「王室如燬」）。","h取豁：火烈而豁。"),
("隳","huī",FY,"从阜毀聲：毀壞城郭牆垣，引申隳敗。","h取豁：城塌而豁。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取尾部「末端垂垂」與毀部「擊打破損」兩面：女取其順，火阜取其破。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcl-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第484－485部（卷七十九 彗）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡485a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡485a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡485a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
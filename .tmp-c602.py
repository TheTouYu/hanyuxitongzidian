import json,subprocess,os,glob
F="【491 干部】干＝象樹杈形，樹杈是原始先民最簡單有效的狩獵工具：攻可叉住獵物頭部使其不能動，守可叉擋猛獸；為增牢固在分叉處綁石塊（或作）。本義為干犯、求取、扞衛。音源字，取敲擊樹杈之聲。"
N="字形：古文字字形库未收。"
D=[("干","gān",F,"本部部首字：樹杈叉具→干犯、求取、扞衛、干祿。","g「隔估」取「隔」：叉以隔物。"),
("旱","hàn",F,"从日干聲：久晴不雨致旱，取干之乾燥義。","h「豁活」取「豁」：日烈而豁。"),
("竿","gān",F,"从竹干聲：竹之直而長者，取干之主干義。","g取隔：竹節相隔。"),
("單","dān",F,"【492 單部】象在干杈端另綁兩塊石頭之形——前端為杈、面寬，宜於投擲擊倒奔跑動物（《集韻》「單至，輕發之皃」）；音源本干聲，因「單、嘼」相混而轉以蟬鳴為聲。","d「囤动」取「囤」：石囤於杈。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取干部「樹杈可叉、可擲」兩面：日取其燥，竹取其直，單取其重石。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcn-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第491－492部（卷八十 干）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡492a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡492a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡492a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
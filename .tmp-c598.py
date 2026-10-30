import json,subprocess,os,glob
F="【482 帚部】帚＝草穗紮成的掃帚；部內从帚諸字取「隱蔽、刷洗、徵召懲戒」三面：一形从又从攴，象人頭上戴彐（草穗）為偽裝而以攴擊之，是「微」之初文（隱行也）；「徵」與「微」同源，側重攴（施為於隱者）故為徵召、懲戒。"
N="字形：古文字字形库未收。"
D=[("微","wēi",F,"本部内字：戴穗偽裝而隱行，本義隱蔽、微細、衰微。","w「蒙末」取「蒙」：蒙穗而隱。"),
("徵","zhēng",F,"从微省：行於微而文達者即徵之，故為徵召、徵驗；引申懲戒（分化作懲）。","zh「凿总」取「总」：徵召而總。"),
("懲","chéng",F,"从心徵聲：戒止、懲創，取徵之懲戒義。","ch「刺持」取「持」：懲而持戒。"),
("敱","ái",F,"从豆上有彐：以草穗刷洗食器，本義有所治也。","a零声母：器治而安。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取帚部「穗可偽裝、可刷洗」两面：心取戒，豆取治。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcj-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第482部帚部（卷七十九 彗）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡482b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡482b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡482b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
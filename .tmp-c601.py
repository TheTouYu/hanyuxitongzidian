import json,subprocess,os,glob
F="【486 美部】美＝象人頭上用羽毛或羊角等裝飾之形，象意儀容裝扮好看，本義美善（《廣韻》「好色」）；轉義為讚美、美好、甘美。部內从美諸字皆取「裝飾好看、因好而欲」兩面。"
N="字形：古文字字形库未收。"
D=[("美","měi",F,"本部部首字：頭戴羽角裝飾→好看、美善、甘美。","m「蒙末」取「蒙」：羽飾蒙首。"),
("媄","měi",F,"从女美聲：《說文》「色好也」，女子貌美。","m取蒙：女色蒙美。"),
("媺","měi",F,"从女微聲：美善（同「媄」），取微之細好。","m取蒙：細好而媺。"),
("羨","xiàn",F,"从羊从㳄（涎）：見羊肉而垂涎，本義貪欲、羨慕，引申有餘。","x「续消」取「续」：涎續而羨。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取美部「裝飾好看、因好生欲」兩面：女取其色，羊取其涎。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcm-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第486部美部（卷七十九 彗）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡486a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡486a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡486a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
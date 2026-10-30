import json,subprocess,os,glob
F="【481 彗部】彗＝象兩彐（草穗）之形，彐象蘆葦、茅草的穗子，兩迭表眾多；音源字，取風吹穗子或穗子抽打之聲。480部後部內另有「雪」（从雨彗聲，雪花如葦絮）。"
FY="【482 帚部】帚＝甲骨文从屮上有彐（草穗），或加表示束縛捆紮之形，象用草穗紮成的掃帚；音源字，取掃帚掃地之聲（掃如爬搔，義音同「蚤」）。"
N="字形：古文字字形库未收。"
D=[("彗","huì",F,"本部部首字：草穗兩疊→掃帚、彗星（拖如帚尾）。","h「豁活」取「豁」：穗散而豁。"),
("雪","xuě",F,"从雨彗聲：雪花如葦絮，故从彗；《釋名》「綏綏然下」。","x「续消」取「续」：絮續而落。"),
("帚","zhǒu",FY,"本部部首字：草穗紮成的掃帚。","zh「凿总」取「总」：穗總而成帚。"),
("掃","sǎo",FY,"从手帚聲（或作埽）：持帚除穢，引申掃蕩、掃興。","s「失收」取「收」：收穢而掃。"),
("婦","fù",FY,"从女持帚：執箕帚之婦，本指主灑掃之事者，引申妻、婦人。","f「附分」取「附」：執帚而附。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取彗帚一系「草穗可束、可掃、可抽打」三面：雨取其絮，手提之，女執之。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lci-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第481－482部（卷七十九 彗）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡482a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡482a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡482a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
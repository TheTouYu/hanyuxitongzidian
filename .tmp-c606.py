import json,subprocess,os,glob
F="【497 生部】生＝象草木从地面长出之形，本義生長、生育（《說文》「進也」）；轉義生命、生熟、生計。部內从生諸字取「生長、所生」兩面。"
N="字形：古文字字形库未收。"
D=[("生","shēng",F,"本部部首字：草木出土→生長、生育、生命。","sh「失收」取「收」：草收而復生。"),
("星","xīng",F,"从晶生聲（本作曐）：夜空中發光的天體，取生之聲。","x取续消：星續而閃。"),
("青","qīng",F,"《說文》「東方色也，木生火，从生丹」：青為木生之色，引申青綠、年輕。","q「亲缺」取「亲」：生色相亲。"),
("牲","shēng",F,"从牛生聲：祭祀所用牛羊豕，取所生之畜。","sh取失收：畜收而牲。"),
("性","xìng",F,"从心生聲：生之質曰性（《說文》「人之陽氣性善者也」）。","x取续消：生而相續。"),
("姓","xìng",F,"从女生聲：人所生也，因生以賜姓。","x取续消：血脈相續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取生部「草木出土、所生」一面：晶取其光，牛取其畜，心取其質，女取其脈。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcr-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第497部生部（卷八十一 釘）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡497a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡497a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡497a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
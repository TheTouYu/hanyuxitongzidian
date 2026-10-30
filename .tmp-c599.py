import json,subprocess,os,glob
F="【483 龖部】龖＝从龍之二疊，龍本指閃電，二疊表極致，象強烈的電閃雷鳴（震，龖之赫，霆之砉）；音源借音，因亮如彗星而義音同「習」（古龖、習、聶可通）。部內从龖諸字取「重疊、震懾」二面。"
N="字形：古文字字形库未收。"
D=[("龖","dá",F,"本部部首字：二龍→電閃雷鳴之極。","d「囤动」取「囤」：雷動而囤。"),
("襲","xí",F,"从衣龖省聲：衣上加衣為重衣，引申因襲、襲擊、沿襲。","x「续消」取「续」：衣重相續。"),
("慴","shè",F,"从心習聲：恐惧、慑服（同「懾」）。","sh「失收」取「失」：心失而慴。"),
("懾","shè",F,"从心聶聲：恐惧、威懾，取雷震之懾人。","sh取失：威震而失。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取龖部「電光重疊、震懾人心」两面：衣取其重，心取其懼。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lck-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第483部龖部（卷七十九 彗）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡483a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡483a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡483a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
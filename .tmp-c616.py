import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【511 心部】心＝象心臟形（甲骨文作心房心室之狀），本義心臟；轉義心思、感情、中心、核心。部內从心諸字皆以心為義符，聲符給具體情狀。"
N="字形：古文字字形库未收。"
D=[("心","xīn",F,"本部部首字：心臟→心思、感情、中心。","x「续消」取「续」：血脈續於心。"),
("慶","qìng",F,"从心从夂从鹿省：以鹿皮為贄而行賀（《說文》「行賀人也」），本義慶賀、福。","q「亲缺」取「亲」：親而相慶。"),
("應","yìng",F,"从心䧹聲：本義應當（《說文》「當也」），引申應對、感應。","y「柔锐」取「柔」：應而柔順。"),
("沁","qìn",F,"从水心聲：水名（沁水）；又滲入（「沁人心脾」）。","q取亲缺：水滲而親。"),
("芯","xīn",F,"从艸心聲：草名；又燈芯、物之中心。","x取续消：草心續長。"),
("訫","xìn",F,"从言心聲：「信」之異體，取心之誠。","x取续消：言續而信。"),
("孞","xìn",F,"从子心聲：「信」之古文異體。","x取续消：子續而信。"),
("吢","qìn",F,"从口心聲：「吣」之本字，貓犬嘔吐。","q取亲缺：口吐而親。"),
("杺","xīn",F,"从木心聲：木名；又車闌。","x取续消：木心續直。"),
("伈","xǐn",F,"从人心聲：「伈伈」，恐懼貌。","x取续消：心續而懼。"),
("鈊","xīn",F,"从金心聲：金名，取心之聲。","x取续消：金續而堅。"),
("応","yìng",F,"从心雁聲：「應」之異體（日本略字）。","y取柔锐：應而柔。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同以心為義符：水取其滲，艸取其芯，言取其誠。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"ldb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
      "boundary":"源自《系統漢語》第511部心部（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡511a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡511a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡511a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "n:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
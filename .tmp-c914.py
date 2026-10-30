import sys,json,subprocess,os,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F="【第597部「用部」】用＝象蟲蛹形，「蛹」之初文（《說文》「繭蟲也」）；蛹是幼蟲化成蟲的過渡形態、工具性存在，用畢即棄，故引申施行、使用、處理、能力、資財、器物、花費、憑藉、租借；部內「甬」指中空之蛹→中空通道。"
D=[("用","yòng",F,"象蟲蛹形：蛹之初文（《說文》「繭蟲也」）；引申施行、使用、器物、憑藉、花費。","y「噎」無部；取零聲母「以」之引：用引而出。"),
("甬","yǒng",F,"中空之甬：甬道、鐘柄；本取蛹之中空，與「同」義音可通。","y取零聲母：中空而引。"),
("桶","tǒng",F,"从木甬聲：木桶（《說文》「木方受六升」），中空之器。","t「涂突」取「涂」：木中空而突。"),
("筩","tǒng",F,"从竹甬聲：竹筒，斷竹之中空者。","t取涂突：竹中空而突。"),
("俑","yǒng",F,"从人甬聲：木偶人（《說文》「痛也」一曰偶人），殉葬之偶。","y取零聲母：象人而引。"),
("通","tōng",F,"从辵甬聲：達也（《說文》「達也」），中空故通。","t取涂突：道通而突。"),
("痛","tòng",F,"从疒甬聲：病也（《說文》「病也」），痛楚。","t取涂突：痛而突。"),
("涌","yǒng",F,"从水甬聲：水往上冒（《說文》「滕也」），洶湧。","y取零聲母：水涌而引。"),
("勇","yǒng",F,"从力甬聲：气也（《說文》「气也」），勇力；甬之中空故有力。","y取零聲母：力涌而引。"),
("誦","sòng",F,"从言甬聲：諷也（《說文》「諷也」），朗讀背誦。","s「失收」取「收」：聲續而收。"),
("蛹","yǒng",F,"从虫甬聲：繭蟲也（《說文》「繭蟲也」），昆蟲過渡之形。","y取零聲母：蟲化而引。"),
("踊","yǒng",F,"从足甬聲：跳也（《說文》「跳也」），踴躍。","y取零聲母：足跳而引。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"用部同取「中空、可容、可通」一面：用蛹器、甬中空、桶木空、筩竹空、俑象人、通達、痛楚、涌上、勇力、誦聲、蛹化、踊跳；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":597,"name":"用"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lyong1-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第597部「用部」（卷九十八 銿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 597用部首12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡597a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡597a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡597a.json"); print(git("commit","-m","knowledge: 597用部首12条")[-60:])
import json,subprocess,os,glob
F="【434－435部】番支余字取「繁生」一面；甹（pīng）＝从丂（脖颈）从西（鸟窝），象鸟在巢边伸长脖子自在鸣叫，「聘」之初文。"
N="字形：古文字字形库未收。"
D=[("嬏","fān",F,"《集韵》「女字」——女子人名用字。","f「附分」取「分」：借声记名。"),
("𥢌","fán",F,"《集韵》「稻名」——稻之一种。","f取分：穗分而实。"),
("𢐲","fán",F,"《玉篇》「养生也」；《集韵》「生育也」——生育蕃衍。","f取分：生而分。"),
("䮳","fán",F,"《正字通》「生养蕃也，经传通作蕃」——马蕃息。","f取分：马群而分。"),
("㢖","pān",F,"《玉篇》「峙屋也」——积储之屋；又储物。","p「拼辟」取「辟」：储而分。"),
("娉","pìn",F,"《说文》「问也，从女甹声」——媒人问名、邀约婚嫁；娉婷美貌。","p取辟：问名而分。"),
("聘","pìn",F,"《说文》「访也，从耳甹声」——访问、聘问。","p取辟：访而分。"),
("𠷓","xīn",F,"《说文》「声也，从只甹声，读若声」——语气助词。","x「续消」取「消」：声出而消。"),
("梬","yǐng",F,"《说文》「枣也，似柿」——黑枣，柿树砧木。","y「柔锐」取「柔」：果小而柔。"),
("䛣","pīng",F,"《集韵》「言也」；又「䛣譠，不决」——言语不决。","p取辟：言分而疑。"),
("俜","pīng",F,"《说文》「使也，从人甹声」——放任、任侠。","p取辟：放而分。"),
("𢖊","pīng",F,"《说文》「使也，从彳䛣声」——使令、放任而行。","p取辟：行而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「翻生／鸟鸣放任」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第434－435部（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡435a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡435a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡435a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
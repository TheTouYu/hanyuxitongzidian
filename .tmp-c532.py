import json,subprocess,os,glob
F="【437 八部】八（bā）＝象物分开成两半、相背之形，《说文》「别也，象分别相背之形」；转义数字八、借「贝」之分二。"
N="字形：古文字字形库未收。"
D=[("𩡩","bā",F,"《说文》「马八岁也，从马从八」——八岁马。","b「闭剥」取「剥」：马分而壮。"),
("𣎵","pō",F,"《说文》「草木盛𣎵𣎵然，象形，八声」——枝叶茂盛、因风舒散之貌。","p「拼辟」取「辟」：叶分而盛。"),
("𠔯","bān",F,"《说文》「赋事也，从菐从八，八亦声」——分配工作。","b取剥：事分而派。"),
("汃","bīn",F,"《说文》「西极之水也，从水八声」——西极之水；又波相激声。","b取剥：水激而分。"),
("𠔁","bié",F,"《说文》「分也，从重八，八亦声」——分开；古文别字。","b取剥：分背而别。"),
("扒","bā",F,"《集韵》「破也、击也」——扒开；又拔也、救也（通拜）。","b取剥：手分而破。"),
("朳","bā",F,"《玉篇》「无齿杷也」——扫除用的无齿耙。","b取剥：扫而分。"),
("仈","bā",F,"《字汇》「姓也」——姓氏用字。","b取剥：借声记姓。"),
("釟","bā",F,"《玉篇》「治金也」——冶炼金属。","b取剥：金分而治。"),
("玐","bā",F,"《集韵》「玉声」；又玉名。","b取剥：玉击而分。"),
("趴","pā",F,"肚子向下卧倒；身体前靠——指爪覆伏紧贴之状，取意类「扒」。","p取辟：伏而分。"),
("𪗔","pà",F,"《广韵》「齿声」——牙齿相击声。","p取辟：齿分而声。"),
("𥐙","pā",F,"《广韵》「石破声」；又玉声。","p取辟：石破而分。"),
("叭","pā",F,"《集韵》「声也」；《字汇》「口开貌」；又军号（号筒）。","p取辟：口开而声。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取八部「分开相背」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbf-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第437部「八部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡437a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡437a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡437a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
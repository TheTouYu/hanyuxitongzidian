import json,subprocess,os,glob
F="【437 八部·分部】分＝从刀八声，剖开；诸字取「分散、香气、水石、数量」诸面。"
F8="【438 半部】半（bàn）＝从牛八声，象宰杀牲体而分剖（判之初文）；转义物中分、大片。"
N="字形：古文字字形库未收。"
D=[("訜","fēn",F,"《集韵》「訜𧥼，语不定」——言语含糊不决。","f「附分」取「分」：言分而疑。"),
("玢","bīn",F,"《广韵》「文采状也」——玉的纹理；又玻璃纸（赛璐玢）。","b「闭剥」取「剥」：理分而文。"),
("昐","fēn",F,"《玉篇》「日光」——日光照耀。","f取分：光分而照。"),
("砏","bīn",F,"《广韵》「水名，又石」；砏磤，大雷、石声。","b取剥：石分而声。"),
("炃","fén",F,"《集韵》「焚，火灼物也，或作燓、炃、燌」——焚烧。","f取分：火分而焚。"),
("馚","fēn",F,"《集韵》「馩馧，香也」——香气。","f取分：香分而馩。"),
("弅","fèn",F,"《集韵》「隐弅，丘高起貌」——高丘之状。","f取分：丘分而高。"),
("秎","fèn",F,"《广韵》「穧秎，获也」——收割，禾束。","f取分：禾分而束。"),
("葐","pén",F,"《集韵》「蒛葐，草名」；葐蒕，盛貌。","p「拼辟」取「辟」：草分而盛。"),
("湓","pén",F,"水名在浔阳；一曰水溢，形如盆。","p取辟：水溢而分。"),
("酚","fēn",F,"有机化合物，羟基直接连于芳香环（苯环）者——酚类。","f取分：性分而析。"),
("半","bàn",F8,"从牛八声，宰杀牲体而分剖（判之初文）；《说文》「物中分也，从八从牛，牛为物大，可以分也」。","b取剥：牛分而半。"),
("伴","bàn",F8,"《说文》「大貌，从人半声」；又伴侣、依随。","b取剥：伴分而随。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「分散／分剖」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbj-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第437－438部（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡438a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡438a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡438a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
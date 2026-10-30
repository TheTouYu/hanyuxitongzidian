import json,subprocess,os,glob
F="【426 皆部】皆＝二虎直立相抗而齐；威猛一支取「虎威→强壮、硬实」，器物各随其质：铁、石、鞋、车皆须坚牢。"
N="字形：古文字字形库未收。"
D=[("偕","xié","《说文》「强也」——《诗》「偕偕士子」，强壮；一曰俱也，共同。","j「聚决」取「聚」：众力相聚而强。"),
("鍇","kǎi","《说文》「九江谓铁曰锴」——好铁、白铁；《方言》「坚也」。","j取聚：铁聚而坚。"),
("瑎","xié","《说文》「黑石似玉者」——黑玉、黑石。","j取聚：石聚而黑。"),
("䃈","jiē","《玉篇》「山名」，《集韵》「石名」；一说同瑎，黑石似玉。","j取聚：石聚为名。"),
("揩","kāi","《玉篇》「摩拭也」，《广雅》「磨也」——揩擦；又敔（止乐之器）。","j取聚：手聚而摩。"),
("䡡","xié","《字汇》「登车」——登车。","j取聚：登车相聚。"),
("𩋧","xié","《玉篇》「履也」——鞋；又鼓名，通作揩。","j取聚：皮聚为履。"),
("媘","jiē","《集韵》「女字」——女子名用字。","j取聚：借声记名。"),
("煯","jiē","《字汇补》「煏也」——用火烘干。","j取聚：火聚而烘干。"),
("𩘅","jiē","《玉篇》「疾风也」——急风。","j取聚：风聚而疾。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取皆部「相抗而齐、相聚而坚」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"jb2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第426部「皆部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡426b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡426b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡426b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
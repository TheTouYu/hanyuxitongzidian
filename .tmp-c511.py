import json,subprocess,os,glob
F="【427 聿部】聿＝手持半竹；律支取「竹管」之形与用：古以竹管定音（律吕），故律从聿——管有长短、音有高下，均布而成法度。"
N="字形：古文字字形库未收。"
D=[("侓","lù","《集韵》「侓魁，大貌」——魁伟高大。","l「拢离」取「离」：形大而舒展。"),
("垏","lǜ","《集韵》「埂埒也」——田埂、堤埒。","l取离：田界分明。"),
("律","lǜ","《说文》「均布也，从彳聿声」——普遍施行的条例；本指竹管定音之器，《集韵》「阳管谓之律」，十二律管长短定音高。","l取离：管别音高、一一分布。"),
("峍","lù","《集韵》「峍矻，山崖也」——山崖高耸。","l取离：崖立而离。"),
("㡽","zhào","《字汇》「言说卑也」；《正字通》疑讹字，据形当同肇，指门杠。","l取离：借形记物。"),
("嵂","lǜ","《集韵》「崒嵂，山高貌」——山势高峻。","l取离：峰高而离。"),
("箻","lǜ","《集韵》「竹管，以射鸟」——竹筒吹箭。","l取离：竹管射物使离。"),
("葎","lǜ","《说文》「艸也」——葎草，茎有细刺，善勒人肤，故名勒草，讹为葎。","l取离：刺牵人衣而离。"),
("䮇","yù","《集韵》「驪马白跨也」——股间白色的黑马。","y「柔锐」取「锐」：白处尖露。"),
("𧊐","lǜ","《集韵》「虫名」——疑指钻木虫。","l取离：虫钻木而离。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取聿部「竹管」一面——管有长短、物有高下，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
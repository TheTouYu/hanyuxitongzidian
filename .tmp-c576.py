import json,subprocess,os,glob
F="【463 又部】又＝象手腕以下的指掌，本义为手（《说文》「手也。象形。三指者，手之列多略不過三也」）；音源搓手声；转为重复、继续之虚词（《广韵》「又，猶更也」）；字族衍义「指动如手」。"
N="字形：古文字字形库已收「又」部头字形，本卡从略。"
D=[("又","yòu",F,"本部部首字，象手形，作偏旁或写作「扌」，表手所从事的动作；本义分化为左、右、手。","y「柔锐」取「柔」：手柔而转。"),
("𤴨","yòu",F,"从疒又声——手抖之疾（帕金森），头亦摇，《玉篇》「頭搖也」。","y取柔：颤而柔。"),
("右","yòu",F,"本同「又」，指右手；金文加口为增饰或象以手助食；转为助、保、尚右、右侧、西方。","y取柔：右手柔便。"),
("祐","yòu",F,"从示右声——神助、保佑；《方言》又训「治」。","y取柔：神助而柔。"),
("佑","yòu",F,"《广韵》「佐也、助也」——辅佐、帮助、庇护。","y取柔：佐助而柔。"),
("宥","yòu",F,"从宀有声——《说文》「寬也」，宽仁、宽待；《类篇》「空也」。","y取柔：宽而柔。"),
("友","yǒu",F,"又之二迭（迭体字），会意手牵手或加倍呵护；引申平等亲密，《说文》「同志為友」。","y取柔：携手而柔。"),
("伖","tǎng",F,"与「帑」同——金币所藏；又通「孥」，指儿女。","t「涂突」取「涂」：藏而涂。"),
("苃","yǒu",F,"草名；据音义当是「茇」之俗、「犮」之讹——形近致误之例。","y取柔：草柔而讹。"),
("有","yǒu",F,"从肉从又，手持肉——或指掌状之肾，或指持肉；转为获取、拥有、赠送、零头、椭圆、青紫。","y取柔：持肉而柔。"),
("䵋","wěi",F,"从黄有声——《说文》「靑黃色也」，青黄色（手掌肉色之引申）。","w「蒙末」取「末」：色暗而末。"),
("珛","xiù",F,"从玉有声——有瑕疵的玉，《说文》「朽玉也」。","x「续消」取「消」：玉朽而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取又部「手之动作、持物」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbz-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第463部又部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡463a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡463a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡463a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
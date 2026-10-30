import json,subprocess,os,glob
F="【463 又部·余支】又部诸字皆取「手之灵动、持物、动作」为义：為＝从象又声，象鼻如人手而灵活；灰＝手所拨之火烬；㝊＝以手守持；手＝又之分化。"
N="字形：古文字字形库未收。"
D=[("為","wéi",F,"从象又声——「又」在象鼻处，象鼻灵活如人手，故引申做、作、充当、代替、伪装。","w「蒙末」取「末」：鼻动而末。"),
("偽","wěi",F,"从人为声——《说文》「詐也」，假装、虚假；「为」之比拟义所生。","w取末：人为而末。"),
("譌","é",F,"从言为声——《说文》「譌言也」，无中生有之言；或作訛。","e零声母：讹言随口。"),
("撝","huī",F,"从手为声——《说文》「裂也」，一曰手指、指挥、挥动。","h「豁活」取「活」：手挥而活。"),
("媯","guī",F,"从女为声——虞舜居妫汭因以为氏；又《方言》「媯媞，慢也」。","g「隔估」取「估」：氏号相承。"),
("鄬","guī",F,"从邑为声——春秋郑地，在今河南鲁山境；亦作「䧦」。","g取估：地名相承。"),
("灰","huī",F,"从手从火——手拨火后之余烬；引申灰色、消沉。","h取活：火灭而活。"),
("恢","huī",F,"从心灰声——《说文》「大也」，广大、恢复。","h取活：心大而活。"),
("盔","kuī",F,"从皿灰声——头盔，覆首如皿；本作「鍐」「盔」。","k「口控」取「控」：覆首而控。"),
("詼","huī",F,"从言灰声——《广韵》「詼諧，調戲也」，诙谐调笑。","h取活：言谐而活。"),
("守","shǒu",F,"从宀从又（寸）——以手守持官署；引申守候、操守。","sh「失收」取「收」：持而收。"),
("狩","shòu",F,"从犬守声——《说文》「犬田也」，冬猎曰狩；甲骨文从犬从干（猎具）。","sh取收：猎而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同为又部之动，形符各定落点：人或言则取诈伪，火与皿则取烬与覆；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lby-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第463部又部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡463b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡463b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡463b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
p=r"D:\系统汉字\memory\CURRENT.md"
t=open(p,encoding="utf-8").read()
if "D:\\字谱智能体" not in t:
    open(p,"w",encoding="utf-8").write(t.rstrip()+"\n- 2026-10-23 原稿 docx 已迁至 `D:\\字谱智能体`（旧 `D:\\修订\\x` 失效）；扫稿、抽图、查部头一律用新路径。\n")
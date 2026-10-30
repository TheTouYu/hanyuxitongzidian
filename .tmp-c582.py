import json,subprocess,os,glob
F="【465 就部】就＝甲骨金文从亯（祭坛）从京（高屋），象高高的祭坛；战国古文加「尤」表特别高；转为靠近、迁就、成就、只、仅；音源借音（特出义同尤，蹙缩义同戚）。"
N="字形：古文字字形库未收。"
D=[("就","jiù",F,"本部部首字：高坛→靠近、迁就、成就、只仅；《说文》「高也」。","j「聚决」取「聚」：高聚而就。"),
("㠇","jiù",F,"从山就声——《广韵》「嶺名」，山岭之名。","j取聚：岭聚而就。"),
("𪆩","jiù",F,"从鳥就声——即「鷲」，秃鹫，头颈裸出，争食时面色变红。","j取聚：鹫聚而就。"),
("僦","jiù",F,"从人就声——《说文》新附「賃也」，租赁。","j取聚：赁聚而就。"),
("蹴","cù",F,"从足就声——《说文》「躡也」，踢、踏；《集韵》「蹴然，敬皃」。","c「亲缺」取「亲」：踏而亲。"),
("噈","cù",F,"从口就声——《广韵》「歍噈，口相就也」，口相就。","c取亲：口就而亲。"),
("𥳛","cù",F,"从竹就声——笡也，竹器相抵。","c取亲：竹抵而亲。"),
("憱","cù",F,"从心就声——与「蹙」同，忧愁蹙眉。","c取亲：心蹙而亲。"),
("㩆","jiù",F,"从手就声——《集韵》「攬也」，又读 zú，「極擊也」。","j取聚：手聚而就。"),
("𦠢","jiù",F,"从肉就声——《漢典》「下痕」，肌痕。","j取聚：痕聚而就。"),
("𧫾","jiù",F,"从言就声——《集韵》「諛也」，谄媚、靠近献殷勤。","j取聚：言聚而就。"),
("𧑙","zú",F,"从虫就声——《唐韵》「蝍𧑙，尺蠖也」，尺蠖爬行头尾相就。","z「凿总」取「总」：虫聚而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取就部「高、靠近、蹙缩」三面，形符各定落点：人与言主就而近，足口手主迫，鳥虫主名物。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbt-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第465部就部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡465a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡465a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡465a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
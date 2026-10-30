import json,subprocess,os,glob
F="【427 聿部·肅】肅＝持篙撑船渡深水旋流；本义疾速，转义严峻、谨慎恭敬。字族两支：①撑篙→细长深长（木长、竹管、长股）②撑船→浮行泛飞。"
N="字形：古文字字形库未收。"
D=[("橚","sù","《说文》「长木貌」——长木；《集韵》「橚矗，行木貌」；qiū 通楸。","s「失收」取「收」：长木收立。"),
("㩋","sù","《集韵》「击也」；《广韵》「击声」「打也」，xiāo「把也」。","s取收：击而收拢。"),
("彇","xiāo","《集韵》「弓弭头也」——弓末弯曲处，绷弦之意。","x「续消」取「消」：弦张力消于此。"),
("繡","xiù","《说文》「五采备也」——刺绣；《释名》「修也，文修修然」；指刺绣时小心刺针之状。","x取消：彩线消入布。"),
("瀟","xiāo","《水经注》「潇者，水清深也」——潇水，湘江上游；又潇潇风雨暴疾。","x取消：水深而清。"),
("潚","sù","《说文》「深清也」——水深且清；sōu 同溲，淘米。","x取消：澄而清。"),
("𩙚","xiāo","《玉篇》「北风也」；《集韵》「凉风谓之𩙚」。","x取消：风过而消。"),
("𩘹","sù","《广韵》「风声」；《广雅》「风也」，寒风。","s取收：风声收聚。"),
("嘯","xiào","《说文》「吹声也」——蹙口出声，长啸；又叱喝。","x取消：声长而消。"),
("歗","xiào","《说文》「吟也」——《诗》「其歗也歌」；蹙口出声。","x取消：吟声散消。"),
("熽","xiào","《玉篇》「火炽也」——火盛。","x取消：火盛将消。"),
("鷫","sù","《说文》「鹔鷞也，五方神鸟」——西方神鸟，色青。","s取收：神鸟收羽。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取肃部「篙入深流」的细长、清深、疾速一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427f2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427f.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427f.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
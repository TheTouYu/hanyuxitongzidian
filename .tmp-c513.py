import json,subprocess,os,glob
FH="【427 聿部·晝】晝＝从日从聿，聿指手持竹竿，象竖竿测量日影以计时，表示白天；《说文》「日之出入，与夜为界」；本部不具表音性，未成字族。"
FS="【427 聿部·肅】肅＝从𣶒从聿，𣶒指深水旋流、聿指持篙，象持篙撑船渡水；「橚」之初文。转义：渡险须速→严峻峻急；战战兢兢→谨慎恭敬；又引申引进、飞。音源：本聿声，因有搜寻义而义音同「叜」。"
N="字形：古文字字形库未收。"
D=[("𢴩","bì",FH,"《广韵》引《方言》「刺也」，亦作㧙——以手刺入。","b「闭剥」取「剥」：手刺而剥。"),
("潷","bì",FH,"《玉篇》「笮去汁也」，《博雅》「𥂖也」——滤出液体、去渣。","b取剥：渣剥而汁出。"),
("㻶","bǐ",FH,"《玉篇》「青白玉琯也」——青白玉制的管。","b取剥：玉琢成管。"),
("𠽩","bì",FH,"《集韵》「鸣也」——鸣叫之声。","b取剥：声剥而出。"),
("晝","zhòu",FH,"从日从聿，竖竿测日影以计时——白天；与夜为界。","zh「凿总」取「凿」：凿影而知时。"),
("𣻱","zhòu",FH,"《字汇补》「水名」——《水经注》「俗以𣻱水为宿留水」。","zh取凿：借声记水。"),
("肅","sù",FS,"从𣶒从聿，持篙撑船渡深水旋流；严峻、谨慎、恭敬引进、飞。","s「失收」取「收」：篙收而渡。"),
("蕭","xiāo",FS,"《说文》「艾蒿也」——艾蒿；艾灸为古代治病要法。","x「续消」取「消」：艾烟消散。"),
("簫","xiāo",FS,"《说文》「参差管乐，象凤之翼」——长短不齐的排箫。","x取消：众管声消长。"),
("䐹","sōu",FS,"《说文》「干鱼尾䐹䐹也」——干鱼；又肉羹、炒碎肉。","s取收：鱼干而收。"),
("蟰","xiāo",FS,"《说文》「蟰蛸，长股者」——长脚小蜘蛛。","x取消：细足虚消。"),
("鱐","sū",FS,"《集韵》「鱼腊」——干鱼。","s取收：鱼收而干。")]
for ch,p,F,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「持竿」一面（竿测影为昼、竿撑船为肃），形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
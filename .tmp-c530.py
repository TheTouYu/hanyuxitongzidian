import json,subprocess,os,glob
F="【436 𠬜部】樊＝棥（林木交叉如篱）＋𠬜（双手分拨），本义马负过重止而不前；字族取「篱障、攀引、分拨」诸面。"
N="字形：古文字字形库未收。"
D=[("𧀭","fán",F,"《集韵》「草名」——草之一种。","f「附分」取「分」：草分而蔓。"),
("𩧅","fán",F,"《玉篇》「𩧅𩡸，止也」；《集韵》「马踌躇不行」——马止而不前。","f取分：马止而分。"),
("𨟄","fán",F,"《说文》「京兆杜陵乡，从邑樊声」——汉樊哙封地。","f取分：地名借声。"),
("𧢜","fán",F,"《说文》「䚔𧢜也，从见樊声」；《集韵》「暂见」——匆匆一见。","f取分：见而分。"),
("𥌞","shuò",F,"《龙龛》「美目貌」，俗字，正作䁻——目暂视。","sh「失收」取「收」：目收而视。"),
("䫶","fán",F,"《说文》「大丑貌，从页樊声」——十分丑陋，疑指秃顶而周围有发如樊篱。","f取分：发分而丑。"),
("𩎑","zuān",F,"《说文》「车衡三束也」——曲辕用皮带捆缚于衡。","z「凿总」取「总」：束而总之。"),
("鑻","pàn",F,"《字汇》「腰带鑻面」——腰带上的铁扣；器系也。","p「拼辟」取「辟」：扣而分。"),
("襻","pàn",F,"《类篇》「衣系曰襻」——衣带、衣扣。","p取辟：系而分。"),
("攀","pān",F,"《玉篇》「援引也」——抓住别的东西向上爬；拉拢。","p取辟：抓分而上。"),
("礬","fán",F,"《集韵》「矾石」——涅石，染羽用，青白矾。","f取分：石分而涩。"),
("蠜","fán",F,"《说文》「阜螽也」——蚱蜢，能跳过樊篱。","f取分：跃而分。"),
("燓","fén",F,"《说文》「烧田也，从火棥」——有计划分片焚烧山林以田猎。","f取分：分片而焚。"),
("爨","cuàn",F,"《说文》「齐谓之炊爨」——烧火煮饭；烟气升腾环绕。","c「刺持」取「刺」：火刺而炊。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取樊部「篱障／攀引／分拨」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbd-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第436部「𠬜部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡436b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡436b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡436b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
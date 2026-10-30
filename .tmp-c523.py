import json,subprocess,os,glob
F432="【432 隶部】隶＝从又抓动物尾巴，追及之初文；字族取「附著、追及、尾随之状」。"
F433="【433 肆部】肆＝从金从隶（隶亦声），本指编钟一虡二十六枚之「銉」（《周礼》「全为銉」），引申穷极、陈列、恣意。"
N="字形：古文字字形库未收。"
D=[("棣","dì",F432,"《说文》「白棣也，从木隶声」——棣棠，花黄色；萼片花瓣彼此相附，故从隶。","d「囤动」取「动」：花附而微动。"),
("殔","yì",F432,"《说文》「瘗也，从歺隶声」——临时浅埋在路旁的假葬。","y「柔锐」取「柔」：浅埋而柔。"),
("埭","dài",F432,"《正韵》「以土堰水也」——堵水的土坝，船过以绠系舟尾挽之。","d取动：挽舟而前。"),
("靆","dài",F432,"《玉篇》「不明貌」；《集韵》「叆叇，云盛貌」——云相堆积。","d取囤：云囤积。"),
("曃","dài",F432,"《广韵》「暖曃，不明貌」——昏暗。","d取囤：光囤而暗。"),
("肆","sì",F433,"春秋金文从金从隶，隶亦声；本指编钟一堵二十六枚（全为銉），引申穷极、陈列、恣意、放肆。","s「失收」取「收」：列而收束。"),
("𢘶","tuì",F433,"《玉篇》「肆也、忘也、忽也」——放肆无拘、遗忘、舒缓、惆怅。","t「涂突」取「突」：放纵而突。"),
("蕼","sì",F433,"《说文》「赤蕼也」——赤色草；《字汇补》与肆同，宽舒貌。","s取收：草柔而收。"),
("𩬶","sì",F433,"《玉篇》「与肆同」；《篇海》「毫毛也」——长毛兽。","s取收：毛长而收。"),
("𤝽","sì",F433,"《集韵》「本作𧳙」；《尔雅》「貄，修毫」——幼小的野猫。","s取收：小兽团缩。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「附著／陈列」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第432－433部（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡432b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡432b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡432b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
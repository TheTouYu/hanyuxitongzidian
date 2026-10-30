import json,subprocess,os,glob
F="【439 㡀部】㡀＝破布狭小，敝之初文；诸字取「击打使破、遮蔽覆掩、憋住」诸面。"
N="字形：古文字字形库未收。"
D=[("潎","pì",F,"《说文》「于水中击絮也，从水敝声」——水中漂击丝絮；又清也。","p「拼辟」取「辟」：水击而分。"),
("蹩","bié",F,"《说文》「踶也，一曰跛也」——踢、跛；蹩𨇨，旋行之貌。","b「闭剥」取「剥」：足踢而分。"),
("撇","piē",F,"《说文》「别也，一曰击也，从手敝声」——用手分开、抽打；又撇捺。","p取辟：手撇而分。"),
("蔽","bì",F,"《说文》「蔽蔽，小艸也」——遮蔽、掩覆、障隐。","b取剥：草掩而分。"),
("幣","bì",F,"《说文》「帛也」——束帛为礼，泛指车马皮帛玉器；今货币。","b取剥：帛裂而分。"),
("瞥","piē",F,"《说文》「过目也，又目翳也」——眼光掠过；一瞥。","p取辟：目掠而分。"),
("獘","bì",F,"《说文》「顿仆也，从犬敝声」——如磕头般前倒，憋气而死。","b取剥：仆地而分。"),
("鄨","bì",F,"《说文》「䍧牱县，从邑敝声」——古县名，今贵州遵义西。","b取剥：地名借声。"),
("龞","biē",F,"《说文》「甲虫也」——鳖；取义于「憋」，外壳封闭而缩头缩脚。","b取剥：壳闭而分。"),
("鐅","piě",F,"《说文》「河内谓锸头金也」——锹类刃口；又煮盐浅锅。","p取辟：刃分而削。"),
("弊","bì",F,"《玉篇》俗「𡚁」字——倒毙、仆倒；困、恶；又作弊。","b取剥：败而分。"),
("蟞","bié",F,"《集韵》「蟞蜉，虫名，蚁也」——大蚂蚁；又鱼鳖俗字。","b取剥：虫分而群。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取㡀部「击破／遮蔽」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbn-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第439部「㡀部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡439b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡439b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡439b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
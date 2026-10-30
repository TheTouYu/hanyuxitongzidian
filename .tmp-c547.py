import json,subprocess,os,glob
F="【441 豩部】豩（huān/bīn）＝从豕二叠、三叠，象意野猪成群追逐争斗、顽劣；二叠亦可表小，小野猪毛色条纹→斑驳（豳）。辯證：《说文》「二豕也」无实义，叠体表特性/数量之极致。音源：借音，义音同「分」。"
F2="【441 㣈支】㣈（sì）＝从㣇二叠，象意祭祀陈列全牲（㣇象野猪张口），与「肆」通；亦表小猪、猪叫。"
F3="【442 斌部】斌（bīn）＝从文从武，象意文武兼备，本作份、彬。音源：借音，义音同「分」。"
N="字形：古文字字形库未收。"
D=[("豩","bīn",F,"《同文備考》「豕亂群」；《康典》引《漢皋詩話》「豩，頑也」——野猪成群、顽劣。","b「闭剥」取「剥」：群豕分逐。"),
("燹","xiǎn",F,"《说文》「火也」；《玉篇》「野火也」；《正字通》「兵火曰燹」——野火、兵燹。","x「续消」取「消」：火延而消。"),
("𩰟","fēn",F,"《说文》「鬥連結𩰝紛相牽也」——争斗不断、纷乱。","f「附分」取「附」：斗而相牵。"),
("𧱾","guāi",F,"《字學三正》「犬逐也」；《正字通》疑「燹」之譌——犬逐。","g「隔估」取「隔」：逐而分。"),
("𧲟","kūn",F,"《搜眞玉鏡》「與昆蟲之昆同」——借为昆。","k「口控」取「控」：群聚而控。"),
("豳","bīn",F,"《说文》「美陽亭，卽豳也，从山从豩」——古地名，今陕西彬县；又通斒，色驳。","b取剥：山地分处。"),
("𧱶","fèn",F,"《字彙補》「古文鳳字」——形近「朋」而讹。","f取附：借形而分。"),
("㣈","sì",F2,"《说文》「㣇屬，从二㣇」；《虞書》「㣈類于上帝」——陈列全牲以祭，通「肆」。","s「失收」取「失」：陈列而放。"),
("斌","bīn",F3,"《玉篇》「文質皃，亦作份、彬」——文武兼备。","b取剥：文质分而备。"),
("贇","yūn",F3,"《玉篇》「美也」——美好；又人名。","y「柔锐」取「锐」：美而锐。"),
("𣁦","pán",F3,"《字彙補》「音槃，義闕」，应即文武全才之义。","p「拼辟」取「辟」：全才而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「群豕／全牲／文武」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第441－442部（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡441a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡441a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡441a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
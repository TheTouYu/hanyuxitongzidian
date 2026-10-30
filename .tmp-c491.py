import json,subprocess,os,glob
B="【419 犮部】犮与亥同源，金文象直立的旱獭正面形、足加一丿表示抬起前肢；转义：直立→挺拔抽引（拔）、往前扑（跋）、毛皮细软面小宜作蔽膝（袚/韍/帗）、掘根致沙化→旱灾（魃）、毛发（髮）、腿肉（胈）。音源：源自旱獭叫声。"
N="字形：古文字字形库未收。"
D=[("茇","bá","《说文》「草根也」——春草根枯，引之而发土为拨；又草之白华为茇、荜茇（柴门草舍）。","b「闭剥」取「剥」：根剥土而拔。"),
("髮","fà","《说文》「根也」；《释名》「髮，拔也，拔擢而出也」——头发。","f「附分」取「分」：发分覆首。"),
("胈","bá","《正字通》「肤毳皮，又股上小毛」；《集韵》「白肉也」。","b「闭剥」取「剥」：毛附肉如剥。"),
("鼥","bá","《集韵》「鼠肥者」——旱獭本名；皮可为裘，甚暖、湿不能透。","b「闭剥」取「剥」：皮剥而为裘。"),
("袚","bò","《说文》「蛮夷衣，一曰蔽膝」——系在衣前的大巾，如今围兜。","b「闭剥」取「剥」：皮剥而为蔽。"),
("帗","bō","《说文》「一幅巾也」——帛幅二尺四寸；又乐舞所执。","b「闭剥」取「剥」：帛剥而幅。"),
("韍","fú","《说文》「巿，韠也——上古衣蔽前而已，巿以象之」；天子朱巿、诸侯赤巿。","f「附分」取「分」：蔽前而分。"),
("黻","fú","《说文》「黑与青相次文」——礼服上黑青相间的花纹，其色正如蒙古旱獭。","f「附分」取「分」：色分而成文。"),
("𢇷","bá","《说文》「舍也」——屋舍；《玉篇》「草舍也，今作茇」。","b「闭剥」取「剥」：草剥而舍。"),
("鈸","bó","《玉篇》「铃也」——铜钹，南齐穆士素所造，相击以和乐。","b「闭剥」取「剥」：铜剥而鸣。"),
("盋","bō","《新附》「盋器，盂属」——即钵，食器。","b「闭剥」取「剥」：器剥而盛。"),
("瞂","fá","《说文》「盾也」——盾牌。","f「附分」取「分」：盾分而蔽。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取犮部「旱獭皮毛／蔽膝」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第419部「犮部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡419c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡419c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡419c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
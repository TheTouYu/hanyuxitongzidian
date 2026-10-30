import json,subprocess,os,glob
F="【424 癹部】癹＝从癶从攴，象拄杖而立、双脚轮换踩踏，指中耕除草（《说文》「以足蹋夷艸」）；也指用棍挑拨或掷棒，此义分化作「發」——發初文不从癹，甲骨文以一点表箭出弦颤。转义：发射→离去、派遣、生发、启动、发布。音源：借音字，义音同「犮」。字族：①除草割草 ②划动分拨 ③发射张起。"
N="字形：古文字字形库未收。"
D=[("橃","fá","《说文》「海中大船」——同「筏」。","f「附分」取「分」：木分而浮。"),
("癈","fèi","《说文》「固病也」——顽固不治之病、残疾；又废弃。","f「附分」取「分」：病分而废。"),
("廢","fèi","《说文》「屋顿也」——房屋由立而突然垮下；引申退、灭、止。","f「附分」取「分」：屋分而顿。"),
("鱍","bō","《集韵》「鱼游貌」；《广韵》「鱼掉尾也」。","b「闭剥」取「剥」：尾剥而游。"),
("蹳","bō","《集韵》「足跋物」——用脚拨开、踢。","b「闭剥」取「剥」：足剥而踢。"),
("潑","pō","《玉篇》「水漏也」；《集韵》「弃水也」——液体倒掉使散开，引申胡乱蛮横。","p「拼辟」取「辟」：水辟而散。"),
("𠷑","pō","《玉篇》「妄说也」——胡说。","p「拼辟」取「辟」：言辟而妄。"),
("墢","fá","《集韵》「垡，耕起土也」——耕地翻起的土块。","f「附分」取「分」：土分而翻。"),
("發","fā","《说文》「射发也」——箭离弦；引申明、进、行、驾车。","f「附分」取「分」：弦分而箭出。"),
("襏","bó","《广韵》「襏襫，蓑，雨衣也」。","b「闭剥」取「剥」：皮剥而蔽雨。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取癹部「以足拨草——分拨／发射」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第424部「癹部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡424b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡424b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡424b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
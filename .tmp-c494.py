import json,subprocess,os,glob
B420="【420 戒部】戒＝甲骨文双手持戈，象意武装防范；转义警戒→谨慎准备、警告→告诉命令、界限。音源：借音字，义音同「亥」，古戒、亥可通。字族衍义：①戒备→束缚约止 ②警告→警示凶暴 ③形近「夭」之讹。"
B421="【421 革部】革＝甲骨文象被剖剥下来摊开的整张兽皮，头、身、尾仍相连（《广韵》「兽皮也」）。转义：皮欲用须去毛并鞣制，故引申指去毛（《玉篇》「去毛也」）；进而引申为更改、改换、除掉；去毛用火燎或开水烫后刮，故引申指急。音源：源自刮毛之声。"
N="字形：古文字字形库未收。"
D=[("𡯰","gà","《汉典》「尴𡯰，同尴尬」——行不正。","g「隔估」取「隔」：行隔而尴。"),
("𢂵","jiè","《玉篇》「㠹，帻也」——头巾。","j「聚决」取「聚」：巾聚而裹。"),
("𢧧","gé","《玉篇》「病也」；𢧧𡭂，草生也。","g「隔估」取「隔」：病隔于身。"),
("𢬿","xiè","《集韵》「持也」。","x「续消」取「续」：手持而续。"),
("㳦","xiè","《集韵》「水名」。","x「续消」取「消」：水流而消。"),
("𧇑","bào","《集韵》「虣，强侵也，《周官》有司虣」——强横侵夺，通作暴。","b「闭剥」取「剥」：强剥而侵。"),
("𡲁","chū","《广韵》「履属」——鞋类。","ch「刺持」取「刺」：足刺于履。"),
("革","gé","本部部首字——剖剥摊开之整张兽皮；去毛为革。","g「隔估」取「隔」：皮隔而覆。")]
for ch,p,xp,sm in D:
    b=B420 if len(ch)==1 and ch in "𡯰𢂵𢧧𢬿㳦𧇑𡲁" else B421
    sec=[{"key":"bengen","label":"字根本义","text":b,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「束止／皮去毛改易」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":("源自《系統漢語》第420部「戒部」（卷七十 亥）；字卡五步规程。" if ch!="革" else "源自《系統漢語》第421部「革部」（卷七十 亥）；字卡五步规程。"),"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡420b421a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡420b421a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡420b421a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
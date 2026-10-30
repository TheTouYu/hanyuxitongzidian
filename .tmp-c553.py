import json,subprocess,os,glob
F="【445 串部】串＝象串珠形（《正字通》「物相連貫也」），引申穿、亲近、积习；字族多表连续、成串、环绕。"
N="字形：古文字字形库未收。"
D=[("串","chuàn",F,"象串珠形，泛指物之连成串；引申穿过、串通、亲近，亦指贯串与积习。","ch「刺持」取「持」：珠串而持。"),
("患","huàn",F,"《说文》「憂也，从心上貫串，串亦聲」——串珠悬心，忧患之状。","h「豁活」取「活」：忧而难活。"),
("槵","huàn",F,"《集韻》「木名」——《本草》无患子（槵子），子可浣垢，核可作念珠。","h取活：木实而活。"),
("漶","huàn",F,"《集韻》「漫漶，不可分别」——水浸纸而字迹模糊。","h取活：水散而活。"),
("瞣","huàn",F,"《集韻》「目病」——眼病视乱，与漫漶同类。","h取活：目乱而活。"),
("䍺","huàn",F,"《集韻》「羊名」——羊名，或指细角羊。","h取活：羊角而活。"),
("𤡟","huàn",F,"《集韻》「獸名」——兽名。","h取活：兽逐而活。"),
("𨫑","huàn",F,"《集韻》「金銀銅鐵璞」——同「鋛」，未冶之矿。","h取活：矿结而活。"),
("鋛","kuàng",F,"《字彙》「古猛切，音礦：金銀銅鐵璞也」——未经冶炼的矿石。","k「口控」取「控」：矿坚而控。"),
("𠁷","chǎn",F,"同「丳」，炙肉具——烤肉串的签子，正中一签、左右各一签。","ch「刺持」取「刺」：签入肉中。"),
("𢈢","lǒu",F,"《篇韻》「草室也」——以草串编而成的草屋。","l「拢离」取「拢」：草聚而拢。"),
("贃","wàn",F,"《集韻》「鋌也」——金属坯；《正字通》「餘財」——余财。","w「勿问」取「问」：财蓄而问。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取串部「连贯／穿过／环绕」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbw-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第445部「串部」（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡4452026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡445.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡445.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
import json,subprocess,os,glob
BZ=("【407 足部】部首足（𠯁𤴕zú）：甲骨文象人的整条腿形（大腿、脚、掌、趾），后腿脚部分写作「口」形（《说文》「人之足也，在下，从止口」）。"
    "轉義：足起支撑基础→器物的脚、植物根茎、事物基础；足小而承重→足够满足增益；两足等长并拢→等齐、迫促。音源：足踏声。"
    "字族衍义：①两足距离→迫促急促 ②两足长度→齐整相等 ③足的大小→小 ④与足相关的行为。")
N="字形：古文字字形库未收。"
D=[
("䎌","cù",BZ,N,"《广韵》「飛皃」；《集韵》「羽齊皃」；《類篇》「羽高皃」——羽齐、羽高之貌。","等齐族②之羽：以「羽」定其形，两翼等长。","c「刺持」取「持」：羽持而齐。"),
("珿","chù",BZ,N,"《玉篇》「等也，齊也」——等同、齐整。","等齐族②之玉：以「玉」定其质，玉等则齐。","ch「刺持」取「持」：持齐不偏。"),
("䇍","chù",BZ,N,"《集韵》「音珿，齊謹也」；《篇海》「等也」——齐而谨。","等齐族②之竹：以「竹」定其物，竹节齐整。","ch「刺持」取「持」：节持而谨。"),
("𡷿","zhuó",BZ,N,"《篇海類編》「音捉，山名」——山名。","等齐族②之山：以「山」定其处，山形齐峙。","zh「凿总」取「总」：群峰总立。"),
("𧯩","chù",BZ,N,"《广韵》「小豆也」——小豆。","小族③之豆：以「豆」定其类，荚小而圆。","ch「刺持」取「持」：豆持于荚。"),
("𥒭","chù",BZ,N,"《集韵》「音矗，小石」——小石。","小族③之石：以「石」定其质，石小如粒。","ch「刺持」取「持」：石持于地。"),
("𪕝","cù",BZ,N,"《集韵》「𪕝鼩，小鼠」——小鼠。","小族③之鼠：以「鼠」定其类，鼠小善窜。","c「刺持」取「刺」：窜刺而疾。"),
("𥷼","cù",BZ,N,"《玉篇》「笡，逆槍也」——掌子（竹签、竹刺）。","行为族④之竹：以「竹」定其物，逆刺之手。","c「刺持」取「刺」：竹刺而入。"),
("莡","cuò",BZ,N,"《玉篇》「行草聲」；《集韵》「草名」——行于草的声音。","行为族④之草：以「艸」定其境，践草有声。","c「刺持」取「刺」：足刺草响。"),
("浞","zhuó",BZ,N,"《说文》「濡也，从水足聲」；《广韵》「水濕」——沾湿。","行为族④之水：以「水」定其状，足涉而湿。","zh「凿总」取「凿」：水凿而濡。"),
("踀","cù",BZ,N,"《龍龕》「絆足也」；《集韵》「齊謹也，或作踀、䇍」——绊足、谨小慎微。","行为族④之足：以「足」定其动，足被绊而谨。","c「刺持」取「刺」：绊刺而止。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,Nx,a,b,c in D:
    json.dump(card(ch,p,Bx,Nx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"䎌":"《集韵》「羽齊皃」；《類篇》「羽高皃」。","珿":"《玉篇》「等也，齊也」。","䇍":"《集韵》「齊謹也」；《篇海》「等也」。","𡷿":"《篇海類編》「山名」。","𧯩":"《广韵》「小豆也」。","𥒭":"《集韵》「小石」。","𪕝":"《集韵》「𪕝鼩，小鼠」。","𥷼":"《玉篇》「笡，逆槍也」——掌子。","莡":"《玉篇》「行草聲」；《集韵》「草名」。","浞":"《说文》「濡也，从水足聲」——沾湿。","踀":"《龍龕》「絆足也」；《集韵》「齊謹也」。"}
def B(ch): return "源自《系統漢語》第407部「足部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bde-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡407足部二2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡407足部二.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡407足部二.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
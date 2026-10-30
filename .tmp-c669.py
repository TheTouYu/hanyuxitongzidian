import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FD="【第527部「向部」】向＝从宀从口（屋与窗），本義窗；轉義窗所朝→方向、相向；音源借音（向陽有光）。字族分向系／尚系／堂系／當系／黨系／掌系六組。"
N="字形：古文字字形库未收。"
D=[("𥤗","dǎng",FD,"《集韻》「頓𥤗，黃穀名」。","d「囤动」取「囤」：穀聚而囤。"),
("𥸈","dǎng",FD,"《集韻》「竹名」；《正字通》「與欓同，盛物之器」。","d取囤动：竹器而囤。"),
("𩽳","dǎng",FD,"𩽳魟魚，背厚長有足；又名钂魚，尾上有刺如欓樹刺。","d取囤动：魚厚而囤。"),
("𪇁","dāng",FD,"《字彙補》音當，鳥名。","d取囤动：借聲為名。"),
("㿩","tǎng",FD,"《玉篇》「明也」，或作曭；白色。","t「涂突」取「涂」：色白而突。"),
("𣎲","tǎng",FD,"《廣韻》「月不明也」。","t取涂突：月暗而突。"),
("𥳶","zhǎng",FD,"《集韻》音掌，竹名。","zh「凿总」取「总」：竹聚而總。"),
("𩞦","chēng",FD,"《字彙》「飽也」。","ch「刺持」取「持」：食飽而持。"),
("𢿦","chéng",FD,"《集韻》引《說文》「橦也」——撞、觸。","ch取刺持：擊撞而持。"),
("礃","zhǎng",FD,"礃子（掌子），採礦或隧道掘進的工作面。","zh取凿总：石面而總。"),
("𣾦","zhǎng",FD,"《搜眞玉鏡》音掌，水名。","zh取凿总：水聚而總。"),
("𦺡","zhǎng",FD,"《正字通》虎掌、射干、仙人掌諸草，葉如人掌。","zh取凿总：草掌而總。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"向部末諸字，皆取本部各組（向／尚／堂／當／黨／掌）之聲，形符各定落點；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiangz-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527i2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527i.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527i.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
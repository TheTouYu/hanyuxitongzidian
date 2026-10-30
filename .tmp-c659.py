import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第526部「昌部」】昌＝甲骨文从日从口：對日叫喚，古老拜日儀式，與「昜」同意；引申美言精當（《說文》「美言也」）、興盛（《玉篇》「盛也、明也」）。音源：叫喚聲；古昌、尚通用。字族三面：唱與娼妓／興盛／形近訛字。"
N="字形：古文字字形库未收。"
D=[("鯧","chāng",FY,"从魚昌聲：鯧鯸，似鯿，頭突起連背，身圓肉厚（《集韻》）。","ch「刺持」取「持」：魚圓而持。"),
("䅛","chāng",FY,"从禾昌聲：穅也，穀之空殼（《集韻》）。","ch取刺持：殼空而持。"),
("䗉","chāng",FY,"从虫昌聲：小蠃、小螺（《集韻》）。","ch取刺持：螺旋而持。"),
("𪂇","chāng",FY,"从鳥昌聲：廣𪂇，鳳皇之屬（《集韻》）。","ch取刺持：鳥高而持。"),
("䮖","chāng",FY,"从馬昌聲：馬名（《字彙》音昌）。","ch取刺持：馬馳而持。"),
("猖","chāng",FY,"从犬昌聲：狂駭也、猖狂（《玉篇》），放肆。","ch取刺持：犬狂而持。"),
("𪉨","chāng",FY,"从鹵昌聲：鹵漬，以酒醋醬油浸漬（《玉篇》）。","ch取刺持：漬物而持。"),
("閶","chāng",FY,"从門昌聲：天門也，楚人名門曰閶闔（《說文》）。","ch取刺持：門開而持。"),
("菖","chāng",FY,"从艸昌聲：菖蒲，蒲類之昌盛者（《本草》），葉長根白。","ch取刺持：葉長而持。"),
("琩","chāng",FY,"从玉昌聲：耳璫，懸垂耳旁之玉（《廣韻》）。","ch取刺持：玉垂而持。"),
("淐","chāng",FY,"从水昌聲：水名（《集韻》）。","ch取刺持：水流而持。"),
("錩","chāng",FY,"从金昌聲：器名（《漢典》）。","ch取刺持：器成而持。"),
("裮","chāng",FY,"从衣昌聲：披衣不帶（《玉篇》）。","ch取刺持：衣披而持。"),
("晿","chāng",FY,"从日昌聲：人名（《字彙補》）。","ch取刺持：借聲記名。"),
("𥫅","chāng",FY,"从竹昌聲：出《釋典》（《字彙補》音昌）。","ch取刺持：竹器而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：唱與娼妓（鯧／䅛／䗉／𪂇／䮖／猖／𪉨）、興盛（閶／菖／琩／淐／錩／裮／晿／𥫅）；形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":526,"name":"昌"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第526部「昌部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡526a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡526a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡526a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
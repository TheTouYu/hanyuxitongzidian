import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FW="【第517部「王部」·王支】王＝甲骨文象闊刃短柄的玉斧，代表無上權力，引申首領、君主；轉義大、盛；辯證《說文》「三畫連中」不確；音源借「黃」。字族多以「㞷」為聲，指歸往，表急、多、亂。"
FQ="【第517部「王部」·皇支】皇＝从日有光芒从丨（十），象太陽光猛烈，為「煌」之初文；轉義天、君、美、盛大；辯證小篆訛从自，《說文》析形不確。"
N="字形：古文字字形库未收。"
D=[("王","wáng",FW,"本部字根：玉斧之形，引申君主、大盛。","w「无为」？取「往」一面：斧刃往而無阻。"),
("皇","huáng",FQ,"本部二級字根：日光猛烈，引申天、君、美。","h「豁活」取「豁」：光豁然而大。"),
("往","wǎng",FW,"从彳㞷聲：之也、去也（《說文》），引申歸嚮。","w取往：往而歸。"),
("汪","wāng",FW,"从水㞷聲：深廣（《說文》），池水所歸往會聚。","w取往：水往而聚。"),
("枉","wǎng",FW,"从木㞷聲：樹木斜曲（《說文》），引申冤抑、曲法。","w取往：木往而曲。"),
("旺","wàng",FW,"从日往聲：光明旺盛（《說文》「光美也」），俗作旺。","w取往：日照而旺。"),
("狂","kuáng",FW,"从犬㞷聲：瘋狗（《說文》「狾犬也」），引申狂放、迷惑。","k「口控」取「控」：犬狂難控。"),
("誑","kuáng",FW,"从言狂聲：欺騙（《說文》「欺也」）。","k取口控：言誑而控。"),
("煌","huáng",FQ,"从火皇聲：光輝（《說文》「煌，輝也」）。","h取豁活：火豁而煌。"),
("篁","huáng",FQ,"从竹皇聲：竹田（《說文》），竹園。","h取豁活：竹密而豁。"),
("惶","huáng",FQ,"从心皇聲：恐懼（《說文》「恐也」）——蝗災起而人心惶惶。","h取豁活：心恐而豁。"),
("徨","huáng",FQ,"从彳皇聲：彷徨往來、心神不安。","h取豁活：行而徬徨。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分二面：王支取「歸往／急多亂」（往／汪／枉／旺／狂／誑）、皇支取「日光盛大／乾旱色黃／蝗災恐慌」（皇／煌／篁／惶／徨）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":517,"name":"王"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lwang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第517部「王部」（卷八十五 匚）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡517a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡517a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡517a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
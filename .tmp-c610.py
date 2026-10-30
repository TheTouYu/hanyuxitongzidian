import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【503 曾部】曾＝甑之初文，象蒸器（箅上有汽）之形；借為「曾經」，轉義重疊（曾祖）、乃。部內从曾諸字取「增加、重疊」兩面。"
G="【504 亙部】亙＝从二从月（一說回旋之形），本義迴環、終竟（《說文》「竟也」）；轉義延續、普遍。部內从亙諸字取「迴環、延續」一面。"
C="【505 从部】从＝从二人相隨，本義跟隨（《說文》「相聽也」）；轉義順從、參與、自。部內从从諸字取「相隨、聚」兩面。"
N="字形：古文字字形库未收。"
D=[("曾","zēng",F,"本部部首字：蒸器→曾經、重疊、曾祖。","z「凿总」取「凿」：汽凿而上。"),
("增","zēng",F,"从土曾聲：加多曰增，取曾之重疊義。","z取凿：土鑿而累。"),
("憎","zēng",F,"从心曾聲：厭惡（《說文》「惡也」）。","z取凿：心鑿而拒。"),
("贈","zèng",F,"从貝曾聲：以物送人（《說文》「玩好相送也」）。","z取凿：貝鑿而遺。"),
("層","céng",F,"从尸曾聲：重屋曰層，取曾之重疊。","c「刺持」取「持」：重積而持。"),
("僧","sēng",F,"从人曾聲：梵語「僧伽」之省，眾比丘。","s「失收」取「收」：眾收而和。"),
("亙","gèn",G,"本部部首字：迴環終竟→延續、普遍。","g「隔估」取「隔」：環隔而不絕。"),
("恆","héng",G,"从心亙聲：常也、久也（《說文》「常也」）。","h「豁活」取「豁」：心豁而恒。"),
("垣","yuán",G,"从土亙聲：牆也（《說文》「牆也」），取亙之環繞。","y「柔锐」取「柔」：土柔而成垣。"),
("宣","xuān",G,"从宀亙聲：天子居曰宣室，引申宣布、疏通。","x「续消」取「续」：氣續而宣。"),
("从","cóng",C,"本部部首字：二人相隨→跟隨、順從、自。","c取刺持：隨而相持。"),
("從","cóng",C,"从辵从聲：隨行（《說文》「隨行也」），从之加辵。","c取刺持：步隨而持。"),
("叢","cóng",C,"从丵取聲：草木聚生曰叢，取从之聚義。","c取刺持：聚而相持。"),
("縱","zòng",C,"从糸從聲：緩也、放也（《說文》「緩也」）。","z取凿：絲鑿而放。"),
("蹤","zōng",C,"从足從聲：足跡（「蹤跡」），取從之隨行。","z取凿：足鑿留跡。")]
cl=[]
for i,(ch,p,F0,xp,sm) in enumerate(D,1):
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"曾部取「重疊增加」，亙部取「迴環延續」，从部取「相隨而聚」；形符各定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    cl.append({"id":f"lcv-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
      "boundary":"源自《系統漢語》第503－505部（卷八十二 工）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡505a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡505a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡505a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
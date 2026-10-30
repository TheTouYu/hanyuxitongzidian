import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FB="【第535部「襄部」】襄＝甲骨文象人头顶器皿之形（双手上举扶物），《說文》「解衣耕」析形不确；轉義上舉昂起→扶助成就→駕車→除去→捲袖肥大。音源借音（相助之義音同「相」，「襄羊」＝「相羊」）。"
FZ="【第534部「爿部」·葬系】葬＝从死在茻中（草莽间），《說文》「藏也」；字族多承「葬、髒」之義。"
N="字形：古文字字形库未收。"
D=[("髒","zāng",FZ,"从骨葬聲：骨間之肉；今通「脏」，不淨。","z「凿总」取「凿」：骨實而凿。"),
("𩦦","zāng",FZ,"从馬葬聲：《集韻》馬名。","z取凿总：馬健而凿。"),
("𠿺","guài",FZ,"《集韻》「聲也」，疑譌字。","g「隔估」取「估」：聲隔而估。"),
("襄","xiāng",FB,"象人头顶皿、双手上举扶物；引申上舉、扶助、駕車、除去、肥大。","x「续消」取「续」：舉而續。"),
("驤","xiāng",FB,"从馬襄聲：馬之低卬也（《說文》），馬騰躍昂首；後右足白亦曰驤。","x取续消：馬昂而續。"),
("纕","xiāng",FB,"从糸襄聲：《說文》「援臂也」，佩帶、束袖之繩。","x取续消：臂帶而續。"),
("饟","xiǎng",FB,"从食襄聲：饋也（《說文》），送飯與人；同「餉」。","x取续消：饋食而續。"),
("蠰","xiāng",FB,"从虫襄聲：《爾雅》「蠰，齧桑」，蟲名。","x取续消：蟲續而消。"),
("攘","rǎng",FB,"从手襄聲：推也（《說文》），捋袖出臂、排斥、侵奪。","r「柔锐」取「锐」：推而锐。"),
("禳","ráng",FB,"从示襄聲：磔禳，祀除殃也（《說文》），祭以去災。","r取柔锐：祭除而锐。"),
("嚷","rǎng",FB,"从口襄聲：吆喝、喧鬧。","r取柔锐：聲銳而揚。"),
("獽","ráng",FB,"从犬襄聲：《集韻》獸名，似犬。","r取柔锐：獸銳而逐。")]
for ch,p,F0,xp,sm in D:
    bn=534 if ch in "髒𩦦𠿺" else 535
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"襄系同取「上舉、扶助」一面：襄言頂皿、驤言馬昂、纕言臂帶、攘言推袖、禳言祭除；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"爿" if bn==534 else "襄"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第534－535部（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡535a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡535a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡535a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
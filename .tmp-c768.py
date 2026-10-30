import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第563部「臸部」】臸＝从至之二疊：至指箭射到，二疊表極致、多，象萬箭齊至或插滿箭矢；引申到達、目標一致、前往、插。"
N="字形：古文字字形库未收。"
D=[("臸","zhī",FH,"从二至：到也（《說文》「到也。从二至」），箭紛至；引申一致、前往、插。","zh「凿总」取「凿」：箭至而凿。"),
("晉","jìn",FH,"从日从臸：進也，日出萬物進（《說文》「進也」），象日光四射如萬箭；引申按抑、插進。","j「聚决」取「聚」：日聚而决。"),
("榗","jiàn",FH,"从木晉聲：木也（《說文》「木也」），可作箭，箭竹。","j取聚决：木直而决。"),
("𡺽","jìn",FH,"从山晉聲：山名（《集韻》「山名」）。","j取聚决：山高而决。"),
("箭","jiàn",FH,"从竹前聲：矢也（《說文》「矢也」），竹高一丈可為矢。","j取聚决：竹直而决。"),
("𨍬","zhēn",FH,"从車秦聲：車聲（《集韻》），車行聲。","zh取凿总：車行而凿。"),
("𧎽","jìn",FH,"从虫晉聲：蛤類（《集韻》「蛤類」），似蛤而扁有毛。","j取聚决：蛤聚而决。"),
("戩","jiǎn",FH,"从戈晉聲：滅也（《說文》「滅也」），戩穀、福祿。","j取聚决：戈擊而决。"),
("鄑","zī",FH,"从邑晉聲：地名（《說文》「地名」），鄑城。","z「凿总」取「总」：邑聚而总。"),
("溍","jìn",FH,"从水晉聲：水名（《說文》「水名」）。","j取聚决：水流而决。"),
("縉","jìn",FH,"从糸晉聲：帛赤色也（《說文》「帛赤色也」），薦紳（縉紳）。","j取聚决：絲赤而决。"),
("搢","jìn",FH,"从手晉聲：插也（《說文》「插也」），搢笏。","j取聚决：手插而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"臸系同取「箭至紛集、日出光芒」一面：晉日出、榗箭竹、𡺽山名、箭矢、𨍬車聲、𧎽蛤、戩滅、鄑邑、溍水、縉赤帛、搢插；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":563,"name":"臸"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhi2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第563部「臸部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡563a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡563a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡563a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
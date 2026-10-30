import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FC="【第537部「長部」】長＝人长发拄杖（年长／首领）；轉義久遠多、長處、增進、撫育。"
FD="【第538部「畕部」】畕＝从二田，田界相比相鄰，《說文》「比田也」；為「疆」之聲根。"
N="字形：古文字字形库未收。"
D=[("悵","chàng",FC,"从心長聲：望恨也（《說文》），失意惆悵。","ch「刺持」取「持」：心悵而持。"),
("倀","chāng",FC,"从人長聲：倀鬼（傳說為虎作倀），又狂也。","ch取刺持：人行而持。"),
("帳","zhàng",FC,"从巾長聲：帷幕、帳篷（張之分化）。","zh「凿总」取「凿」：布张而凿。"),
("賬","zhàng",FC,"从貝長聲：帳之俗字，記財物出入。","zh取凿总：贝记而凿。"),
("脹","zhàng",FC,"从肉長聲：肌膚鼓脹（張之分化）。","zh取凿总：肉张而凿。"),
("腸","cháng",FC,"从肉長聲：腸道，迂長如帶。","ch取刺持：腸长而持。"),
("漲","zhǎng",FC,"从水長聲：水漲（張之分化）。","zh取凿总：水张而凿。"),
("萇","cháng",FC,"从艸長聲：萇楚，即羊桃（《說文》）。","ch取刺持：草长而持。"),
("鼚","chāng",FC,"从鼓長聲：鼓聲（《說文》「鼓聲也」）。","ch取刺持：鼓振而持。"),
("瓺","chàng",FC,"从瓦長聲：瓶也（《說文》）。","ch取刺持：瓦瓶而持。"),
("粻","zhāng",FC,"从米長聲：糧米（《說文》「食米也」）。","zh取凿总：米实而凿。"),
("畕","jiāng",FD,"从二田：比田也（《說文》），田界相邻，疆之初文。","j「聚决」取「聚」：田聚而决。")]
for ch,p,F0,xp,sm in D:
    bn=537 if ch!="畕" else 538
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"長系同取「引而長、張而鼓」一面（帳幕、脹肉、漲水、腸道、粻米）；畕言田界相鄰；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"長" if bn==537 else "畕"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第537－538部（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡538a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡538a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡538a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
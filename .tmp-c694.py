import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FB="【第535部「襄部」】襄＝人头顶皿、双手上举扶物；轉義上舉→扶助→駕車→除去→捲袖肥大→嵌藏。"
N="字形：古文字字形库未收。"
D=[("讓","ràng",FB,"从言襄聲：責讓（《說文》「相責讓」），引申推辭、謙讓。","r「柔锐」取「锐」：言锐而责。"),
("鑲","xiāng",FB,"从金襄聲：《說文》「作型中腸也」，鑄器內模；引申鑲嵌。","x「续消」取「续」：嵌而續。"),
("壤","rǎng",FB,"从土襄聲：柔土也（《說文》）；引申土地、疆域。","r取柔锐：土柔而锐。"),
("孃","niáng",FB,"从女襄聲：少女之稱，又母親（孃／娘）。","n「纳弄」取「纳」：女而纳。"),
("瀼","ráng",FB,"从水襄聲：《說文》「露濃貌」；水流貌。","r取柔锐：水盛而锐。"),
("曩","nǎng",FB,"从日襄聲：曩，向也（《說文》），從前、昔日。","n取纳弄：日前而纳。"),
("釀","niàng",FB,"从酉襄聲：釀酒，以穀麥發酵成酒。","n取纳弄：酒纳而弄。"),
("忀","xiāng",FB,"从彳襄聲：忀徉，徘徊不進。","x取续消：行續而消。"),
("勷","ráng",FB,"从力襄聲：劻勷，急促不安貌。","r取柔锐：力锐而促。"),
("瓤","ráng",FB,"从瓜襄聲：瓜內之肉（瓜瓤）。","r取柔锐：瓜内而锐。"),
("鬤","ráng",FB,"从髟襄聲：毛髮雜亂貌。","r取柔锐：髮乱而锐。"),
("爙","rǎng",FB,"从火襄聲：火貌（《集韻》）。","r取柔锐：火盛而锐。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"襄系同取「上舉、扶助、捲藏」一面：讓言責、鑲言嵌、壤言土、釀言酒、瓤言瓜肉；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":535,"name":"襄"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiangb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第535部「襄部」（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡535b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡535b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡535b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
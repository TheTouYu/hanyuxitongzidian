import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FG="【第531部「桑部」】桑＝甲骨文象枝葉繁茂的桑樹（《玉篇》「蠶所食葉」）；轉義桑幹結節→圓鼓堅韌之物，飼蠶→蠶之狀；音源借音義同「爽」。"
FS="【第531部「桑部」·喪系（二级字根）】喪（丧䘮）＝甲骨文从吅从桑：「吅」眾口，象群蠶食桑；眾蠶食桑如白衣人匍匐哭喪，故引申失去、死亡（《廣韻》「亡也、死喪也」）、喪事。"
FR="【第531部「桑部」·染系（二级字根）】染（𣑱）＝从水从桑，象意以桑樹汁液作染料（《本草綱目》「煮汁染褐色，久不落」；柘桑染黃赤）；轉義染色→玷污（《廣雅》「污也」）、薰陶（《正字通》「習俗積漸曰染」）。"
N="字形：古文字字形库未收。"
D=[("喪","sàng",FS,"从吅从桑：群蠶食桑，如白衣哭喪；引申失去、死亡、喪事。","s「失收」取「收」：亡而收。"),
("染","rǎn",FR,"从水从桑：以桑汁染布；引申染色、玷污、薰陶。","r「柔锐」取「柔」：染而柔。"),
("𣞙","sǎng",FG,"《廣韻》「鼓匡木也」、《玉篇》「鼓材也」。","s取失收：鼓材而收。"),
("鎟","sǎng",FG,"《集韻》「鈴聲」；或同䡦，轂中受軸之空。","s取失收：金鳴而收。"),
("𡠏","sāng",FG,"商代地名，在今河南寧陵南（《漢典》）。","s取失收：地名而收。"),
("𩺞","sǎng",FG,"黃顙魚，頭部堅硬——如桑之結節。","s取失收：魚頭而收。"),
("𣉕","sàng",FG,"《集韻》「㫰𣉕，暴熭也」，暴曬。","s取失收：日曬而收。"),
("縔","shuǎng",FG,"《集韻》「𡳭中繭」，繭中蠶絲。","sh取失收：繭絲而收。"),
("褬","sǎng",FG,"《集韻》「𧚅褬，衣敝」——衣爛如蠶吃過的桑葉。","s取失收：衣敝而收。"),
("𤸯","sǎng",FG,"《集韻》「馬病」——疑馬吐沫如蠶吐絲。","s取失收：病而收。"),
("䮣","sǎng",FG,"《集韻》「馬色黃尾白」，馬色如蠶。","s取失收：馬色而收。"),
("𨢆","sāng",FG,"《玉篇》「乳酒」。","s取失收：酒而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"桑系諧聲字分兩面：桑之結節（𣞙／鎟／𩺞／𣉕／䮣）與桑葉蠶事（縔／褬／𤸯／𨢆）；喪系取群蠶食桑如哭喪，染系取桑汁為染；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":531,"name":"桑"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lsang2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第531部桑）：{xp}",
 "boundary":"源自《系統漢語》第531部「桑部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡531d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡531d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡531d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
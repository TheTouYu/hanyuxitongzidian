import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第523部「羊部」】羊＝象有角的羊頭形，取其角為標誌符號；音源為羊叫聲。字族分取「羊毛厚多」「羊群處溫順」「羊眼小而假寐」「羊行山崖」諸面。"
N="字形：古文字字形库未收。"
D=[("羊","yáng",FY,"本部字根：角為標誌，溫順群處，引申美善。","y「圆容」取「圆」：角曲而圓。"),
("洋","yáng",FY,"从水羊聲：廣大——言羊毛多而厚；又海洋。","y取圆容：水廣而容。"),
("徉","yáng",FY,"从彳羊聲：仿徉、徘徊——羊走路較慢。","y取圆容：行緩而容。"),
("样","yàng",FY,"从木羊聲：榜樣、模樣——群羊有領頭羊，為標準。","y取圆容：模範而容。"),
("翔","xiáng",FY,"从羽羊聲：迴飛（《說文》），取羊毛飛揚之狀。","x「续消」取「续」：羽續而翔。"),
("詳","xiáng",FY,"从言羊聲：審議、詳細（《說文》「審議也」），取羊性溫順可細察。","x取续消：言審而續。"),
("恙","yàng",FY,"从心羊聲：病——羊哀聲如呻吟；又無恙。","y取圆容：病憂而容。"),
("佯","yáng",FY,"从人羊聲：假裝——羊眼小而似假寐。","y取圆容：假借而容。"),
("痒","yǎng",FY,"从疒羊聲：皮膚癢——羊毛貼膚而刺癢。","y取圆容：癢而容。"),
("祥","xiáng",FY,"从示羊聲：吉凶之兆、福善——羊為祭祀之牲。","x取续消：兆續而祥。"),
("烊","yáng",FY,"从火羊聲：熔化、炙——羊脂遇火而融。","y取圆容：火融而容。"),
("氧","yǎng",FY,"从氣羊聲：化學元素（氧氣），取羊之溫順無害。","y取圆容：氣容而續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分四面：取「羊毛厚多」（洋／徉）、取「群處有標準」（样／詳）、取「眼小假寐／哀聲」（佯／恙）、取「溫順可祭」（祥／痒／烊／氧）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":523,"name":"羊"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第523部「羊部」（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡523a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡523a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡523a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
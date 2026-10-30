import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第524部「永部」】永、𠂢本同源：从人从彳或行，象人行於道，表道路之遠。加水為「泳」，潛行水中。轉義：道路河流多分支→支、別（隸變作𠂢）。辯證：《說文》「水巠理之長」所據小篆本从水从永，析形不確；甲骨文正反無別，永、𠂢為一字。音源：本行聲，古永、羊通用。字族分二面：長久／分支分散。"
N="字形：古文字字形库未收。"
D=[("永","yǒng",FY,"从人从彳（行亦聲）：人行於道，表長遠；加水為泳。","y「圆容」取「圆」：道遠而周。"),
("詠","yǒng",FY,"从言永聲：歌吟、長言（《說文》），禽鳥鳴亦曰詠（《正字通》）。","y取圆容：聲長而周。"),
("昶","chǎng",FY,"从日从永：日長也，白天時間長（《新附》），引申通、明、舒。","ch「刺持」取「持」：日長而持。"),
("昹","ǎi",FY,"从日永聲：星名，又同昶（《金鏡》）。","零声母「上善若水」取一面：星曜而周。"),
("𨠕","yòng",FY,"从酉永聲：酗酒，同「醟」（《集韻》）。","y取圆容：醉而周。"),
("𩶙","yǒng",FY,"从魚永聲：蜀江之魚，鱗黑膚理似玉，可作鱠（《益部方物略記》）。","y取圆容：魚游而遠。"),
("𥙎","mò",FY,"从示永聲：神也（《玉篇》音陌）。","m「蒙末」取「末」：神杳而末。"),
("𥿯","pài",FY,"从糸𠂢聲：散絲、未緝之麻（《說文》）。","p「拼辟」取「拼」：絲散而拼。"),
("霢","mài",FY,"从雨脈聲：霢霂，小雨，如人沐頭僅沾上枝（《釋名》）。","m取蒙末：雨細而蒙。"),
("眽","mò",FY,"从目𠂢聲：目財視，斜眼餘光瞥視（《說文》）。","m取蒙末：目斜而末。"),
("派","pài",FY,"从水从𠂢：別水，分支水流（《說文》）；物均分亦曰派。","p取拼辟：水支而分。"),
("覛","mì",FY,"从𠂢从見：衺視，斜眼略視（《說文》），覓之籀文。","m取蒙末：視斜而末。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分二面：取「長久」（詠／昶／昹／𨠕／𩶙／𥙎）、取「分支分散」（𥿯／霢／眽／派／覛）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":524,"name":"永"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyong-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第524部「永部」（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡524yong2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡524yong.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡524yong.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
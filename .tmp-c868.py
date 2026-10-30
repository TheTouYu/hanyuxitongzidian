import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第586部「爪部」·㕚及形近之訛】㕚＝从又（手）指間有小點，象以手抓撓（小點為掉落皮屑），實「搔」之初文；《說文》「手足甲也，从又，象㕚形」所解與字形不符（小點在指間非指頭），應指爪子。部內另有形近「又、介、𠂢」之訛字組。"
N="字形：古文字字形库未收。"
D=[("㕚","zhǎo",F,"从又指間小點：象以手抓撓（《玉篇》「刮也」），搔之初文；《說文》「手足甲也」析形不確。","zh「凿总」取「总」：指聚而总。"),
("𥄗","wò",F,"从目从㕚：捾目也（《說文》「捾目也」），挖眼。","w「蒙末」取「末」：目深而末。"),
("𢯲","wàn",F,"从手𥄗聲：手𢯲也（《說文》引揚雄「𢯲，握也」），手腕。","w取蒙末：腕握而末。"),
("骱","jiè",F,"从骨介聲：䯦骱，小骨（《集韻》）；又堅也。","j「聚决」取「聚」：骨小而聚。"),
("䯰","jiè",F,"从髟介聲：簪髻（《正字通》「䯰、紒通」），束髮簪。","j取聚决：髻聚而决。"),
("齘","xiè",F,"从齒介聲：齒相切也（《說文》），咬牙；一曰怒也。","x「续消」取「消」：齒切而消。"),
("芥","jiè",F,"从艸介聲：芥本字（《正字通》），芥菜；又菜名生水中。","j取聚决：菜辛而决。"),
("衸","jiè",F,"从衣介聲：衣裾也（《玉篇》），刺膝、衣長皃。","j取聚决：衣長而决。"),
("𡰫","niǎn",F,"从尸从又：柔皮也（《說文》「从申尸之後」），使皮革柔軟（搓揉）。","n「纳弄」取「纳」：皮柔而纳。"),
("𨋚","niǎn",F,"从車㞋聲：轢也（《說文》），車輪輾壓；又軟（柔也）。","n取纳弄：車輾而纳。"),
("䁊","wò",F,"从目𥄗聲：短深目皃（《說文》），眼眶短而眼珠深陷。","w取蒙末：目深而末。"),
("𤭲","nà",F,"从瓦叉聲：牡瓦（《廣韻》），房上俯蓋之瓦。","n取纳弄：瓦覆而纳。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"㕚及訛字組同取「抓撓、形近而訛」一面：㕚抓撓、𥄗挖眼、𢯲手腕、骱小骨、䯰簪髻、齘咬牙、芥芥菜、衸衣裾、𡰫柔皮、𨋚車輾、䁊目深、𤭲牡瓦；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":586,"name":"爪"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhao4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第586部「爪部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡586d.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡586d{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
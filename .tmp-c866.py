import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第586部「爪部」·蚤支】蚤＝甲骨文从虫从又（又即爪，表抓撓），象引起人抓撓的蟲（跳蚤），《說文》「齧人跳蟲，从䖵㕚聲，㕚古爪字」；轉義 早（借為早暮字）、抓撓；字族取「跳動、蚤咬瘙癢吵醒抓撓」二面。"
N="字形：古文字字形库未收。"
D=[("蚤","zǎo",F,"从虫从又（又即爪）：齧人跳蟲（《說文》），跳蚤；借為早暮字；又抓撓。","z「凿总」取「总」：蟲小而总。"),
("搔","sāo",F,"从手蚤聲：刮也（《玉篇》），以指甲抓撓。","s「失收」取「收」：指撓而收。"),
("騷","sāo",F,"从馬蚤聲：擾也（《說文》），騷動；又《離騷》之騷（憂）。","s取失收：馬動而收。"),
("慅","cǎo",F,"从心蚤聲：動也（《說文》「一曰起也」），騷動；又憂愁。","c「刺持」取「持」：心動而持。"),
("溞","sāo",F,"从水蚤聲：溞溞，淅米聲（《集韻》），淘米聲。","s取失收：水聲而收。"),
("糔","xiǔ",F,"从米蚤聲：溲也（《說文》「糔，溲也」），以水調粉。","x「续消」取「消」：米調而消。"),
("瘙","sào",F,"从疒蚤聲：疥瘙（《玉篇》），疥瘡奇癢。","s取失收：癢聚而收。"),
("鼜","qì",F,"从壴蚤聲：夜戒守鼓也（《說文》引《禮》「夜半三通為戒晨」），夜間警戒擂鼓。","q「亲缺」取「亲」：鼓夜而亲。"),
("𠋺","sāo",F,"从人蚤聲：驕也（《說文》），驕傲；又夭也。","s取失收：人驕而收。"),
("鰠","sāo",F,"从魚蚤聲：魚似鱣（《玉篇》）。","s取失收：魚游而收。"),
("𢔳","sáo",F,"从彳蚤聲：𢔳𢔇，緩行皃（《集韻》）；又跳也。","s取失收：行緩而收。"),
("𦃐","sāo",F,"从糸蚤聲：繅之或體，繹繭為絲（繭因抽絲而跳動）。","s取失收：絲抽而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"蚤支同取「跳動、蚤咬瘙癢」一面：搔抓撓、騷擾動、慅心動、溞淅米、糔調粉、瘙疥癢、鼜夜鼓、𠋺驕、鰠魚、𢔳緩行、𦃐繅絲；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":586,"name":"爪"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzao6-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第586部「爪部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡586c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡586c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
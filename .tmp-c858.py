import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第584部「喿部」】喿＝眾口在木上鳴叫（噪之初文）；字族五面：聲音之雜／狀態之雜／色彩之雜／行為之雜／心理之雜。"
N="字形：古文字字形库未收。"
D=[("𢤁","sào",F,"从心喿聲：情性踈皃（《廣韻》），性情疏放。","s「失收」取「收」：性疏而收。"),
("㿋","sào",F,"从疒喿聲：瘙之或體，疥瘙（《廣韻》），疥瘡奇癢。","s取失收：癢聚而收。"),
("劋","jiǎo",F,"从刀喿聲：絕也（《說文》引《周書》「天用劋絕其命」），滅絕、剁碎；又狡猾。","j「聚决」取「决」：絕斷而决。"),
("㩰","jiǎo",F,"从手喿聲：剽截也（《玉篇》），摷之或體，拘擊。","j取聚决：擊斷而决。"),
("𧒮","zǎo",F,"从虫喿聲：同蚤（跳蚤），叮咬致瘙癢。","z「凿总」取「总」：蟲聚而总。"),
("趮","zào",F,"从走喿聲：疾也（《說文》）；又矢傍掉（箭飛搖擺）。","z取凿总：走疾而总。"),
("鱢","sāo",F,"从魚喿聲：鮏臭也（《說文》引《周禮》「膳膏鱢」），腥味。","s取失收：魚腥而收。"),
("懆","cǎo",F,"从心喿聲：愁不安也（《說文》引《詩》「念子懆懆」），憂愁。","c「刺持」取「持」：愁結而持。"),
("嬠","cān",F,"从女喿聲：婪也（《龍龕》），貪婪。","c取刺持：貪聚而持。"),
("矂","sào",F,"从目喿聲：眊矂，失意、煩惱（《漢典》）。","s取失收：目昏而收。"),
("髞","sāo",F,"从高喿聲：髝髞，麤急皃（《廣韻》）、高皃（《集韻》）。","s取失收：高急而收。"),
("燥","zào",F,"从火喿聲：乾也（《說文》），乾枯；焦、焦急。","z取凿总：火乾而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"喿部收尾同取「擾動、焦急、雜亂」一面：𢤁性疏、㿋疥瘙、劋絕斷、㩰拘擊、𧒮跳蚤、趮疾走、鱢魚腥、懆愁、嬠貪、矂失意、髞高急、燥乾枯；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":584,"name":"喿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzao3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第584部「喿部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡584c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡584c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
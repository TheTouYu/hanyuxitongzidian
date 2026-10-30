import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第513部「悤部」】悤＝甲骨文从心从十，十倍於常心之跳，本義心跳急速（《廣韻》「速也」）；又取心統率全身血管，引申統領聚束（分化為總）；小篆加囪為聲；音源讀作「十」，後與「蔥」混同。"
N="字形：古文字字形库未收。"
D=[("悤","cōng",F,"本部字根：心跳十倍而急，引申匆忙；又統束（總）。","c「刺持」取「持」：心跳持急。"),
("總","zǒng",F,"从糸悤聲：聚束（《說文》「聚束也」），引申總領、皆。","z「凿总」取「总」：絲總而束。"),
("聰","cōng",F,"从耳悤聲：聽而能審（《說文》「察也」），取心跳靈敏。","c取刺持：耳持而察。"),
("蔥","cōng",F,"从艸悤聲：菜也（《說文》）；其初文从中有，象氣味沖鼻，故蔥味沖鼻。","c取刺持：氣沖而刺。"),
("鏓","zǒng",F,"从金悤聲：大鑿、平木之器（《說文》「鎗鏓也」）。","z取凿总：鑿聚而穿。"),
("鏦","cōng",F,"《廣韻》「鏦，短矛也」——短矛，取蔥形之尖直。","c取刺持：矛持而刺。"),
("謥","cōng",F,"《廣韻》「𧩪詷，言急」——言語嗆人，取蔥氣沖人。","c取刺持：言刺而嗆。"),
("楤","zōng",F,"《廣韻》「尖頭擔也」——兩頭尖的禾槍，取其狀如蔥。","z取凿总：擔聚柴束。"),
("璁","cōng",F,"从玉悤聲：石之似玉者（《說文》），中空如蔥、色如蔥。","c取刺持：玉中含翠。"),
("驄","cōng",F,"从馬悤聲：馬青白雜毛（《說文》）——色如蔥之青白。","c取刺持：毛雜而青。"),
("窻","chuāng",F,"从穴悤聲：通孔（《說文》「通孔也」），即窗之初文。","ch取刺持：穴穿而通。"),
("熜","zǒng",F,"从火悤聲：麻莖束成的火炬（《說文》「然麻蒸也」），麻莖中空如蔥。","z取凿总：束麻而燃。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分五面：聚束（總／鏓）、聰敏（聰）、細長而尖（蔥／鏦／楤／謥）、青白雜色（璁／驄）、中空（窻／熜）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":513,"name":"悤"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lco-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第513部「悤部」（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡513a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡513a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡513a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第559部「戔部」】戔＝从戈之二疊：兩戈相對象戰爭殘害（《說文》「賊也。从二戈」）；疊體亦表極致，指似戈而短小的器物（錢之初文）；引申淺少、棚構。"
N="字形：古文字字形库未收。"
D=[("戔","cán",FH,"从二戈：賊也（《說文》「賊也」），兩兵相對；轉義淺少、棚構。","c「刺持」取「刺」：戈刺而持。"),
("賤","jiàn",FH,"从貝戔聲：賈少也（《說文》「賈少也」），價格低、卑下。","j「聚决」取「聚」：價少而决。"),
("箋","jiān",FH,"从竹戔聲：表識書也（《說文》「表識書也」），注釋、公文体裁。","j取聚决：竹編而决。"),
("餞","jiàn",FH,"从食戔聲：送去也（《說文》「送去也」），餞行、以酒送別。","j取聚决：食送而决。"),
("諓","jiàn",FH,"从言戔聲：善言也（《說文》「善言也」），巧言、諓諓。","j取聚决：言巧而决。"),
("俴","jiàn",FH,"从人戔聲：淺也（《說文》「淺也」），淺薄。","j取聚决：人薄而决。"),
("淺","qiǎn",FH,"从水戔聲：不深也（《說文》「不深也」），水淺、淺薄。","q「亲缺」取「缺」：水淺而缺。"),
("錢","qián",FH,"从金戔聲：銚也，古田器（《說文》「銚也，古田器」），錢之初文；貨泉。","q取亲缺：金小而缺。"),
("盞","zhǎn",FH,"从皿戔聲：小杯也，玉爵之屬（《集韻》），酒盞。","zh「凿总」取「凿」：杯小而凿。"),
("線","xiàn",FH,"从糸戔聲：縷也（《說文》「縷也」），絲線。","x「续消」取「续」：絲续而消。"),
("殘","cán",FH,"从歹戔聲：賊也（《說文》「賊也」），殘害、剩餘。","c取刺持：殘而持。"),
("踐","jiàn",FH,"从足戔聲：履也（《說文》「履也」），踐踏、實行。","j取聚决：足践而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"戔系同取「戈相擊、淺少、細小」一面：賤價少、箋表識、餞送行、諓巧言、俴淺、淺水深、錢田器、盞小杯、線縷、殘賊、踐履；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":559,"name":"戔"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcan-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第559部「戔部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡559a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡559a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡559a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
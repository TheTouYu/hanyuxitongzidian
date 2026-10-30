import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第570部「丯部」】害＝甲骨文从入从丯（入象三角形刮刀，丯象用刀割），「割」之初文；引申殺害、傷害、災禍、妨礙；《說文》「从宀从口」析形不確。"
N="字形：古文字字形库未收。"
D=[("害","hài",F,"从入（刮刀）从丯（刀割）：割之初文（《廣韻》「剥也、斷也」），引申傷、禍、妨。","h「豁活」取「豁」：割裂而豁。"),
("割","gē",F,"从刀害聲：剥也（《說文》「剥也」），斷也、裂也。","g「隔估」取「隔」：刀斷而隔。"),
("轄","xiá",F,"从車害聲：車軸端之鍵（《說文》「車聲也」一曰鍵），引申管轄、統轄。","x「续消」取「续」：軸鍵而续。"),
("鎋","xiá",F,"从金害聲：車軸頭鐵（《說文》或體），同轄。","x取续消：鐵鍵而续。"),
("搳","huá",F,"从手害聲：擘也（《集韻》），劃開、拳擊。","h取豁活：手擘而豁。"),
("犗","jiè",F,"从牛害聲：騬牛也（《說文》「騬牛也」），去勢之牛。","j「聚决」取「聚」：牛割而决。"),
("磍","xiá",F,"从石害聲：磍磍，石聲（《集韻》），石相擊。","x取续消：石擊而续。"),
("螛","xiá",F,"从蟲害聲：蟲名（《集韻》），螛螳之類。","x取续消：蟲鳴而续。"),
("豁","huō",F,"从谷害聲：通谷也（《說文》「通谷也」），開闊、豁然、裂開。","h取豁活：谷開而豁。"),
("嗐","hài",F,"从口害聲：嘆詞（《字彙》），表惋惜、懊悔。","h取豁活：嘆息而豁。"),
("瞎","xiā",F,"从目害聲：目盲（《字彙》「目盲也」），引申盲目、亂。","x取续消：目閉而续。"),
("鶷","xiá",F,"从鳥害聲：鶷𪆰，鳥名（《集韻》），似鸕鶿。","x取续消：鳥啼而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"害系同取「割裂、阻隔」一面：害割、轄鍵、鎋鐵、搳擘、犗去勢、磍石聲、螛蟲、豁谷開、嗐嘆、瞎盲、鶷鳥；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":570,"name":"丯"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lhai-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第570部「丯部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡570b.json"
for it in range(8):
    json.dump({"schema_version":1,"intent":f"字卡570b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
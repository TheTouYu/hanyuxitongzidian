import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第579部「䍜部」】䍜（罩）＝从网从隹，象以網罩鳥令不飛走（讀若到）；春秋金文加糸作「羅」（以絲罟鳥）；轉義 環繞羅列、巡查、羅綺、遭遇；音源為借音（義音同離）。字族多指張羅之狀，表示環繞。"
N="字形：古文字字形库未收。"
D=[("䍜","zhào",F,"从网从隹：覆鳥令不飛走也（《說文》），罩鳥之網籠。","zh「凿总」取「总」：罩覆而总。"),
("羅","luó",F,"从网从維：以絲罟鳥也（《說文》），羅網→羅列、羅綺、姓。","l「拢离」取「离」：網張而离。"),
("邏","luó",F,"从辵羅聲：巡也（《說文》），巡察、遮也、山色環繞。","l取拢离：巡行而离。"),
("蘿","luó",F,"从艸羅聲：莪也（《說文》），女蘿托松而生。","l取拢离：蔓附而离。"),
("罹","lí",F,"从网：心憂也（《說文新附》），遭遇（古多通離）。","l取拢离：憂纏而离。"),
("纙","luò",F,"从糸羅聲：錢緡也（《集韻》），穿錢之繩。","l取拢离：繩貫而离。"),
("儸","luó",F,"从人羅聲：健而不德（《玉篇》），僂儸＝幹練機靈。","l取拢离：人捷而离。"),
("鑼","luó",F,"从金羅聲：鈔鑼，銅器（《集韻》），銅鑼（面有圈紋）。","l取拢离：金鳴而离。"),
("攞","luó",F,"从手羅聲：裂也（《集韻》），撕裂、向上捋。","l取拢离：手裂而离。"),
("籮","luó",F,"从竹羅聲：竹器（《玉篇》），籮筐（篾編螺旋狀）。","l取拢离：器編而离。"),
("囉","luó",F,"从口羅聲：歌詞、嘍囉（《廣韻》），又句末助詞。","l取拢离：聲轉而离。"),
("𤄷","luó",F,"从水羅聲：汨𤄷，水名（《廣韻》），汨羅江（屈原沉處）。","l取拢离：水曲而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"䍜部同取「張網環繞」一面：䍜罩、羅網、邏巡、蘿蔓、罹憂、纙繩、儸幹、鑼鳴、攞裂、籮筐、囉聲、𤄷水曲；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":579,"name":"䍜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第579部「䍜部」（卷九十五 離）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡579a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡579a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
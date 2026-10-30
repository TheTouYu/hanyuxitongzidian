import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第583部「巢部」】巢＝甲骨文从木上有「西」（西本指鳥窩），象樹上有鳥窩形；《說文》「鳥在木上曰巢，在穴曰窠」；轉義 高／笙（鳥窩在樹上猶笙之有瓠）／棧道；音源借音（鷦鷯最善營巢，義音同「少」）。字族分五面：鳥巢之狀／高、抄掠／小／吵鬧／形近之訛。"
N="字形：古文字字形库未收。"
D=[("巢","cháo",F,"从木上有西（西＝鳥窩）：鳥在木上曰巢（《說文》）；轉義 高（《小爾雅》）、笙（《爾雅》「大笙謂之巢」）、棧道；音源借音同「少」。","ch「刺持」取「持」：木上而持。"),
("樔","cháo",F,"从木巢聲：澤中守艸樓（《說文》）；又罺之或體，捕魚抄網。","ch取刺持：巢木而持。"),
("繅","sāo",F,"从糸巢聲：繹繭為絲（《說文》），抽繭出絲（繭如鳥窩）。","s「失收」取「收」：繭抽而收。"),
("漅","cháo",F,"从水巢聲：湖名（《廣韻》「音剿，湖名」）。","ch取刺持：水聚而持。"),
("薻","zǎo",F,"从艸从水巢聲：水艸也（《說文》引《詩》「于以采薻」），水藻（浮出水面如巢）。","z「凿总」取「凿」：水中而生。"),
("窼","chāo",F,"从穴巢聲：鳥穴中也（《集韻》）；俗作窠（窟也、巢窠）。","ch取刺持：穴藏而持。"),
("鏁","suǒ",F,"从金巢聲：鎖之俗字（《廣韻》「鎖，鐵鎖也。俗作鏁」）。","s取失收：金鎖而收。"),
("轈","cháo",F,"从車巢聲：兵高車加巢以望敵（《說文》引《春秋傳》「楚子登轈車」），巢車。","ch取刺持：車高而持。"),
("鄛","cháo",F,"从邑巢聲：南陽棗陽鄉（《說文》），漢代鄉名。","ch取刺持：邑聚而持。"),
("罺","cháo",F,"从网巢聲：抄網（《爾雅》「罺謂之汕」），撩罟（水中撈魚）。","ch取刺持：网抄而持。"),
("摷","jiǎo",F,"从手巢聲：拘擊也（《說文》）；又取也（《廣雅》），水中撈物、抄取。","j「聚决」取「聚」：手聚而决。"),
("勦","jiǎo",F,"从力巢聲：勞也（《說文》引《春秋傳》「安用勦民」）；又輕捷、竊取抄襲。","j取聚决：力聚而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"巢部同取「鳥窩之形／高、抄掠」一面：樔艸樓、繅抽繭、漅湖、薻水藻、窼鳥穴、鏁鎖、轈巢車、鄛鄉、罺抄網、摷拘擊、勦勞；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":583,"name":"巢"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第583部「巢部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡583a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡583a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
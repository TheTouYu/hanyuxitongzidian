import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第571部「力部」·男支】男＝从田从力，象耒耕；成年男子；字族②象聲（聲小）。"
F2="【第571部「力部」·耒支】耒＝手耕曲木（同力部，象耒耜之形；小篆从木从丯，丯指刻）；字族①累陳（耕翻泥土堆積之狀）。"
F3="【第571部「力部」·耤支】耤＝甲骨文象人持耒耕作（下加𡿧表水田），引申借助、賦稅、踐踏、狼藉。"
N="字形：古文字字形库未收。"
D=[("喃","nán",F1,"从口南聲：呢喃，小聲說話（《集韻》語聲）。","n「纳弄」取「纳」：語細而纳。"),
("𡇨","nān",F1,"（囝）从囗从子：兒也（《漢典》「同囝」）。","n取纳弄：子在囗而纳。"),
("𧋱","zhān",F1,"从蟲占聲：音詀（《字彙補》），疑指蟲飛聲。","zh「凿总」取「凿」：蟲飛而凿。"),
("耒","lěi",F2,"从木从丯（丯指刻）：手耕曲木（《說文》），木製犁具，耒耜之柄。","l「拢离」取「离」：犁土而离。"),
("誄","lěi",F2,"从言耒聲：諡也（《說文》），累列行跡以作諡號（祭文）。","l取拢离：累列而离。"),
("䒹","lèi",F2,"从艸耒聲：耕多艸（《說文》），果實下垂皃。","l取拢离：草多而离。"),
("頛","lèi",F2,"从頁从耒：頭不正也（《說文》），耒，頭傾也。","l取拢离：頭傾而离。"),
("㑍","lèi",F2,"从人耒聲：俹也（《集韻》），倚靠。","l取拢离：倚靠而离。"),
("㼍","lěi",F2,"从瓜耒聲：㼍㼏，瓜名（《集韻》），一曰傷熟瓜。","l取拢离：瓜垂而离。"),
("䋘","zhuì",F2,"从糸耒聲：以繩有所縣也（《說文》縋），自上放物。","zh「凿总」取「凿」：繩垂而凿。"),
("𠱤","lěi",F2,"从口耒聲：以言相遮（《篇海類編》），言語相阻。","l取拢离：言遮而离。"),
("𥑶","lěi",F2,"从石耒聲：礧，大石皃（《集韻》）。","l取拢离：石大而离。"),
("𨀤","lèi",F2,"从足耒聲：足跌（《集韻》）。","l取拢离：足跌而离。"),
("耤","jí",F3,"从耒从昔（昔為甾之訛）：象人持耒耕作，引申借助、賦稅、踐踏、狼藉。","j「聚决」取「聚」：耒田而决。"),
("籍","jí",F3,"从竹耤聲：簿書也（《說文》），戶籍、門籍；引申登記、徵稅。","j取聚决：簿聚而决。"),
("藉","jiè",F3,"从艸耤聲：祭藉也（《說文》），祭祀陳列之墊；引申憑借、踐踏、狼藉。","j取聚决：藉墊而决。"),
("䣢","jí",F3,"从邑耤聲：蜀地也（《說文》）。","j取聚决：邑聚而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"男支象聲（喃、𡇨、𧋱）；耒支累陳（誄、䒹、頛、㑍、㼍、䋘、𠱤、𥑶、𨀤）；耤支憑藉踐踏（耤、籍、藉、䣢）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":571,"name":"力"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llei-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第571部「力部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡571c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡571c{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
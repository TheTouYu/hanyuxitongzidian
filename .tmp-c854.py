import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第584部「喿部」】喿＝从品从木，眾口在木上（象蟲鳥獸眾多在樹上鳴叫），「噪」之初文，《玉篇》「呼噪也」；轉義 雜亂（米穀雜）、焦躁急迫；音源為噪雜叫聲（義音同「小」）。字族五面：聲音之雜／狀態之雜／色彩之雜／行為之雜（擾動爬搔）／心理之雜（焦急）。"
N="字形：古文字字形库未收。"
D=[("喿","zào",F,"从品从木：蟲鳥獸眾口在樹上鳴叫（《玉篇》「呼噪也」），噪之初文；轉義 雜亂、焦躁。","z「凿总」取「总」：聲匯而总。"),
("譟","zào",F,"从言喿聲：擾也（《說文》），群呼煩擾、喧嘩。","z取凿总：言雜而总。"),
("噪","zào",F,"从口喿聲：譟之或體（《集韻》），蟲鳥鳴叫、喧噪。","z取凿总：眾口而总。"),
("幧","qiāo",F,"从巾喿聲：斂髮也（《說文》），束髮巾（幧頭）。","q「亲缺」取「亲」：髮斂而亲。"),
("𤒕","cāo",F,"从火喿聲：欲沸（《集韻》「水將沸，冒泡」）。","c「刺持」取「持」：水沸而持。"),
("僺","qiào",F,"从人喿聲：僥俏，長皃（《集韻》）。","q取亲缺：人長而亲。"),
("氉","sào",F,"从毛喿聲：毛也（《玉篇》）；毷氉，煩躁不安。","s「失收」取「收」：毛聚而收。"),
("𧴜","sāo",F,"从豸喿聲：貉𧴜胡，即絡腮鬍（《字海》）。","s取失收：毛亂而收。"),
("躁","zào",F,"从足喿聲：動也（《廣韻》），急進不安靜（《正字通》）。","z取凿总：足動而总。"),
("澡","zǎo",F,"从水喿聲：灑手也（《說文》），洗滌、整治。","z取凿总：水滌而总。"),
("操","cāo",F,"从手喿聲：把持也（《說文》），握持；又節操、操練。","c取刺持：手把而持。"),
("臊","sāo",F,"从肉喿聲：豕膏臭也（《說文》），腥臊；又臊子（細剁肉）。","s取失收：肉臭而收。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"喿部同取「雜亂、擾動」一面：譟噪喧嘩、幧斂髮、𤒕欲沸、僺長貌、氉毛亂、𧴜絡腮鬍、躁足動、澡洗滌、操把持、臊腥臭；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":584,"name":"喿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第584部「喿部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡584a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡584a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
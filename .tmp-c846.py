import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第582部「小部」·少支】少＝小之加一撇（細小之極／分出），象沙粒微小（《說文》「少，不多也」）；其字族多从少聲，取「微小、稀少、末梢、不足」諸面。"
N="字形：古文字字形库未收。"
D=[("抄","chāo",F,"从手少聲：叉取也（《集韻》），掠取、謄寫。","ch「刺持」取「持」：手取而持。"),
("炒","chǎo",F,"从火少聲：熬也（《集韻》），火乾、炒製。","ch取刺持：火熬而持。"),
("秒","miǎo",F,"从禾少聲：禾芒也（《說文》「秒，禾芒也」），引申時間單位。","m「蒙末」取「末」：禾末而末。"),
("眇","miǎo",F,"从目少聲：一目小也（《說文》「眇，一目小也」），又微小、精微。","m取蒙末：目小而末。"),
("妙","miào",F,"从女少聲：美也（《廣雅》），精微、神妙。","m取蒙末：微末而末。"),
("渺","miǎo",F,"从水眇聲：渺茫（《集韻》），水遠無際。","m取蒙末：水遠而末。"),
("杪","miǎo",F,"从木少聲：木標末也（《說文》「杪，木標末也」），樹梢。","m取蒙末：木末而末。"),
("劣","liè",F,"从力少：弱也（《說文》「劣，弱也」），少力、劣弱。","l「拢离」取「离」：力少而离。"),
("尟","xiǎn",F,"从是少：鮮少（《說文》「尟，是少也」），稀少。","x「续消」取「消」：少而消。"),
("觘","chào",F,"从角少聲：角上也（《說文》「觘，角匕也」），角上曲。","ch取刺持：角長而持。"),
("耖","chào",F,"从耒少聲：重耕田也（《集韻》），耖田。","ch取刺持：耕重而持。"),
("麨","chǎo",F,"从麥少聲：糗也（《說文》「麨，糗也」），炒米粉。","ch取刺持：麥炒而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"少支同取「微小、稀少、末梢、不足」一面：抄取、炒熬、秒芒、眇小、妙微、渺遠、杪末、劣弱、尟少、觘角、耖耕、麨糗；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":582,"name":"小"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiao4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第582部「小部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡582d.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡582d{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
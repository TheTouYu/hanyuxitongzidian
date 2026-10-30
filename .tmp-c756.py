import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第558部「先部」】先＝从「止」或「之」處於「人」頭頂，象人走在前面（《說文》「前進也。从儿之」）；引申時間次序在前，又引申眾多（爭先恐後皃）。"
N="字形：古文字字形库未收。"
D=[("先","xiān",FH,"从止在人上：前進也（《說文》「前進也」），走在前；引申時間次序在前、祖先、已死。","x「续消」取「续」：行续而先。"),
("駪","shēn",FH,"从馬先聲：馬眾多皃（《說文》「馬眾多皃」），群行疾而欲先。","sh「失收」取「收」：馬群收而先。"),
("侁","shēn",FH,"从人先聲：行皃（《說文》「行皃」），往來侁侁，眾多齊整。","sh取失收：人聚而收。"),
("詵","shēn",FH,"从言从先，先亦聲：致言也（《說文》「致言也」），詵詵眾多。","sh取失收：言聚而收。"),
("毨","xiǎn",FH,"从毛先聲：仲秋鳥獸毛盛可選取為器用（《說文》），毛更生、整理。","x取续消：毛盛而续。"),
("㭠","xiǎn",FH,"从木先聲：㭠木，子赤如大豆（《玉篇》），俗云雷鳴子；又棗木。","x取续消：木實而续。"),
("筅","xiǎn",FH,"从竹先聲：洗帚飯具（《廣韻》），竹刷帚；狼筅為兵器。","x取续消：竹刷而续。"),
("姺","shēn",FH,"从女先聲：殷諸侯為亂疑姓也（《說文》「商有姺邳」），古國名。","sh取失收：女聚而收。"),
("冼","shěng",FH,"从冫先聲：𠗌冼，寒皃（《集韻》）；又姓。","sh取失收：寒收而先。"),
("跣","xiǎn",FH,"从足先聲：足親地也（《說文》「足親地也」），赤腳貼地。","x取续消：足行而续。"),
("烍","xiǎn",FH,"从火先聲：熂也（《集韻》「熂也」），火燒雜草，蔓延迅速。","x取续消：火蔓而续。"),
("洗","xǐ",FH,"从水先聲：洒足也（《說文》「洒足也」），洗滌。","x取续消：水洗而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"先系同取「走在前、爭先致多」一面：駪馬眾、侁行、詵致言、毨毛盛、㭠木實、筅刷帚、姺國名、冼寒、跣赤足、烍燒草、洗洒足；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":558,"name":"先"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxian-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第558部「先部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡558a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡558a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡558a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
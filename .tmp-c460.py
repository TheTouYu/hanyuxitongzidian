import json,subprocess,os,glob
BS="【409 蚩部（原属它部，从虫从止）】蚩＝甲骨文从虫从止：虫指蛇，止指足、行走。侧重在虫，则象蛇爬行（读 chǎn，《玉篇》「蟲伸行」）；侧重在行，则象行走时碰到蛇、受阻不能前行，此义繁化作「舝（辖）」（《释名》「辖，害也，车之禁害也」，即刹车装置），转义悖乱、可笑、轻侮。辯證：战国古文变化较大，小篆分作「𧈪、蚩、舝」三字，《说文》分别释之（蚩「虫也，从虫之声」）已非初形。音源：本「止」声，因蛇行蜿蜒而义音或同「延」。字族衍义：①蛇行→刮擦、迟缓 ③蛇貌→丑陋、痴呆、可笑。"
N="字形：古文字字形库未收。"
D=[
("𢾫","zhǐ","《说文》「剌也，从攴蚩聲」——刮擦。","蛇行族①之攴：以「攴」定其动，蛇行如刮。","zh「凿总」取「凿」：刮而凿之。"),
("滍","zhì","《说文》「水，出南陽魯陽堯山，東北入汝」——沙河，汝水支流。","蛇行族①之水：以「水」定其地，蜿蜒如蛇行。","zh「凿总」取「总」：众流总汇。"),
("䩶","chěng","《说文》「驂具也，从革𧈪聲」——骖马的马具；《集韵》「收丝器」。","蛇行族①之革：以「革」定其物，收束如蛇盘。","ch「刺持」取「持」：束持而收。"),
("𤚍","chǎn","《集韵》「牛緩謂之𤚍」——牛行迟缓。","蛇行族①之牛：以「牛」定其物，蛇行则缓。","ch「刺持」取「持」：缓持而行。"),
("𨖀","chǎn","《玉篇》「行也」，《集韵》「㢟，安步也，或作𨖀」。","蛇行族①之辵：以「辵」定其行，蛇行缓缓。","ch「刺持」取「持」：持步而缓。"),
("𩺉","hàn","《字彙》「𩹀𩹑，蚌屬」——蚌类。","蛇行族①之魚：以「魚」定其物，蚌行如蛇。","h「豁活」取「活」：水活而蚌生。"),
("䥀","chǎn","《博雅》「䥀，抒長也」——把物拉长。","蛇行族①之金：以「金」定其器，引而长之如蛇。","ch「刺持」取「持」：持而引长。"),
("𠋷","chǎn","《集韵》「人形長皃」——人形长貌。","蛇行族①之人：以「人」定其形，长如蛇。","ch「刺持」取「持」：形持而长。"),
("𩝚","chǎn","《集韵》「長味」——味长。","蛇行族①之食：以「食」定其味，长如蛇。","ch「刺持」取「持」：味持而长。"),
("䧝","chī","《集韵》地名；zhì 山名。","蛇行族①之阜：以「阜」定其地，山势蜿蜒。","ch「刺持」取「持」：地持而曲。"),
("妛","chī","《集韵》「侮也，痴也，或作媸，通作蚩」——丑陋、痴呆。","蛇貌族③之女：以「女」定其人，蛇行蠢笨则痴丑。","ch「刺持」取「持」：持而痴。"),
("嗤","chī","《玉篇》「笑皃」——讥笑。","蛇貌族③之口：以「口」定其声，蛇行可笑则嗤。","ch「刺持」取「刺」：笑如刺人。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for t in D:
    ch,p,Bx,a,c=t
    b="同取蚩部「蛇行迟缓／蛇貌可笑」一面，形符各定其落点；故声符给义、形符定落点。"
    json.dump(card(ch,p,Bx,N,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
def B(ch): return "源自《系統漢語》第409部「蚩部」（卷六十七 足）；字卡五步规程。"
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{t[0]}（字卡）",
   "statement":f"{t[0]}（{t[1]}）：{t[2]}","boundary":B(t[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,t in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡409蚩部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡409蚩部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡409蚩部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
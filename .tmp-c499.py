import json,subprocess,os,glob
P="【423 癶部】癶＝象两足相背之形，表示两脚交叉、行走不顺（《说文》「足剌癶也，读若拨」）；辨证「癶、舛」应是一字——动物正常脚印是相对的，交错便走不好；故癶、舛或指两足并立、或指两足交错。音源：借音字，义音或如「乘」（作登字声符）、或如「背」（作癹字声符）。字族：荈（老茶）、𥬫（竹贯物）、曻（昇）。"
F="【424 癹部】癹＝从癶从攴，象拄杖而立、双脚轮换踩踏之状，故脚交错成癶形；指中耕时田间除草（俗名「徕田」，《说文》「以足蹋夷艸」）。「癶」也可指棍子的移动（用棍挑拨）或手持棍棒投掷，此义后分化作「發」——發的初文本不从癹，甲骨文将弓弦写成独立一点，表箭射出后弦颤动，或加攴表声、加止表行。转义：发射→离去、派遣、生发、启动、发布、呈现、发扬。音源：借音字，拄杖而立故义音同「犮」。字族衍义：①癹草→除草割草 ②癹草时脚的运行→划动、分拨。"
N="字形：古文字字形库未收。"
D=[("癶","bō","本部部首字——两足相背、交叉，行走不顺。","b「闭剥」取「剥」：足剥地而交。",P),
("舛","chuǎn","与癶一字——两足相背、交错；引申违背、错乱。","ch「刺持」取「刺」：足刺而错。",P),
("荈","chuǎn","《集韵》「茶叶老者」——《类篇》「茶晚取者名荈」，即悖时令。","ch「刺持」取「持」：老叶持枝。",P),
("𥬫","chuǎn","《集韵》「竹以贯物也」——义音同「串」。","ch「刺持」取「刺」：竹刺而贯。",P),
("曻","shēng","同「昇」——上升。","sh「失收」取「收」：气收而升。",P),
("癹","bá","本部部首字——以足踏草、中耕除草（徕田）。","b「闭剥」取「剥」：足剥草而除。",F),
("𢯸","bá","《集韵》「癹，以足蹋夷艸，或从足、从手」——除草。","b「闭剥」取「剥」：手剥草而芟。",F),
("𦳠","bá","《集韵》「癹，除草也，或从艸」。","b「闭剥」取「剥」：草剥而去。",F),
("鏺","pō","《说文》「两刃，木柄，可以刈草」——长柄两刃镰刀。","p「拼辟」取「辟」：刃辟而刈。",F),
("撥","bō","《说文》「治也」——治理；今义用手指或棍子推动挑起，本义即癹。","b「闭剥」取「剥」：手拨而分。",F)]
for ch,p,xp,sm,b in D:
    sec=[{"key":"bengen","label":"字根本义","text":b,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取「两足交踏——除草／分拨」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":("源自《系統漢語》第423部「癶部」（卷七十 亥）；字卡五步规程。" if b==P else "源自《系統漢語》第424部「癹部」（卷七十 亥）；字卡五步规程。"),"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm,b) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡423a424a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡423a424a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡423a424a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
import json,subprocess,os,glob
C9=("【采部余字】部首采（cǎi）：甲骨文从爪从木，象意采摘树上的果实或叶子；《说文》「捋取也」。轉義：选择、获取；采桑柞饲蚕、采草木染布故引申色彩；采以为食故引申采食之地、封地乃至坟墓。音源：源自采摘声。字族衍义：①采以为食 ②采以为染料 ③采摘行为。")
C8=("【才部】部首才（𧴶cái）：甲骨文从「一」穿过「▽」，「▽」与「不」「帝」所从相同，指花房；从「一」表示连接花房果蒂与枝茎的梗。轉義：花未成而先有梗→开始、起初（《集韵》「始也」）；梗承载花果、输送养分，细梗而大花重果→才能（《广韵》「用也、质也、力也、文才也」）；连梗采摘易伤枝茎，须裁切留梗→剪裁；花谢果熟从蒂部先梗而落，残梗后枯→留存（「存、在」皆从才声）。辯證：小篆省去花房结构，故《说文》「艸木之初也，从一上贯一」析形不确。音源：借音字，义音同「采」。字族衍义：①以小胜大表才能 ②开始 ③形近「丰、木」之讹。")
N1="字形：古文字字形库未收；原稿该部有「▲战国铜器上的采桑纹饰」可参。"
N2="字形：古文字字形库未收；原稿该部有「▲花的结构图」可参。"
D=[
("踩","cǎi",C9,N1,"《篇韵》「音葵，跳也。又音劣，义同」；cǎi 践踏——以足着地而取径，是采摘之手移到脚下。","主组③之足：以「足」定其落点，践踏如采撷般直取。","c「刺持」取「刺」：足刺地而行。"),
("睬","cǎi",C9,N1,"《字彙補》「此宰切，音彩。偢睬，俗言也」——理会、答理（今语「理睬」）。","主组③之目：以「目」定其落点，看一眼即算应。","c「刺持」取「刺」：目刺而应。"),
("採","cǎi",C9,N1,"《正韵》「同采。摘也、取也、揽也」——「采」加手之累增字，义不变。","主组③之正：以「手」定其动，正写采摘之形。","c「刺持」取「刺」：手刺而取。"),
("啋","cǎi",C9,N1,"《汉典》「幸运，喜幸；理睬、理会」；《篇海》「许饶切，音嚣。諠也、大也、动也、不安静也」；cāi 语气词。","主组③之声：以「口」定其声，出声以应、以贺。","c「刺持」取「刺」：声刺入耳。"),
("鼒","zī",C8,N2,"从鼎才声，《说文》「鼎之圜掩上者」子之切；《玉篇》「小鼎也」——小口圆顶之鼎。","主组①之器：以「鼎」定其类，小而能容，即「以小胜大」。","z「凿总」取「凿」：铸鼎凿范而成。"),
("閉","bì",C8,N2,"从门，才所以歫（拒）门，《说文》「阖门也」博计切；《礼·月令》「修键闭」，郑注「键，牡；闭，牝也」——门闩。","主组①之直：以「门」定其处，一木横拒而门合。","b「闭剥」取「闭」：正是闭门。"),
("財","cái",C8,N2,"从贝才声，《说文》「人所宝也」昨哉切；《玉篇》「所以资生者」——物资与货币的总称。","主组①之富：以「贝」定其质，才之能生者聚为财。","c「刺持」取「持」：持贝而不散。"),
("材","cái",C8,N2,"从木才声，《说文》「木梃也」——大树干；《正字通》「其入于用者曰材」。","主组①之质：以「木」定其体，干之可用者为材。","c「刺持」取「持」：木持其用。"),
("𦬁","cái",C8,N2,"《类篇》引《博雅》「蘱、𦬁，𦳋也」；《广韵》「蔽前草箭」——蒯草，可编席。","主组①之草：以「艸」定其类，草之细而可束者。","c「刺持」取「刺」：蒯叶有刺而编。"),
("豺","chái",C8,N2,"从豸才声，《说文》「狼属，狗声」士皆切——豺狗，性凶残、好成群、体瘦。","主组①之兽：以「豸」定其类，兽之凶而群者。","ch「刺持」取「刺」：群起而刺噬。"),
]
def card(ch,p,Bx,Nx,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本义","text":Bx,"cites":[]},
      {"key":"zigen","label":"字形","text":Nx,"cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,Bx,Nx,a,b,c in D:
    json.dump(card(ch,p,Bx,Nx,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
ST={"踩":"《篇韵》「音葵，跳也。又音劣，义同」；cǎi 践踏。","睬":"《字彙补》「偢睬，俗言也」——理会、答理。","採":"《正韵》「同采。摘也、取也、揽也」——采加手之累增字。","啋":"《汉典》「幸运，喜幸；理睬、理会」；《篇海》「諠也、大也、动也」。","鼒":"《说文》「鼎之圜掩上者」；《玉篇》「小鼎也」——小口圆顶之鼎。","閉":"《说文》「阖门也。从门；才，所以歫门也」——门闩。","財":"《说文》「人所宝也。从贝才声」——物资与货币的总称。","材":"《说文》「木梃也。从木才声」——大树干，入于用者曰材。","𦬁":"《类篇》引《博雅》「蘱、𦬁，𦳋也」——蒯草，可编席。","豺":"《说文》「狼属，狗声。从豸才声」——豺狗，性凶残、好成群。"}
def B(ch):
    return "源自《系統漢語》第399部「采部」（卷六十六 采）；字卡五步规程。" if ch in ("踩","睬","採","啋") else "源自《系統漢語》第400部「才部」（卷六十六 采）；字卡五步规程。"
cl=[{"id":f"bci-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
   "statement":f"{d[0]}（{d[1]}）：{ST[d[0]]}","boundary":B(d[0]),"permission":"public",
   "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡399余+400才部首6字2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡400才部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡400才部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
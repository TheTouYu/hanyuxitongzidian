import json,os,io,re,subprocess
D=r"web\public\cards"
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
C=("部頭徹（彻）：甲骨文从又从鬲，象意搬動食器鬲——吃完後收拾空的鬲（《六書故》「屏去釜鬲徹饌之義」）。"
   "轉義：撤走鬲→拆除、毀壞、陳設；由鬲之空盡→通達、透明（《廣韻》「通也、明也、道也、達也」）。"
   "辯證：戰國古文「鬲」演作「育」、「又」演作「攴」，另加「彳」表行走；《說文》「从彳从攴从育」所錄古文才是本體。音源：借音，因拖開之意義音同「也」。字族衍義：①撤除→發射抽走 ②空盡→通達透明。")
def card(ch,py,pang,lian,sm):
    return {"char":ch,"pinyin":py,"bus":["368.徹部"],"sources":["卷六十二  蛇.docx 368.徹部"],
            "sections":[S("bengen","字根（第368部：徹部）",C),S("xingpang","形旁·声旁",pang),
                        S("hengxiang","横向比较",lian),S("shengmu","声母义",sm)]}
rows=[
("徹","chè","徹＝又＋鬲之象意，本義撤去食器（吃完收鬲）；引申拆除、通達、透明。","撤除：徹（又鬲）撤｜撤（手）撤｜澈（水）澄。","穿母ch，「刺持」取「刺」：剔除而盡。"),
("勶","chè","勶（撤）＝力＋徹（形旁），徹亦聲。《說文》「發也」——發射；《集韻》「撤，去也」。","①撤除：勶（力）發｜撤（手）撤｜發（弓）發。","穿母ch，「刺持」取「刺」。"),
("轍","zhé","轍（軼）＝車＋徹省聲。《說文新附》「車跡也」——車輪碾出的痕跡，亦可指道路。","②空盡：轍（車）車跡｜軌（車）軌｜迹（辵）跡。","照母zh，「鑿總」取「鑿」。"),
("澈","chè","澈（𤁲）＝水（形旁）＋徹（聲旁）。《玉篇》「水澄也」水清；《正字通》「澈者，水竆也」水盡。","②空盡：澈（水）清澈｜澄（水）澄｜清（水）清。","穿母ch，「刺持」取「刺」。"),
("瞮","chè","瞮＝目（形旁）＋徹（聲旁）。《集韻》「明也」——目明。","②空盡：瞮（目）目明｜㬚（日）日明｜明（日）明。","穿母ch，「刺持」取「刺」。"),
("𨅊","zhé","𨅊（𨇂）＝足（形旁）＋徹（聲旁）。《集韻》「轍或从足」車跡；chè 又通「徹」。","②空盡：𨅊（足）車跡｜轍（車）轍｜跡（足）跡。","照母zh，「鑿總」取「鑿」。"),
("㬚","chè","㬚（𦠣）＝日（形旁）＋徹（聲旁）。《集韻》「明也」——日光透亮。","②空盡：㬚（日）日明｜瞮（目）目明｜徹（彳）通。","穿母ch，「刺持」取「刺」。"),
("䒆","chè","䒆＝舟（形旁）＋徹（聲旁）。《集韻》「船行也」；《玉篇》「舟也」。","②空盡：䒆（舟）船行｜舟（舟）舟｜航（舟）航。","穿母ch，「刺持」取「刺」。"),
("𠾀","zhé","𠾀＝口（形旁）＋轍聲。《篇海》「語不止貌」——話說個不停。","①撤除：𠾀（口）語不止｜轍（車）轍｜喋（口）喋。","照母zh，「鑿總」取「鑿」。"),
("𦅄","zhé","𦅄＝糸（形旁）＋徹聲。《集韻》「衣破」。","①撤除：𦅄（糸）衣破｜破（石）破｜裂（衣）裂。","照母zh，「鑿總」取「鑿」。"),
]
for ch,py,pang,lian,sm in rows:
    open(os.path.join(D,ch+".json"),"w",encoding="utf-8",newline="\n").write(json.dumps(card(ch,py,pang,lian,sm),ensure_ascii=False,indent=1))
print("cards",len(rows))
B="源自《系統漢語》卷六十二「蛇」部之「徹部」（第368部）；字卡五步规程。"
cl=[(f"zk-{391+i}",f"{ch}本義：{pang.split('。')[0]}",f"{ch}（{py}）：{pang} 橫向：{lian}")
    for i,(ch,py,pang,lian,sm) in enumerate(rows)]
draft={"schema_version":1,"intent":"字卡徹部首10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in cl:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第四十一批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h)
print("applied", '"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h))
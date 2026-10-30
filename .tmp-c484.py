import json,subprocess,os,glob
BZH="【416 甾部】甾＝甲骨文从屮（草）被水淹没之形，后作从田𡿧声，指水淹田；转义：浸渍之田泥变黑，引申指黑色（分化作缁）。字族衍义：①草木被淹死→直立、参差 ②浸渍之泥→黑色。"
BZAI="【417 宰部（原属它部，从宀从辛）】宰＝从宀从辛，象意家里负责主刀的人，即屠夫、杀牲畜者（故或指屠杀，如屠宰场；或指主持分祭肉的人，《史记·陈丞相世家》「里中社，平为宰，分肉食甚均」），为「𣪮」之初文（《集韵》「杀也，通作宰」）。转义：因其在家臣中属领头的，故引申指主管、主持（主宰、宰相），再由主管引申指治理（《玉篇》「治也、制也」）；古代宰杀除刀杀外还采用沉、埋、缢，故或引申指坟墓（《公羊传》「宰上之木拱矣」）、又引申指渣滓（分化作「滓」）。辯證：《说文》误以「辠」为「辛」的本义，故释宰为「辠人在屋下执事者」，所释不确。音源：借音字，因有水淹之意而义音同「甾」（滓／缁互作）。字族衍义：①指主管、统领 ②指宰杀、灭绝 ③指淹死，表示形、色如渣滓 ④形近「𡨧」之讹。"
N="字形：古文字字形库未收。"
D=[
{"ch":"䐉","p":"zì","ben":BZH,"xp":"《玉篇》「腊䐉也」；《正字通》「讹字，《说文》无䐉字」，大约即「腦」之讹。","sm":"z「凿总」取「总」：肉总而肥。"},
{"ch":"䣎","p":"zī","ben":BZH,"xp":"《集韵》「乡名」；《正字通》「讹字」。","sm":"z「凿总」取「总」：地名借声。"},
{"ch":"宰","p":"zǎi","ben":BZAI,"xp":"从宀从辛——屋下主刀之人，屠夫、分祭肉者。","sm":"z「凿总」取「凿」：刀凿而宰。"},
{"ch":"榟","p":"zǐ","ben":BZAI,"xp":"《说文》「楸也」——梓树，主干通直平滑高大，号称「百木长」「木王」。","sm":"z「凿总」取「总」：百木总长。"},
{"ch":"縡","p":"zài","ben":BZAI,"xp":"《说文》「事也」；《玉篇》「载也」；又同「缯」，丝织品总名。","sm":"z「凿总」取「总」：丝总而织。"},
{"ch":"㱰","p":"zǎi","ben":BZAI,"xp":"《集韵》「灭也」——灭绝。","sm":"z「凿总」取「凿」：尽凿而灭。"},
{"ch":"𣪮","p":"zǎi","ben":BZAI,"xp":"《集韵》「杀也，通作宰」——宰之或体。","sm":"z「凿总」取「凿」：击杀如凿。"},
{"ch":"𤌊","p":"zǎi","ben":BZAI,"xp":"《集韵》「烹也」——烹煮。","sm":"z「凿总」取「凿」：火凿而烹。"},
{"ch":"滓","p":"zǐ","ben":BZAI,"xp":"《说文》「淀也」——沉淀下来的渣滓；疑本指用溺水法宰杀牲畜。","sm":"z「凿总」取「总」：渣滓总沉。"},
{"ch":"䔂","p":"zǐ","ben":BZAI,"xp":"《说文》「羹菜也」——菜肉作的羹汁，取「滓」意。","sm":"z「凿总」取「总」：菜总成羹。"},
{"ch":"𦞤","p":"zǐ","ben":BZAI,"xp":"《集韵》「食所遗也」——剩余食物；或带骨肉酱；又「囟」之或体。","sm":"z「凿总」取「总」：余食总留。"},
{"ch":"䏁","p":"zǎi","ben":BZAI,"xp":"《说文》「聋也，秦晋听而不闻谓之䏁」——半聋，取「滓」意：耳被堵住。","sm":"z「凿总」取「凿」：耳塞如凿。"},
]
for e in D:
    sec=[{"key":"bengen","label":"字根本义","text":e["ben"],"cites":[]},
         {"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":e["xp"],"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「主刀分肉／淹死成滓」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":e["sm"],"cites":[]}]
    json.dump({"char":e["ch"],"pinyin":e["p"],"bus":[],"sections":sec},open(rf"web\public\cards\{e['ch']}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{e['ch']}（字卡）",
   "statement":f"{e['ch']}（{e['p']}）：{e['xp']}","boundary":("源自《系統漢語》第416部「𡿧部」（卷六十九 舄）；字卡五步规程。" if e["ben"]==BZH else "源自《系統漢語》第417部「宰部」（卷六十九 舄）；字卡五步规程。"),
   "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,e in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡416e417a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡416e417a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡416e417a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
import json,subprocess,os,re,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十一  犀.docx"); ps=d.paragraphs
n=0
for b in ps[132]._p.findall('.//'+qn('a:blip')):
    rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
    if part is None or not hasattr(part,'blob'): continue
    im=Image.open(io.BytesIO(part.blob))
    if max(im.size)<200: continue
    os.makedirs(r"web\public\glyphs\photos\㚇",exist_ok=True)
    im.convert("RGB").save(r"web\public\glyphs\photos\㚇\01.jpg","JPEG",quality=90); n+=1
print("photo",n)
B="源自《系統漢語》卷六十一「犀（屖）」部之「囟部」（第354部）；字卡五步规程。"
rows=[
("zk-092","匈本義：从勹凶聲，膺也，胸之初文","匈（匃𦙄，xiōng）从勹、凶聲，轉注。甲骨文从「凶」在「人」胸部，指心窩，為「胸」之初文；心窩如囟門因心跳而湧動。《說文》「膺也。从勹，凶聲，許容切」，古文或从肉作胷。字族一路指心跳→擾動不安，一路為形近𣬉之訛。"),
("zk-093","胸本義：从肉匈聲，膺也","胸（胷匈，xiōng）从肉、匈聲，轉注，匈之後起形聲。《廣韻》「膺也，亦作匈、𦙄」，胸膛。"),
("zk-094","洶本義：从水匈聲，湧也","洶（汹，xiōng）从水、匈聲，轉注，取心跳湧動。《說文》「湧也。从水匈聲，許拱切」；《集韻》「水勢，或作汹」。"),
("zk-095","詾本義：从言匈聲，訟也、眾言喧嘩","詾（訩𧧗，xiōng）从言、匈聲，轉注，取喧擾。《說文》「說也。从言匈聲」；《類篇》引《詩》傳「訟也，一曰盈也，一曰眾言」；《廣韻》「嚇也」，恐嚇。"),
("zk-096","恟本義：从心匈聲，擾恐也","恟（忷，xiōng）从心、匈聲，轉注，取心跳。《集韻》引《說文》「擾恐也」，恐懼驚駭、心狂跳之狀。"),
("zk-097","㚇本義：从夊凶聲，囟門未合之幼兒，引申叢聚","㚇（𡕩𡕫𡕢𡕰，zōng/miǎn）从夊（倒退，表幼弱）、凶聲，轉注。本同「兇」，指囟門未合之幼兒；護囟留髮不剃，由蓄髮之狀引申叢聚（《玉篇》「聚也、最也」）。辯證：《說文》「斂足也…从夊凶聲」所釋斂足雖通，然「凶」與鳥飛無涉，析形不確；「𡕩」从囟最為標準，「𡕫」為訛字。"),
("zk-098","嵏本義：从山㚇聲，峰聚之山","嵏（zōng）从山、㚇聲，轉注，取高聳叢聚。《說文》「九嵏山，在馮翊谷口，从山㚇聲，子紅切」；《正字通》「峰聚之山曰嵏」。"),
("zk-099","堫本義：从土㚇聲，穜也，種植捅穿","堫（䎫，zōng）从土、㚇聲，轉注，取聚束入土。《說文》「穜也，一曰內其中也，从土㚇聲，子紅切」，種植、捅穿；《集韻》「不耕而種，或作䎫」。"),
("zk-100","糉本義：从米㚇聲，蘆葉裹米，角黍","糉（粽，zòng）从米、㚇聲，轉注，取聚束成角。《說文》「蘆葉裹米也。从米㚇聲，作弄切」；《集韻》「角黍也，或作粽」。"),
("zk-101","稯本義：从禾㚇聲，禾四十秉為稯","稯（𥞝𥠡，zōng/zǒng）从禾、㚇聲，轉注，取聚束。《說文》「布之八十縷為稯，从禾㚇聲，子紅切」，《段注》「禾四十秉為稯」；《集韻》「禾聚束也」。"),
("zk-102","椶本義：从木㚇聲，栟櫚，葉簇生頂","椶（zōng）从木、㚇聲，轉注，取葉簇聚。《說文》「栟櫚也，可作萆，从木㚇聲，子紅切」，棕櫚樹，葉簇生頂端。"),
("zk-103","騣本義：从馬㚇聲，馬鬣也","騣（zōng）从馬、㚇聲，轉注，取鬣毛聳聚。《新附》「馬鬣也。从馬㚇聲，子紅切」，馬頸長毛；《玉篇》「金騣，馬冠也」。"),
]
draft={"schema_version":1,"intent":"字卡匈㚇族12条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十三批.json"
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
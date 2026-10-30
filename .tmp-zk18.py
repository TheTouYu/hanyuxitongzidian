import json,subprocess,os,re,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十一  犀.docx")
for i in (348,347,346):
    got=False
    for b in d.paragraphs[i]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob))
        if max(im.size)>=200:
            os.makedirs(r"web\public\glyphs\photos\銃",exist_ok=True)
            im.convert("RGB").save(r"web\public\glyphs\photos\銃\01.jpg","JPEG",quality=90)
            print("PIC",i,im.size); got=True; break
    if got: break
B="源自《系統漢語》卷六十一「犀（屖）」部之「允部」（第357部）；字卡五步规程。"
rows=[
("zk-151","允本義：象人肩上騎人，夋之初文","允（𠃔𠘭，yǔn）甲骨文象人肩上騎人之形，與「異」表意近似，為「夋」之初文（《玉篇》「倨也」）。轉義：騎與被騎建立在互信→信任（《廣韻》「信也」）、應允（《增韻》「肯也」）；能承受上重→相當（《玉篇》「當也」）；被騎走不快→行走緩慢；人上有人→超俊（分化為夋）。辯證：西周後上人形演作「㠯」，故《說文》「信也，从儿㠯聲」析形不確。音源：借音字，因有高峻義義音同囟（總一本作統）。"),
("zk-152","阭本義：从阜允聲，高也，一曰石","阭（yǔn/yǎn）从阜、允聲，轉注，取高。《說文》「高也，一曰石也，从𨸏允聲，餘准切」，高峻或指石；yǎn《玉篇》「地名也」。"),
("zk-153","𡴞本義：从辵允聲，進也，騎馬而進","𡴞（允，yǔn）从辵、允聲，轉注。《說文》「進也。从𠦍从屮，允聲，《易》𡴞升大吉，餘准切」，前進；𠦍本指騎馬，當指騎馬而進。"),
("zk-154","馻本義：从馬允聲，馬毛逆，疑同駿","馻（yǔn）从馬、允聲，轉注。《玉篇》「馬毛逆」；疑本同「駿」，指堪騎善奔的良馬。"),
("zk-155","狁本義：从犬允聲，獫狁，匈奴別號","狁（yǔn）从犬、允聲，轉注。《集韻》「獫狁，匈奴別號」——北方人個頭高大故从允，从犬乃貶意。"),
("zk-156","玧本義：从玉允聲，玉䞓色；充耳玉","玧（璊㻊，mén/yǔn）从玉、允聲，轉注。《集韻》引《說文》「璊，玉䞓色也，禾之赤苗謂之虋，言璊玉色如之」；yǔn《廣韻》「充耳玉」。"),
("zk-157","吮本義：从口允聲，欶也，含吸","吮（shǔn）从口、允聲，轉注。《說文》「欶也。从口允聲，徂沇切」，撮攏伸長嘴含吸。"),
("zk-158","㽙本義：从田允聲，古允字，同畯","㽙（畯，jùn）从田、允聲，轉注。《字彙補》「古允字」；《集韻》「畯，《說文》農夫也，一曰典田官，一曰農神」。"),
("zk-159","鈗本義：从金允聲，侍臣所執兵；銳之訛","鈗（銳，yǔn/duì）从金、允聲，轉注兼訛字。《說文》「侍臣所執兵也。从金允聲，《周書》一人冕執鈗，讀若允，餘凖切」，侍臣所持矛類兵器；duì《集韻》「銳，矛屬，或作鈗」——銳之訛字。"),
("zk-160","抁本義：从手允聲，動也、搖也","抁（𢯻挩，yǎn）从手、允聲，轉注。《玉篇》「動也、搖也」；《集韻》「動也、揣也，或从兗」；挩《博雅》「動也」。"),
]
draft={"schema_version":1,"intent":"字卡允部10条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十八批.json"
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
import json,subprocess,os,re,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
# 1) photo p499
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx")
got=None
for j in (499,500,498):
    for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob))
        if max(im.size)<200: continue
        os.makedirs(r"web\public\glyphs\photos\𩰫",exist_ok=True)
        im.convert("RGB").save(r"web\public\glyphs\photos\𩰫\01.jpg","JPEG",quality=90)
        got=(j,im.size); break
    if got: break
print("photo",got)
B="源自《系統漢語》卷六十「𩰫」部（第351部）；字卡五步规程。"
items=[
("zk-045","竵本義：从立𩰫聲，不正也","竵（wāi/huá）从立、𩰫聲，屬轉注，聲旁取歪斜。《說文》「不正也。从立𩰫聲。火鼃切」，《廣韻》「物不正」，《集韻》「𦮃，不正也，或作華、𠇗、竵」。"),
("zk-046","𧬭本義：从言𩰫聲，惰也、黠也","𧬭（huà）从言、𩰫聲，借聲之字。《集韻》「諣，惰也、黠也，或作𧬭」。"),
("zk-047","𠿎本義：从口𩰫聲，口戾貌，俗咼字","𠿎（huā）从口、𩰫聲，屬轉注，聲旁取歪斜。《玉篇》「虎佳切，口戾皃」，《廣韻》「口偏」，《正字通》「俗咼字」。"),
("zk-048","𡢓本義：从女𩰫聲，籀文媧字","𡢓（wā）从女、𩰫聲。《說文》「媧，古之神聖女，化萬物者也。从女咼聲。𡢓，籀文媧从𩰬」——聲符由咼改作𩰬而音同，為媧之籀文。"),
("zk-049","𩦣本義：从馬𩰫聲，黃馬黑喙，即嘴不正","𩦣（騧、𩢍，guā）从馬、𩰫聲，屬轉注。《集韻》「騧，《說文》黃馬黑喙，籀从𩰬，或作𩢍」，指黃毛黑嘴之馬；原稿點明「即嘴不正之意」。"),
("zk-050","𧒘本義：从虫𩰫聲，細腰土蜂，或从果","𧒘（蜾、蝸，guǒ）从虫、𩰫聲，屬轉注。《說文》「𧒘蠃，蒲盧，細要土蠭也…从虫𩰬聲，或从果，古火切」，《集韻》「亦作蝸」；陶弘景注「土蜂一種，黑色，腰甚細，銜泥於人壁及器物邊作窠」。細腰如「不正」，其窠圓如小果。"),
]
draft={"schema_version":1,"intent":"字卡𩰫部六条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第八批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
pid=re.search(r'pln_[0-9a-f]+',out).group(0); print("PLAN",pid)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1)
print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
print("done")
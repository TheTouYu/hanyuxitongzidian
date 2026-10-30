import json,subprocess,os,re,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十  𦟀.docx")
got=None
for j in (515,516,514):
    for b in d.paragraphs[j]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob))
        if max(im.size)<200: continue
        os.makedirs(r"web\public\glyphs\photos\委",exist_ok=True)
        im.convert("RGB").save(r"web\public\glyphs\photos\委\01.jpg","JPEG",quality=90); got=(j,im.size); break
    if got: break
print("photo",got)
B="源自《系統漢語》卷六十「委」部（第352部）；字卡五步规程。"
items=[
("zk-051","逶本義：从辵委聲，逶迤斜行曲折","逶（wēi）从辵、委聲，屬轉注，聲旁取「下垂而曲」。《說文》「逶迤，衺去之皃。从辵委聲，或从虫、爲。於為切」，指斜行、彎曲連綿、曲折行進、隱蔽宛轉。"),
("zk-052","捼本義：从手委聲，推也，兩手相切摩","捼（ruó/wō/wěi）从手、委聲，屬轉注。《說文》「推也。从手委聲。一曰㒳手相切摩也。奴禾切」，徐鉉「今俗作挼」；《廣韻》「捼挱，兩手相切摩也」。"),
("zk-053","萎本義：从艸委聲，蔫也，草木枯死","萎（wěi/wèi）从艸、委聲，屬轉注，聲旁取枯萎下垂。《唐韻》「蔫也」，《集韻》「艸木枯死」「萎腇，耎弱也」；wèi《說文》「食牛也」，喂牛乾草。"),
("zk-054","痿本義：从疒委聲，痹也，肌萎不能行","痿（wěi）从疒、委聲，屬轉注，聲旁取柔弱委頹。《說文》「痹也。从疒委聲。儒隹切」，指身體某部分萎縮或失功能、不能行動；《玉篇》「不能行也，痺濕病也」。"),
("zk-055","餧本義：从食委聲，饑也，魚敗亦曰餧","餧（něi/wèi）从食、委聲，屬轉注，聲旁取柔弱。《說文》「饑也。从食委聲。一曰魚敗曰餧。奴罪切」；wèi《廣雅》「食也」，餵食。"),
("zk-056","緌本義：从糸委聲，系冠纓，垂而下","緌（ruí）从糸、委聲，屬轉注，聲旁取下垂。《說文》「系冠纓也。从糸委聲。儒隹切」，指帽帶系結後下垂的部分；《爾雅》「繼也、縭也」；《集韻》「一曰垂也」，或作綏。"),
("zk-057","倭本義：从人委聲，順皃；又國名、倭墮髻","倭（wēi/wō/wǒ）从人、委聲，屬轉注，聲旁取下垂柔順。《說文》「順皃。从人委聲，《詩》曰周道倭遟。於為切」；wō《玉篇》「國名」，古代稱日本；wǒ《集韻》「倭墮，髻皃」，髮髻歪在一側。"),
("zk-058","矮本義：从矢委聲，短人也","矮（ǎi）从矢、委聲，屬轉注：《新附》「短人也。从矢委聲。烏蟹切」，矢為長度之準，取委之短縮下垂。"),
("zk-059","踒本義：从足委聲，足跌也，足骨折","踒（wō/ruí/wēi）从足、委聲，屬轉注，聲旁取曲折。《說文》「足跌也。从足委聲。烏過切」，《集韻》「折也，或作踠」；ruí 為弩名（張弩必以足）；wēi 同「逶迤」。"),
("zk-060","蜲本義：从虫委聲，蜲蛇，形如蛇紆曲","蜲（wēi/wěi）从虫、委聲，屬轉注，聲旁取曲折。《廣韻》「蜲蛇」；《集韻》「水精也，形如蛇紆曲，長八尺，以名呼之可使取魚，通作蟡」；wěi 為蟲名黍負（鼠負）。"),
("zk-061","諉本義：从言委聲，累也，煩累推託","諉（wěi）从言、委聲，屬轉注，聲旁取「委棄、推委」。《說文》「累也。从言委聲。女恚切」，《集韻》「諈諉，煩重皃」，煩累拖累；後世作推諉、推託。"),
("zk-062","崣本義：从山委聲，嶊崣，山高貌","崣（wěi）从山、委聲，屬轉注，聲旁取高而下垂之勢。《集韻》「嶊崣，山高皃」。"),
]
draft={"schema_version":1,"intent":"字卡委部十二条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第九批.json"
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
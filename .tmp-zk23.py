import json,subprocess,os,re,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
d=Document(r"D:\字谱智能体\卷六十二  蛇.docx")
for i in (143,144):
    for b in d.paragraphs[i]._p.findall('.//'+qn('a:blip')):
        rid=b.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob))
        if max(im.size)>=200:
            os.makedirs(r"web\public\glyphs\photos\杝",exist_ok=True)
            im.convert("RGB").save(r"web\public\glyphs\photos\杝\01.jpg","JPEG",quality=90)
            print("PIC",i,im.size); break
B="源自《系統漢語》卷六十二「蛇」部之「也部」（第360部）；字卡五步规程。"
rows=[
("zk-210","䶔本義：从齒也聲，齒齗見","䶔（chí）从齒、也聲，轉注，取蛇牙。《玉篇》「齒齗見」——牙齦外露，如蛇牙外露。"),
("zk-211","䗐本義：从虫施聲，蛄䗐強羋（米象）","䗐（shī）从虫、施聲，轉注。《說文》「蛄䗐，強羋也，从虫施聲，式支切」——米象，米中蛀蟲。"),
("zk-212","狏本義：从犬也聲，獸似犬赤喙白首","狏（𤝻𤝛𧳁，tuó/yí）从犬、也聲，轉注。《集韻》「獸名，似犬，赤喙白首，見則荒」；《山海經》鮮山有獸如膜犬、赤喙赤目白尾，名曰𤝻。"),
("zk-213","葹本義：从艸施聲，枲耳（蒼耳）","葹（shī）从艸、施聲，轉注。《廣雅》「苓耳、葹、常枲、胡枲，枲耳也」；《玉篇》「卷葹草，拔心不死」——蒼耳子；《增韻》「豆屬」。"),
("zk-214","絁本義：从糸也聲，粗緒；繒屬","絁（䌳䌤𦇲𦂛，shī）从糸、也聲，轉注，取蛻皮質地。《集韻》引《說文》「粗緒也，一曰繒屬」；《玉篇》「粗細經緯不同者」——古時粗綢。"),
("zk-215","肔本義：从肉也聲，引腸也","肔（胣，chǐ）从肉、也聲，轉注，取蛻皮。《玉篇》「引腸也」；《廣韻》「裂也」；《集韻》「刳腸也」。"),
("zk-216","迆本義：从辵也聲，衺行也","迆（迤，yǐ）从辵、也聲，轉注，取爬行。《說文》「衺行也」（《夏書》「東迆北，會于匯」）斜行如蛇；《廣韻》「邐迆，連接」；《玉篇》「邐迆，水曲流也」。"),
("zk-217","虵本義：从虫也聲，毒蟲，正作蛇","虵（蛇迤，shé）从虫、也聲，轉注（也即本字）。《玉篇》「毒蟲，正作蛇」；yě 虵蛭氏虜姓；yí 委蛇＝委曲自得。"),
("zk-218","𢻱本義：从攴也聲，𢾭也，施行敷布","𢻱（shī）从攴、也聲，轉注。《說文》「𢾭也，从攴也聲，讀與施同，式支切」，施行、敷布。"),
("zk-219","暆本義：从日施聲，日行暆暆","暆（yí）从日、施聲，轉注。《說文》「日行暆暆也。从日施聲，弋支切」，太陽迤邐徐行；樂浪有東暆縣。"),
("zk-220","馳本義：从馬也聲，大驅也","馳（chí）从馬、也聲，轉注，取爬行疾速。《說文》「大驅也」使馬長驅；《廣雅》「犇也」；《集韻》「走也」。"),
("zk-221","弛本義：从弓也聲，弓解也","弛（𢐋，chí）从弓、也聲，轉注。《說文》「弓解也」弓弦鬆弛——正眼鏡蛇放鬆頸褶之狀；《廣韻》「釋也」；《集韻》「改易也，通作施」「落也」。"),
]
draft={"schema_version":1,"intent":"字卡也部12条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第二十三批.json"
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
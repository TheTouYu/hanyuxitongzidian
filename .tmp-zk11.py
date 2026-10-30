import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部（第353部）；字卡五步规程。"
rows=[
("zk-069","徲本義：从彳犀聲，久也","徲（tí/chí）从彳、犀聲，轉注，聲旁取遲緩。《說文》「久也。从彳犀聲。讀若遲，杜兮切」；《字彙》「久待也」；《集韻》「後至」；chí《博雅》「徲徲，往來也」。"),
("zk-070","稺本義：从禾屖聲，幼禾也","稺（穉稚，zhì）从禾、屖聲，轉注，聲旁取幼弱。《說文》「幼禾也。从禾屖聲。直利切」，幼小禾苗，引申幼稚、幼小。"),
("zk-071","㓾本義：从刀屖聲，破皮、劃開","㓾（xī/chí）从刀、屖聲，轉注，取屖「刻刀」本義。《玉篇》「𠞮也」破皮；《字彙》「㓾魚」破魚、劃開。"),
("zk-072","䙙本義：从衣屖聲，衣也","䙙（chí）从衣、屖聲，轉注，屬犀牛皮「紋飾相似」一路。《字彙》「音池。衣也」。"),
("zk-073","𦃘本義：从糸屖聲，針縫也","𦃘（zhì）从糸、屖聲，轉注。《類篇》「紩也」；《玉篇》「刺𦃘，針縫也」，用針縫補。"),
("zk-074","墀本義：从土犀聲，塗地也","墀（chí）从土、犀聲，轉注。《說文》「塗地也。从土犀聲，《禮》天子赤墀，直泥切」，塗飾地面；《字彙》「階上地也」；或同坻，水中高地。"),
("zk-075","樨本義：从木犀聲，木名桂花，皮紋如犀","樨（xī）从木、犀聲，轉注，取犀牛皮紋相似。《字彙》「木名，桂花，俗名木樨花」，樹皮紋如犀牛皮。"),
("zk-076","厗本義：从厂屖省聲，唐厗石也","厗（tí）从厂、屖省聲，轉注。《說文》「唐厗，石也。从厂，屖省聲，杜兮切」；《玉篇》「古銻字」；《廣韻》「鎕銻，火齊也」，火齊珠（琉璃）。"),
("zk-077","𧎨本義：从虫犀聲，蛭也","𧎨（chí）从虫、犀聲，轉注，取犀牛皮厚相類之蠕蟲。《類篇》「蟲名，蛭也」，螞蟥。"),
("zk-078","𣖅本義：从木屖聲，研米槌也","𣖅（𣖸𣹲漽𣸒，tí）从木、屖聲，轉注。《廣韻》「漽，研米槌也，𣖅上同」；《集韻》「𣸒，米瀾也，或从屖」，淘米水。"),
]
draft={"schema_version":1,"intent":"字卡犀部续十条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十一批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h); print(run("bundle-apply",b,"--apply","--content-hash",h)[:120])
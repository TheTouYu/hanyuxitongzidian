import json,subprocess,os,re,io
B="源自《系統漢語》卷六十「妥」部（第349部）；字卡五步规程。"
items=[
("zk-029","俀本義：从人妥聲，弱也","俀（tuǐ）从人、妥聲，屬轉注，聲旁取柔弱委頹。《集韻》「弱也」，軟弱之貌。同取弱者：㞂（尢）風疾不行、㱣（歹）弱也、餒（食）饑弱、娞（女）柔弱。"),
("zk-030","骽本義：从骨妥聲，股也，大腿胯骨","骽（tuǐ）从骨、妥聲，屬轉注，聲旁取身之下委。《集韻》「股也，或作腿」，《玉篇》「骽股也」，指大腿、胯骨。"),
("zk-031","㟎本義：从山妥聲，山高而長，委蛇堆疊","㟎（tuǐ/tuǒ）从山、妥聲，屬轉注，聲旁取委頹堆疊。《廣韻》「㟎㠑，山高皃」；tuǒ《集韻》「山長皃，或作𡽃、嶞」。"),
("zk-032","鞖本義：从革妥聲，鞌邊帶，馬鞍絛飾","鞖（suī）从革、妥聲，屬轉注，聲旁取安附。《集韻》「䪎，鞌邊帶，或作鞖」，指馬鞍上的絛飾、邊帶；帶附於鞍而使安。"),
("zk-033","浽本義：从水妥聲，浽微小雨；又濁也","浽（suī/něi）从水、妥聲，屬轉注，聲旁取柔弱細微。《集韻》「浽微，小雨」；něi 讀「涹，《博雅》濁也，或作浽」。"),
("zk-034","㱣本義：从歹妥聲，弱也，不平也","㱣（tuǐ）从歹、妥聲，屬轉注，聲旁取柔弱委頹。《廣韻》「㱬㱣，弱也」；《玉篇》「不平也」。同取弱病者：㞂（尢）、俀（人）、餒（食）。"),
]
draft={"schema_version":1,"intent":"字卡妥部再六条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第六批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
pid=re.search(r'pln_[0-9a-f]+',out); print("PLAN",pid.group(0) if pid else out[-300:]); pid=pid.group(0)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin); print("BUNDLE",b.group(0) if b else fin[-300:]); b=b.group(0)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1)
print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
print("done")
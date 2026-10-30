import json,subprocess,os,re,io
B="源自《系統漢語》卷六十「妥」部（第349部）；字卡五步规程。"
items=[
("zk-019","妥本義：从又从女，以手安撫女子，為娞（綏）之初文","妥（tuǒ）从又从女，「又」指手，或作「爪」同；从女，象意女子以手安撫，實為「娞（綏suī）」之初文，《廣雅》「撫也、舒也」。轉義：由安撫引申止息、安定（《爾雅》「止也、坐也」，《廣韻》「安也」）；又引申柔弱委頹，分化為俀（tuǐ）。辯證：《說文》失收而偏旁有之；或以「以手按女使之止坐」解，作者不取——同例「孚」非按子，且母親多以手輕撫哭鬧小兒使之安定。音源：借音字，義音同「貴」或「果」。"),
("zk-020","桵本義：从木妥聲，白桵，木理白疏易破","桵（ruí）从木、妥聲，屬轉注，聲旁取妥之「柔弱委頹」一面。《說文》「白桵，棫。从木妥聲。儒隹切」，段注引陸機「其材理全白，無赤心者為白桵，直理易破，可為犢車軸」。木質白而疏理易破，正合柔弱委頹。同取柔弱易折者：俀（人）弱也、㞂（尢）弱病。"),
("zk-021","挼本義：从手妥聲，摧也，兩手相切摩","挼（ruó/suī）从手、妥聲，屬轉注，聲旁取「以手相切摩」。《說文》「摧也。从手妥聲。一曰㒳手相切摩也。奴禾切」，《集韻》「捼，兩手相切摩，或作挼、撋」，即揉搓。此條屬妥部字族①「安撫，表示輕握、揉搓、平定」。同取其義者：捼、撋。"),
("zk-022","䅑本義：从禾妥聲，禾四把，攏束成束","䅑（ruí）从禾、妥聲，屬轉注，聲旁取「以手收束使有定形」。《集韻》「長沙謂禾四把曰䅑，或作䅗」。四把為一束，須以手攏之，與妥之「以手加之使定」同源。此條屬妥部字族③「成把、成束」；《集韻》又以「捰，理也，或作挼」證妥部與「果」音義相通。"),
]
draft={"schema_version":1,"intent":"字卡妥部四条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第四批.json"
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
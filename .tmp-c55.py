import json,io,os,re,subprocess
D=r"web\public\cards"; chars=["誎","梀","餗","踈"]
claims=[];i=0
for ch in chars:
    c=json.load(io.open(os.path.join(D,ch+".json"),encoding="utf-8"))
    sec={s["key"]:s["text"] for s in c["sections"]}
    bu=c["bus"][0]
    claims.append({"id":f"zk-{509+i}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":f"{ch}本義：{sec['xingpang'].split('。')[0]}",
      "statement":f"{ch}（{c['pinyin']}）：{sec['xingpang']} 橫向：{sec['hengxiang']}",
      "boundary":f"源自《系統漢語》卷六十三「索」部之「{bu.split('.')[1]}」；字卡五步规程。",
      "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
    i+=1
fn="intake/20261023-字卡第五十一批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps({"schema_version":1,"intent":"字卡束部4条入库 2026-10-23","risk":"low","claims":claims},ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1)
run("bundle-approve",b,"--apply","--content-hash",h)
ok='"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h)
print("plan",pid,"bundle",b,"hash",h[:16],"applied",ok)
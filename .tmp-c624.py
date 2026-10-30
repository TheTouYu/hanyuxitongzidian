import subprocess,os,re,json
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
def settle(pid):
    run("knowledge-plan","check",pid,"--mode","delta","--format","json")
    fin=run("knowledge-plan","finalize",pid,"--format","json")
    m=re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"[\s\S]*?"content_hash":\s*"([0-9a-f]+)"',fin)
    if not m: print("FIN FAIL",fin[:200]); return
    run("bundle-approve",m.group(1),"--apply","--content-hash",m.group(2))
    run("bundle-apply",m.group(1),"--apply","--content-hash",m.group(2))
    print("applied",m.group(1))
settle("pln_670fe55b777e3544d40d75388e")
out=run("knowledge-plan","init","--intent","慍昷義訂正2026-10-23","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0)
r=run("knowledge-plan","revise-claim",pid,"--claim-id","clm_A9A17716106ED7AB0E6DC609F5",
 "--statement","慍（yùn）从心𥁕聲：怒也、怨恨（《說文》「怒也。从心𥁕聲」）；𥁕（昷）與囚同源，从人在囗中（封閉保暖），小篆加皿為聲（密不透風故有溫熱之意），《玉篇》「和也」。",
 "--boundary","源自《系統漢語》第282部「囗部」之𥁕（昷）支（卷五十 豕）；字卡五步规程。",
 "--semantic-declaration","clarify","--reason","昷義依原稿订正：与囚同源、封闭保暖，非浴婴温水")
print("rev", '"ok": true' in r)
settle(pid)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))
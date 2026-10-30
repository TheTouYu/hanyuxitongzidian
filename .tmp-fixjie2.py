import json,subprocess,os,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
t=open(r"knowledge\hanzi-yinyuan\02y-zika.md",encoding="utf-8").read()
ids={}
for m in re.finditer(r"<!-- CLAIM:START (clm_[0-9A-F]+) -->\s*\n### ([^·\n]+)·",t):
    ids.setdefault(m.group(2).strip(),[]).append(m.group(1))
tgt=["骱","䯰","齘","芥","衸"]
picks={c:ids[c][-1] for c in tgt if c in ids}
print(picks)
out=run("knowledge-plan","init","--intent","fix介部归属2026-10-24","--risk","low","--baseline","worktree")
pid=re.search(r"pln_[0-9a-f]+",out).group(0)
F="【第81部「介部」】介＝甲骨文从人四周有小點（疥之初文／鎧甲）；轉義 助佑、間隔、堅固、大、單個。"
newst={"骱":"从骨介聲：䯦骱，小骨（《集韻》），一曰堅也。","䯰":"从髟介聲：簪髻（《正字通》「䯰、紒通」），束髮簪。","齘":"从齒介聲：齒相切也（《說文》），咬牙；一曰怒也。","芥":"从艸介聲：菜也（《說文》），芥菜（根莖包裹厚皮故从介），種子細小味辛辣。","衸":"从衣介聲：衣裾也（《玉篇》），刺膝、衣長皃。"}
for c,cid in picks.items():
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",newst[c],"--boundary","源自《系統漢語》第81部「介部」（卷十三 合）；字卡五步规程。","--semantic-declaration","clarify")
    print(c,cid,"ok" if "error" not in r.lower() else r[:200])
print(run("knowledge-plan","check",pid,"--mode","delta")[:200])
print(run("knowledge-plan","finalize",pid)[:200])
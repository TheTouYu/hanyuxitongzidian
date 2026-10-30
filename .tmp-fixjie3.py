import json,subprocess,os,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
pid="pln_0063ae8513f574ccf835d31ca6"
picks={'骱':'clm_C32E522AC173DCDF0666221559','䯰':'clm_01ADCFD37E8BA028B2CC595703','齘':'clm_7A56706A93574EC7D74899E7DE','芥':'clm_B0F3237D93B6D19BD96F76CA00','衸':'clm_1D3A73F2599D244DC710C08DF4'}
st={"骱":"从骨介聲：䯦骱，小骨（《集韻》），一曰堅也。","䯰":"从髟介聲：簪髻（《正字通》「䯰、紒通」），束髮簪。","齘":"从齒介聲：齒相切也（《說文》），咬牙；一曰怒也。","芥":"从艸介聲：菜也（《說文》），芥菜（根莖包裹厚皮故从介），種子細小味辛辣。","衸":"从衣介聲：衣裾也（《玉篇》），刺膝、衣長皃。"}
for c,cid in picks.items():
    r=run("knowledge-plan","revise-claim",pid,"--claim-id",cid,"--statement",st[c],"--boundary","源自《系統漢語》第81部「介部」（卷十三 合）；字卡五步规程。","--semantic-declaration","clarify","--reason","部属误标：原稿列入爪部「形近字介之訛」组，实属第81部介部")
    print(c,"OK" if '"ok": true' in r else r[:300])
print(run("knowledge-plan","check",pid,"--mode","delta")[:160])
print(run("knowledge-plan","finalize",pid)[:200])
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
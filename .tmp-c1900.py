import io,re,sys,tempfile,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
print("has smAlt", "smAlt" in h, "has IIFEhead", "const s=d.head" in h, "has cim css", ".cim{" in h)
js="\n;\n".join(re.findall(r"<script>(.*?)</script>",h,re.S))
t=tempfile.mktemp(suffix=".js"); io.open(t,"w",encoding="utf-8").write(js)
print("rc",subprocess.run([r"C:\Users\萧磊\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe","--check",t],capture_output=True,text=True).returncode)
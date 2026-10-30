import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
h=r"D:\系统汉字\web\public\test.html"; s=io.open(h,encoding="utf-8").read()
bad="    }}\n  }\n  $('#hint').innerHTML=base+rel;"
good="    }\n  }\n  $('#hint').innerHTML=base+rel;"
assert bad in s, "pattern not found"
s=s.replace(bad,good)
io.open(h,"w",encoding="utf-8",newline="\n").write(s)
print("fixed braces")
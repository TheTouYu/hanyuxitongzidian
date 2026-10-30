import io
h=io.open(r"D:\系统汉字\web\public\test.html",encoding="utf-8").read()
i=h.find('class="bu"')
print(h[i-300:i+200])
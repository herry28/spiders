from aip import AipOcr
import re

APP_ID="18137435"
API_KEY="Rtast1dOns0Mf4ckdQyM8LKC"
SECRET_KEY="gpEkNxGpWkeqCbnTl3DsR1ni6h4fSCYV"
client=AipOcr(APP_ID,API_KEY,SECRET_KEY)

#将图片读取到程序中
with open(r"E:\image\aa.png","rb") as f:
    image=f.read()
data=str(client.basicGeneral(image)).replace(" ","")
print(data)
pat=r"{'words': '(.*?)'}"
pattern=re.compile(pat)
res=pattern.findall(data)[0]
print(res)
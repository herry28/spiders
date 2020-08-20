import requests
from bs4 import BeautifulSoup


header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "cookie": "loading = agree;UserCookie = e9dd9f3a71827abc08aa24f8fe558149fba232e4b0b0a566158a7423c4fff463;IsLogin = 1"}
#第一页，https://www.zhipin.com/c101280600/b_%E7%A6%8F%E7%94%B0%E5%8C%BA/?query=%E8%87%AA%E5%8A%A8%E5%8C%96&ka=sel-business-4
#第二页， https://careers.tencent.com/search.html?index=2
# 第三页，https://careers.tencent.com/search.html?index=3



#构造每一页的url
for i in range(1,4):
    url="https://careers.tencent.com/search.html?index="+str(i)
    print(url)
    res=requests.get(url,headers=header)
    print(res)
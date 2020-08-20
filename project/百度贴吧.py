# 第一页：http://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search  （1-1）*50
#第一页：http://tieba.baidu.com/f?ie=utf-8&kw=python&pn=0
# 第二页：http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50   （2-1）*50
# 第三页：http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100   （3-1）*50

import  urllib
from urllib import request
import time


header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

def loadpage(fullurl,filename):
    print("正在下载：",filename)
    req=request.Request(fullurl,headers=header)
    res=request.urlopen(req).read()
    return res

def writepage(html,filename):
    print("正在保存：",filename)
    with open(filename,"wb") as f:
        f.write(html)
    print("=============")

def tiebaSpider(url,begin,end):
    for page in range(begin, end+1):
        pn=(page-1)*50
        #每次请求完整的url
        fullurl=url+"&pn="+str(pn)
        # 每次请求后保存的文件名
        filename="c:/第"+str(page)+"页.html"
        #调用爬虫，爬取网页
        html=loadpage(fullurl,filename)
        # 把获取到的网页信息写入本地
        writepage(html,filename)



if __name__ == '__main__':
    kw=input("请输入要爬取的贴吧名：")
    begin=int(input("请输入起始页："))
    end=int(input("请输入结束页："))

    url="http://tieba.baidu.com/f?"
    key=urllib.parse.urlencode({"kw":kw})
    url=url+key
    tiebaSpider(url,begin,end)
    time.sleep(10)
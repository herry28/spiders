import requests
from lxml import etree

class Spider():
    def __init__(self):
        self.tiebaName="java"
        self.beginPage=1
        self.endPage=3
        self.url="http://tieba.baidu.com/f?"
        self.header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        self.fileName=1
    #构造url
    def tiebaSpider(self):
        for page in range( self.beginPage, self.endPage+1):
            pn=(page-1)*50
            myurl=self.url+"&"+"kw="+self.tiebaName+"&"+"pn="+str(pn)
            # print(myurl)
            self.loadPage(myurl)
    #爬取页面内容,获取每个帖子的链接
    def loadPage(self,url):
        #爬取每个网页内容的源代码（字符串）
        res=requests.get(url,headers=self.header).text
        # print(res)
        html=etree.HTML(res)
        # print(html)
        # 获取每个帖子的链接
        links=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        print(links)
        for link in links:
            link="http://tieba.baidu.com"+link
            print(link)
            self.loadImages(link)


    #爬取帖子详情页,获得图片链接
    def loadImages(self,link):
        res=requests.get(link,headers=self.header).text
        html=etree.HTML(res)
        links=html.xpath('//img[class="BDE_Imag"]/@src')
        print(links)
        for imageslink in links:
            self.writeImage(imageslink)

    #通过图片所在链接，爬取图片并保存图片到本地
    def writeImage(self,imageslink):
        print("正在存储图片：",self.fileName,"---")
        image=requests.get(imageslink).text
        #保存图片到本地
        with open("c:\\image"+str(self.fileName)+".jpg","wb") as f:
            f.write(image)
            f.close()
            self.fileName+=1
if __name__ == '__main__':
    myspider=Spider()
    myspider.tiebaSpider()
# -*- coding: utf-8 -*-
import scrapy
import re
from myspider.items import MyspiderItem

class MusicspiderSpider(scrapy.Spider):
    name = 'musicspider'#爬虫识别名称
    allowed_domains = ['http://www.htqyy.com/']#爬取的网页范围
    start_urls = ['http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20']

    def parse(self, response):
        # filename="music.html"
        data=response.body.decode()#获取响应内容
        # open(filename,"wb").write(data)#写入到本地

        items=[]#存放音乐信息的列表
        titles=re.findall(r'target="play" title="(.*?)" ',data)
        artists = re.findall(r'target="_blank">(.*?)</a> ', data)

        for i in range(0,len(titles)):
            pass



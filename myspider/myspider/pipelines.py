# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#管道文件，负责item的后期处理或保存
class MyspiderPipeline(object):
    def __init__(self):
        self.file=open("music.txt","a")
    #管道每接收到item后执行的方法(必须实现)
    # return item 必须要有
    def process_item(self, item, spider):
        content=str(item)+"\n"
        self.file.write(content)#写入数据到本地
        return item
    #当爬取结束时执行的方法
    def close_spider(self,spider):
        self.spider.close()

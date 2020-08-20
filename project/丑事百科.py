import threading
import queue
import requests
import time
from lxml import etree

# http://www.lovehhy.net/Joke/Detail/QSBK/1
# http://www.lovehhy.net/Joke/Detail/QSBK/2



#2个线程
#爬取网页线程---爬取段子列表所在的网页，放进队列
class Thread1(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName  # 线程名
        self.pageQueue = pageQueue  # 页码队列
        self.dataQueue = dataQueue  # 数据队列
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def run(self):
        print("启动线程"+self.threadName)
        while not flag1:
            try:
                page=self.pageQueue.get()
                url="http://www.lovehhy.net/Joke/Detail/QSBK/+str(page)"
                content=requests.get(url,headers=self.headers).text
                time.sleep(0.5)
                self.dataQueue.put(content)#将数据放到数据队列中
            except Exception as e:
                pass
        print("结束线程"+self.threadName)

#解析网页线程---从队列中拿到列表网页，进行解析，并存储到本地
class Thread2(threading.Thread):
    def __init__(self,threadName,dataQueue,filename):
        threading.Thread.__init__(self)
        self.threadName = threadName  # 线程名
        self.dataQueue = dataQueue  # 数据队列
        self.filename=filename


    def run(self):
        print("启动线程"+self.threadName)
        while not flag2:
            try:
                data1=self.dataQueue.get()
                html=etree.HTML(data1)
                node_list=html.xpath("//h3[@class='red']/a")
                for node in node_list:
                    data=node.text
                    self.filename.write(data+"\n")


            except Exception as e:
                pass
        print("结束线程"+self.threadName)

flag1=False#表示页码队列中是否为空，默认不为空
flag2=False#表示数据队列默认不为空

#主逻辑放在main方法里
def main():
    #页码队列
    pageQueue=queue.Queue(10)
    for i in range(1,11):
        pageQueue.put(i)
    #存放采集结果的数据队列
    dataQueue=queue.Queue()
    # 保存到本地的文件
    filename=open("E\\joke\\joke.txt","a")

    t1=Thread1("采集线程",pageQueue,dataQueue)
    t1.start()
    t2=Thread2("解析线程",pageQueue,filename)
    t2.start()

    #当pageQueue为空时，结束采集线程
    while not pageQueue.empty():
        pass
    global flag1
    flag1=True
    # 当dataQueue为空时，结束解析线程
    while not pageQueue.empty():
        pass
    global flag2
    flag2 = True

    t1.join()
    t2.join()
    filename.close()

    print("结束")

if __name__ == '__main__':
   main()




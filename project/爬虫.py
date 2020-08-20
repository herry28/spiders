# import urllib.request
from  urllib import request
import urllib
# import re
# url="http://www.baidu.com"
# res=urllib.request.urlopen(url).read().decode()
# pat=r"<title>(.*?)</title>"
# data=re.findall(pat,res)
# print(data)

# #创建http处理器对象（专门处理http请求的对象）
# http_hander=request.HTTPHandler()
# #创建自定义opener对象
# opener=request.build_opener(http_hander)
# #创建自定义请求对象
# req=request.Request(url)
# #发送请求，获取响应
# res=opener.open(req).read()
#
# #把自定义opener设置为全局，这样用urlopen发送的请求也会使用自定义的opener
# request.install_opener(opener)


#创建代理处理器对象
# proxyhander=request.ProxyHandler()
# #创建自定义opener对象
# opener=request.build_opener(proxyhander)
# #创建自定义请求对象
# req=request.Request(url)
#  #发送请求，获取响应
# res=opener.open(req).read()

# #构造url编码
# wd={"wd":"北京"}
# wdd=urllib.parse.urlencode(wd)
# print(wdd)

# import urllib
# from urllib import  request
# url="http://i.baidu.com/"
# header={
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
#     "Cookie":"BAIDUID=3817703B899AF2D822F3AEC0354A3D45:FG=1; BIDUPSID=3817703B899AF2D822F3AEC0354A3D45; PSTM=1553850290; locale=zh; pgv_pvi=7159101440; BDUSS=XBZdUlsTkVURkZwZkhGNktxY3BTZ1dkOTR2ZGxiMFkzWlhIRGVtek12dzlEaUZlSVFBQUFBJCQAAAAAAAAAAAEAAABdSil-0KG6o2hlcnkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD2B-V09gfldR; ZD_ENTRY=empty; PHPSESSID=ndi0nhre2tqgthgfr9adbsikl0; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1577243336; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1577243336"}
# req=request.Request(url,headers=header)
# res=request.urlopen(req).read().decode()
# print(res)

# import  requests
# res=requests.get("http://www.baidu.com")
#获取响应的cookie
# #1.获取返回的cookiejar对象
# cookiejar=res.cookies
# #2.将cookiejar转换成字典
# cookiedict=requests.utils.dict_from_cookiejar(cookiejar)
# print(cookiedict)

#使用session实现登陆
#1.创建session对象
# se=requests.session()
# #2.构造登陆所需的参数
# data={"user":"","pwd":""}
# #3.通过传递用户名和密码得到cookie信息（变化的）
# se.post(url,data=data)
#4.再去请求其他页面（需要登陆才可以的）

# 正则表达式：针对字符串进行数据筛选的表达式
# 原子：正则表达式中实现匹配的基本单位,每个原子只匹配一个字符
# ①以普通字符作为原子（匹配普通字符），re.search(pat,str)
# ②以通用字符作为原子（匹配通用字符）
# \w,任意字母、数字、下划线
# \W,非字母、数字、下划线
# \d,十进制的数字
# \D,非十进制数字
# \s,空白字符
# \S,非空白字符
# [0-9]，匹配数字
# [a-z][A-Z]，匹配英文
# [\u4e00-\u9fa5]，匹配中文
#原子表：定义一组平等的原子（单个的）
#元字符：正则表达式中具有特殊含义的字符
# .，匹配任意字符（\n除外）（1个字符）
# ^，匹配字符串开始位置
# $，匹配字符串结束位置
# *，重复0或1或n次前面的原子
# ？，重复0或1次前面的原子
# +，重复1或多次前面的原子
# 匹配固定次数
# {n}，前面的原子出现n次
# {n，}，前面的原子至少出现n次
# {n，m}，前面的原子出现次数介于n-m之间

import re
# a="13588996544"
# pat1=r"13/d{9}|\d{3}-\d{7} "
# print(re.sea)

# a="python666java"
# pat=re.compile(r"PYTHON",re.I)#，模式修正符：忽略大小写
# print(pat.search(a))

# strr="pythonjavahtmljs"
# pat=re.compile(r"java")
# print(pat.match())

# strr="hello----------------hello----------------------hello----------hello------------------"
# pat=re.compile(r"hello")
# # print(pat.findall(strr))
# # print(pat.finditer(strr))
# data=pat.finditer(strr)
# list1=[]
# for i in data:
#     list1.append(i.group)
#     print(list1)

# a="张三，，，，李四，，，，，，，，王五，，，，，，，，，，赵六"
# pat=re.compile(r"，+")
# res=pat.split(a)
# print(res)

# str2="hello  123 hello   456!"
# pat=re.compile(r"\d+")
# res=pat.sub("666",str2)
# print(res)

#导包
from lxml import etree
# #将字符串html文档解析成特殊的html对象
# html=etree.HTML()
# #将html对象转成字符串
# res=etree.tostring(html,encoding="utf-8").decode()
# #爬虫中网页处理方式：
# ①数据获取和数据清洗一体，HTML()
# ②数据获取和数据清洗分开，parse()
# 获取指定属性的标签（获取指定标签的所有li标签）
# html.xpath("//li[@class='']")
# 获取标签的属性信息(获取所有li标签的class属性)
# html.xpath("//li/@class")



import threading
import time
import queue

# def run(name):
#     print(name,"线程执行了")
#     time.sleep(5)

# #创建2个线程对象
# t1=threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run, args=("t2",))
# #启动线程
# t1.start()
# t2.start()
# #等待子线程执行完毕再执行主线程后面的内容
# t1.join()
# t2.join()
# print("执行完毕")

# class myThread(threading.Thread):
#     def __init__(self,name):
#         threading.Thread.__init__(self)
#         self.name=name
#     def run(self):
#         print("开始线程",self.name)
#         print("线程执行中---1")
#         time.sleep(1)
#         print("线程执行中---2")
#         time.sleep(1)
#         print("线程执行中---3")
#         time.sleep(1)
#         print("线程结束",self.name)
#
# #创建线程
# t1=myThread("t1")
# t2=myThread("t2")
# t3=myThread("t3")
# #开启线程
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# print("执行完毕")

#队列：用来实现线程安全，提供了一个适用于多线程编程的先进先出的数据结构
# 即队列，用来在生产者和消费者之间的信息传递。

# 创建对象
q=queue.Queue(maxsize=10)#maxsize表示队列里最多可放的对象
for i in range(1,11):
    q.put(i)#在队列里放对象
print(q.get())#取对象
#判断队列是否为空，循环取出所有值
while not q.empty():
    print(q.get())

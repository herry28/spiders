# import random
import os
# #一个学校3个办公室，8个老师随机分配
# school=[[],[],[]]
# #定义一个变量，保存8个老师
# mystr="ABCDEFGH"
# for i in mystr:
#     index=random.randint(0,2)
#     school[index].append(i)
# print(school)


#对一个全是数字的列表求最大值、最小值
#定义一个变量，记录最终的最大值
# mymax=0
# mylist=[1,5,10,200,200,0]
# for value in mylist:
#     if value>mymax:
#         mymax=value
# print(mymax)
#
# mymin=mylist[0]
# for i in mylist:
#     if i<mymin:
#         mymin=i
# print(mymin)


# mytuple=(1,3,5,True,"hello")
# vale=mytuple[4]=hello6666
# print(vale)

# mydict={"name":"小红","age":18,"no":"007"}
# mydict["name"]="小海"
# mydict["title"]="哈哈哈"
# keys=mydict.keys()
#
# if "name" in mydict:
#     print("xuzn")

#计算字符个数
#定义一个列表
# mylist=["hrllo","world"]
# mystr="hello world"
# for i in mystr:
#     #去除空格切这个字符列表未保存过
#     if i!=" " and i not in mylist:
#         count=mystr.count(i)
#         print("%s:%d"%(i,count))
#         mylist.append(i)
#
# print("".join(mylist))
#
# def m():
#     pass

# def myfun(name):
#     print("你好"+name)
# myfun("小海")
# mystr="hello"
#  def mylen(object):
#      res=0
#      for i in object:
#          res+=1
#          print(res)
# mylen(mystr)

# def add(a,b):
#     res=a+b
#     return res
# print(add(4,9))

# def my_print():
#     print("hello world 1")
#
# def my2():
#     print("函数2开始")
#     my_print()
#     print("函数2结束")
#
#
# my2()
# print("测试结束")

# def print_one_line():
#     print("-"*10)
# print_one_line()
#
# def print_lines(n):
#     for i in range(n):
#         print_one_line()
# print_lines(5)

# def add(a,b,c):
#     return a+b+c
# print(add(5,9,8))

# def average(a,b,c):
#     return (a+b+c)/3
# print(average(9,58,2))

# def myinfo(name,no):
#     """
#
#     :param name: name
#     :param no:age
#     :return:姓名，年靓
#     """
#     print("名字："+name)
#     print("学号：" + no)
#     print("年龄：" + age)
#     print("="*30)
# # myinfo("小明","001")
# # myinfo("小还","002")
# # myinfo("小海","002","30")

# help(myinfo)
#
# print("hello","world")
# (lambda : print("hello world"))()
# f=lambda : print("hello world")
# f()
# f=lambda :5
# print(f())
# f=lambda name :print("hello",name)
# f("小海")
# mylist=[{"name":"herry","age":18},{"name":"tom","age":10}]
# mylist.sort(key=lambda mydict:mydict["name"])
# print(mylist)
# mylist=[[10,9,8],[87,5,,2],[9,2,1]]
# mylist.sort(key=lambda newlist:newlist[2],reverse=True)
# print(mylist)
# mylist=[]
# for i in range(1,101):
#     mylist.append(i)
# print(mylist)

# mylist=[i for i in range(1,51)]
# print(mylist)
# my=["herry" for i in range(7)]
# print(my)
#
# myk=[i for i in range(2,51,2)]
# print(myk)

# f=open("x.txt","r")
# res=f.read()
# print(res)
# # f.write("hello world")
# f.close()

# f=open("x.txt","r",encoding="utf-8")
# re=f.read()
# print(re)
# f.close()

# old=open("herry.txt","w")
# old.write("hello xiaohai")
# old.close()
#
# old=open("herry.txt","r")
# result=old.read()
# new=open("herrycopy.txt","w")
# new.write(result)
# new.close()

# os.rename("herry.txt","hahha.txt")
# res=os.getcwd()
# print(res)
# mylist=os.listdir()
# print(mylist)
# os.mkdir("hm")
# os.chdir("hm")
# print(os.getcwd())
# for i in range(10):
#     f=open("hm%d.txt"%i,"w")
#     f.close()

# os.chdir("hm")
# mylist=os.listdir()
# print(mylist)
# for filename in mylist:
#     newfilename=filename.replace(".txt","[中国].txt")
#     print(newfilename)
#     os.rename(filename,newfilename)
# list

# class Hero():
#     def move(self):
#         print("英雄会走")
#
# wukong=Hero()
# wukong.name="悟空"
# print(id(wukong))

# class Dog(object):
#     def eat(self):
#         print("狗吃骨头")
#
#     #     print("毛色：", self.color)
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print("名字：",self.name)
#         print("年龄：", self.age)
#
#
# wancai1=Dog("旺财",7)
# # wancai1.name="旺财"
# # wancai1.age=5
# # wancai1.color="灰色"
# wancai1.info()

# class Hero():
#     def __init__(self,name):
#         self.name=name
#
#     # def info(self):
#     #     print(self.name,self.hp)
#     def __str__(self):
#         return "名字：%s"%self.name
#     def __del__(self):
#         print("zaijia")
# wukong=Hero("悟空")
# wukogn=wukong
# wu=wukong
# del wukong
# # print(wukong)
# # input("请输入信息")

# class Master():
#     def __init__(self):
#         self.kongfu="古法煎饼果子配方"
#     def makecake(self):
#         print("按照《%s》制作煎饼果子"%self.kongfu)
#     def dayanda(self):
#         print("dayandai")
#
#
# class School():
#     def __init__(self):
#         self.kongfu="现代煎饼果子配方"
#         self.__money = 2200
#     def makecake(self):
#         print("按照《%s》制作煎饼果子"%self.kongfu)
#
#
# class Work(Master,School):
#     def __init__(self):
#         self.kongfu="猫屎咖啡"
#
#     def makecake(self):
#         print("按照《%s》制作煎饼果子"%self.kongfu)
#
#
# # tudi=Work()
# # tudi.makecake()

# class Person():
#     def __init__(self):
#         self.name="xiaoming"
#         self.age=20
#     def eat(self):
#         print("坑的几")
#         print("="*20)
# xiaoming=Person()
#
# class Dog():
#     def __init__(self):
#         self.name="gougou"
#         self.age=2
#     def eat(self):
#         print("骨头")
#         print("="*20)
# dog=Dog()
#
# def printinfo(object):
#     print(object.name)
#     print(object.age)
#     object.eat()
#
# printinfo(xiaoming)
# printinfo(dog)


# for i in range(2,6):
#     for j in range(i):
#         print("*",end="")
#     print("")

# class Person():
#     country="中国"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self):
#         print("吃饭")
#         print("="*20)
#
# xiao=Person("小明","3")
# # print(id(xiao))
# # print(id(xiao.name))
# # hah=Person("小名")
# # print(id(hah))
# # print(id(hah.name))
# print(xiao.country)


# class Person():
#     __country="中国"
#     @classmethod
#     def get_country(cls):
#         return cls.__country
#     @classmethod
#     def set_country(cls,new_country):
#         cls.__country=new_country
# print(Person.get_country())
# Person.set_country("美国")
# print(Person.get_country())

# #
# class Person():
#     __country="中国"
#     def __init__(self):
#         self.name="小明"
#     def get_age(self):
#         return self.__age
#     def set_age(self,newage):
#         self.__age=newage
#
#     @classmethod
#     def get_country(cls):
#         return cls.__country
#     @classmethod
#     def set_country(cls,new_country):
#         cls.__country=new_country


# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print("--new")
#         return object.__new__()
#     def __init__(self):
#         print("--init")
#         self.name="小明"
#     def __str__(self):
#         return "名字：%s"%self.name
#     def __del__(self):
#         print("再见")
# xiaoming=Person()
# print(xiaoming)

# class Person():
#     #定义一个类属性，保存这个类创建的对象
#     __instance=None
#     # 定义一个类属性，判断是否是第一次走init方法
#     __is_first=True
#     # 创建对象
#     # 重写new方法，是为了完成单例模式中的对象地址唯一
#     def __new__(cls, *args, **kwargs):
#         #判断是否通过这个类创建对象，如果没有值需要创建
#         if not cls.__instance:
#             # 创建对象保存起来
#             cls.__instance=object.__new__(cls)
#             # 如果有值直接返回
#         return  cls.__instance
#     def __init__(self,name,age):
#         #判断是否是第一次
#         # if Person.__is_first:
#             #赋值一次
#             self.name=name
#             self.age=age
#             #设置类属性__is_first为False
#             # Person.__is_first=False
#
#
# xiaming=Person("小明",20)
#
# xiaohong=Person("小红",21)
# print(id(xiaming.name),id(xiaohong.name))

try:
    open("h.txt","r")
except FileNotFoundError as e:
    print(e)

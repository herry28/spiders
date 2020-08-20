# #使用字典进行保存
# # all_dict={"小海"：{"name":"小海","age":22},"小红":{"name":"小红","age":20}}
# #准备一个空字典
# mydic={}
# #添加名片
# mydic["小海"]={"name":"小海","age":22}
# print(mydic)
# #删除名片
# # del mydic["小海"]
# # print(mydic)
# #修改名片
# mydic["小海"]["age"]=25
# print(mydic)
# #查询名片
# myname=mydic["小海"]["name"]
# print(myname)

#定义一个字典保存所有人的数据
data={}
#引导用户输入
info="""1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
请选择："""


#死循环
while True:
    index = input(info)
    if index == "1":
        # 引导用户输入姓名和年龄
        myname = input("请输入你的姓名：")
        myage = input("请输入您的年龄")
        mydic = {"name": "小海", "age": 22}
        # 添加数据到data中
        data[myname] = mydic
        print("添加名片成功")
    if index == "2":
        # 引导用户输入需要删除的名字
        myname = input("请输入需要删除的名字：")
        # 判断这个名字是否存在于data中
        if myname in data:
            del data[myname]
        else:
            print("你输入的名字有误")
    if index == "3":
        # 引导用户需要修改的名字
        myname = input("请输入需要修改的名字：")
        if myname in data:
            # 引导用户修改后的年靓
            myage = input("请输入修改后的年龄：")
            data[myname]["age"] = myage
            print("修改数据成功")
        else:
            print("你输入的名片有误")
    if index == "4":
        # 引导用户查询的名字
        myname = input("请输入要查询的名字：")
        if myname in data:
            n = data[myname]["name"]
            a = data[myname]["age"]
            print("姓名" + n + "年龄" + a)
        else:
            print("输入信息有误")
    if index=="5":
        print("欢迎下次使用程序")
        break


print(data)

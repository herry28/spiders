#坐地铁的票价
#6km以内3元
#6-12,4
#12-55,5

#定义一个变量模拟出行公里
km=52
#定义一个变量保存单程票价
money=0
if km >0 and km<=6:
    money=3
elif km >6 and km <= 12:
    money=4
elif km >12 and km <=22:
    money=5
elif km>22 and km<=32:
    money=6
    #32km以上部分，每增加1元可乘坐20公里
elif km>32:
    #定义一个变量求公里数的差值
    temp=km-32
    if temp%20==0:
        money=6+temp/20
    else:
        #int去掉小数部分
        money=6+int(temp/20)+1
print("当前票价："+money)
#定义一个变量保存总的消费金额
total_money=0
#循环模拟40次
for i in range(40):
    if total_money<100:
        total_money+=money
    elif total_money>=100 and total_money<150:
        total_money+=money*0.8
    elif total_money>=150 and total_money<400:
        total_money+=money*0.5
    elif total_money>=400:
        total_money+=money
p

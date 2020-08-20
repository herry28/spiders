#打印直角三角形
# row=1
# while row <= 5:
#     col=1
#     while col <= row:
#         print("*",end="")
#         col+=1
#     print()
#     row+=1

#打印九九乘法表
x=1
while x <=9:
    y=1
    while y <=x :
        print("%d*%d=%-2d"%(y,x,x*y),end=" ")
        y+=1
    print()
    x+=1
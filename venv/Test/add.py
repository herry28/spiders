class Calc():
    #加法函数
    def add(self,a,b):
        c=a+b
        return c
    def jian(self,a,b):
        c=a-b
        return c
if __name__ == '__main__':
    #创建对象
    ca=Calc()
    res1=ca.add(3,4)
    res2=ca.jian(5,2)
    print(res1)
    print(res2)
import unittest
from testcase.add import  Calc



# 继承
class Test1(unittest.TestCase):
    #初始化函数
    def setUp(self):
        print('开始')
    # 结束函数
    def tearDown(self):
        print('结束')

    def test_001(self):
        #创建对象
        ca=Calc()
        res1=ca.add(8,9)
        #断言
        self.assertEqual(res1,17)
    def test_002(self):
        ca=Calc()
        res2=ca.jian(10,2)
        self.assertEqual(res2,9)


if __name__ == '__main__':
   unittest.main()

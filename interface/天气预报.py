import requests
import unittest
import xlrd

#给接口地址定义变量名称
# url="http://v.juhe.cn/weather/index"
# para={"cityname":"北京","key":"1da1ca41ccfd55d94882e0e438c7218"}

# #发送请求
# r=requests.get(url,params=para)
# print(r.status_code)
# r.status_code
# #获取json数据
# # print(r.json())
# # res=r.json()
# # print(res["reason"])
# # print(res["result"]["sk"]["temp"])
# res=r.json()
# print(res["error_code"])

# url="http://v.juhe.cn/weather/uni"
# para={"key":"1da1ca41ccfd55d94882e0e438c72188"}
# r=requests.get(url,params=para)
# print(r.json())

# url="http://v.juhe.cn/weather/geo"
# para={"lon":"112","lat":"40","dtype":"json","key":"1da1ca41ccfd55d94882e0e438c72188"}
# r=requests.post(url,data=para)
# print(r.json())

# class Test_add(unittest.TestCase):
#     def setUp(self):
#         print("kaishi")
#     def tearDown(self):
#         print("jisshu")
#     def test01(self):
#         a=1
#         b=2
#         self.assertEqual(2,a+b)
#         self.assertIn()
# if __name__ == '__main__':
#     unittest.main()

# class Weather(unittest.TestCase):
#     def setUp(self):
#         print("开始")
#     def tearDown(self):
#         print("结束")
#     def test_01(self):
#         url="http://v.juhe.cn/weather/index"
#         para={"cityname":"杭州","key":"1da1ca41ccfd55d94882e0e438c72188"}
#         r=requests.get(url,params=para)
#         res=r.json()
#         self.assertEqual(res["reason"],"查询成功!")
#     if __name__ == '__main__':
#         unittest.main()

# class kuaidi(unittest.TestCase):
#     def setUp(self):
#         print("开始")
#     def tearDown(self):
#         print("结束")
#     def test_01(self):
#         url="http:www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
#
#         r=requests.get(url)
#         res=r.json()
#         print(res)
#         self.assertEqual(res["reason"],"查询成功!")
# if __name__ == '__main__':
#         unittest.main()

#打开excel
book=xlrd.open_workbook("data.xlsx")
#定位到sheet
sheet=book.sheet_by_index(0)
#统计行数和列数
print(sheet.nrows)
print(sheet.ncols)
# print(sheet.row_values(0))






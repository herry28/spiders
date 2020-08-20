import re
import requests

header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
res=requests.get(url,headers=header).text
print(res)

# "rating":["9.7","50"]
# "title":"肖申克的救赎"
# "vote_count":1732047
pat1=r'"rating":\["(.*?)","\d+"\]'
pat2=r'"title":"(.*?)"'
pat3=r'"vote_count":(\d+)'
pattern1=re.compile(pat1)
pattern2=re.compile(pat2,re.I)
pattern3=re.compile(pat3)
data1=pattern1.findall(res)
data2=pattern2.findall(res)
data3=pattern3.findall(res)
# print(data1,data2)
# list1=[]
for i in range(len(data1)):
    print("排名:",i+1,"评分:",data1[i],"电影名:",data2[i],"评论数:",data3[i])
#     list1.append(data1[i]+data2[i])
# print(list1)

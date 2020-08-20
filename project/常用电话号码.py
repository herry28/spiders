import re
import requests

header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
url="http://changyongdianhuahaoma.51240.com/"
res=requests.get(url,header).text
# print(res.text)

pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
pattern1=re.compile(pat1)
pattern2=re.compile(pat2)
data1=pattern1.findall(res)
data2=pattern2.findall(res)

resultlist=[]
for i in range(0,len(data1)):
    resultlist.append(data1[i]+data2[i])
    print("卖方：",data1[i],"电话：",data2[i])
print(resultlist)

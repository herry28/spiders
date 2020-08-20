#第一页url
# http://www.htqyy.com/top/hot
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# 第二页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# 第三页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20

#单个歌曲页面的url
# http://www.htqyy.com/play/33
#单个歌曲资源的url
# http://f2.htqyy.com/play7/33/mp3/12



import requests
import re
page=int(input("请输入需要爬取的页数："))
songID=[]
songName=[]

for i in range(page):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    #获取音乐榜单的网页信息
    html=requests.get(url)
    str1=html.text
    # print(str1)
    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'

    idlist=re.findall(pat2,str1)
    titlelist=re.findall(pat1,str1)

    songID.extend(idlist)
    songName.extend(titlelist)
# print(songID)
# print(songName)
for i in range(0,len(songID)):
    songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/12"
    songname=songName[i]

    #爬取歌曲信息
    data=requests.get(songurl).content
    print("正在下载第",i+1,"首")
    with open("E:\\music\\{}.mp3".format(songname),"wb") as f:
        f.write(data)


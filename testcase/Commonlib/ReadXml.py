from xml.dom import minidom

class ReadXml():
    def read_xml(self,filename,onenode,twonode):
    #打开文件
        root=minidom.parse(filename)
        firstnode=root.getElementsByTagName(onenode)[0]
        secondnode=firstnode.getElementsByTagName(twonode).firstChild.data
        return secondnode

r=ReadXml()
res=r.read_xml("../DataXml/data.xml","jia","num1")
print(res)
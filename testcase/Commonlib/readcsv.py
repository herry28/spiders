import csv

class readcsv():
    def read_csv(self):
        mylist=[]
        con=csv.reader(open('../DataXml/data.csv','r'))
        for cons in con:
            mylist.append(cons)
        print(mylist)
        return  mylist



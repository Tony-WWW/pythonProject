#coding: UTF-8
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
import random
import requests
import xlwt
from bs4 import BeautifulSoup




htmls = []
name = []
price = []
location = []
xiaoquname = []
time = []
other = []

page = 1
url = 'https://cq.lianjia.com/ershoufang/pg1/'
r = requests.get(url)
r.encoding= r.apparent_encoding
#r.encoding = "UTF-8"
soup = BeautifulSoup(r.text,'html.parser')
htmls.append(r.text)
for n in soup.find_all('a',class_="title"):
    name.append(n.text)

for p in soup.find_all(class_='price'):
    price.append(p.text)

for xqname in soup.find_all('a',attrs={'data-el':'region'}):
    xiaoquname.append(xqname.text)
#print str(name).decode('string_escape')

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')
num1=0
num2=0
num3=0
for n in name:
    num1 = num1+1
    worksheet.write(num1,0, label = n)

for p in price:
    num2 = num2+1
    worksheet.write(num2,1, label = p)

for a in xiaoquname:
    num3 = num3+1
    worksheet.write(num3,2, label = a)

workbook.save('Excel_test.xls')




#print("loading page" + url)

#print(soup.prettify())

#print (soup.select(""))

#prices = soup.find_all(class_="price")

#for pri in prices:
    #print(type(item))
 #   print(pri.text)

#infos = soup.find_all(class_="info")

#for inf in infos:
    #print(type(item))
 #   print(inf.text)


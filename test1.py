#coding=utf-8

#读取数据或者集合每一行的某一列
#>>> a=[[1,2,3],[4,5,6]]
#>>> a[0]    #取一行
#[1, 2, 3]
#>>> a[:,0]  #尝试用数组的方法读取一列失败
#TypeError: list indices must be integers or slices, not tuple



#我们需要用列表解析的方法读取一列
#>>> b=[x[0] for x in a]
#>>> print(b)
#[1, 4]

#而对于数组，可以直接读取：
#>>> import numpy as np
#>>> a=np.array([[1,2,3],[4,5,6]])
#>>> a[:,0]
#array([1, 4])
import operator
import os
import sqlite3
import urlparse
import urllib
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict



db_path='/Users/tony/'
files=os.listdir(db_path)
history_db=os.path.join(db_path,'History')
conn=sqlite3.connect(history_db)
cursor=conn.cursor()
sql='select url,visit_count from urls'
cursor.execute(sql)

results=cursor.fetchall()

count_dict={}
for url,count in results:
   try:
      url = url.split('//')[1]           #地址从//切断取第1个值
      domain = url.split('/')[0]         #地址从/切断取第0个值
      #print domain
   except:
      print 'error format!'
   if domain in count_dict:
      count_dict[domain]+=1
   else:
      count_dict[domain]=1

count_sorted=sorted(count_dict.items(),key=operator.itemgetter(1),reverse=True)

#count_sorted.encode('utf-8')
a=[k[0] for k in count_sorted] #a代表网址
b=[j[1] for j in count_sorted] #b代表网站的访问次数
#print a

#print count_sorted[0]
x=np.arange(len(count_sorted))
y=np.array(b)
plt.rcParams['figure.figsize'] = (20.0, 12.0)
plt.bar(range(len(b)),b,tick_label=a)
#plt.xticks(rotation=45)
#plt.xticks(range(len(count_sorted)),count_sorted.keys())
plt.title('Google',size=40)
#plt.bar(count_sorted,count_sorted)

for c,d in zip(x,y):
   plt.text(c,d+0.1, '%.0f' % d, ha='center', va= 'bottom',fontsize=20)
#num_list = [1.5,0.6,7.8,6]
#plt.bar(range(len(num_list)), num_list)
plt.ylim(0,10)
plt.xticks(x,size='small',rotation=30)
plt.show()

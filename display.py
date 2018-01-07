#!/usr/bin/python3


# -*- coding:utf-8 -*-
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import re
import sqlite3

 
conn=sqlite3.connect('zl.db')
sql='select * from zl '
data=pd.read_sql(sql,conn)
df=pd.DataFrame(data,columns=['Name1','Name2','Sum'])
df2=df[(df.Sum>14)&(df.Sum<25)]
tmp=df2.set_index(['Name1','Name2'])
tmp2=tmp['Sum'].unstack('Name2')
tmp2.T.plot(kind='bar')
plt.show()
conn.commit() 
conn.close()
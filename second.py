#!/usr/bin/python3


# -*- coding:utf-8 -*-

import requests,bs4
import re
import sqlite3


conn=sqlite3.connect('my.db')
c=conn.cursor()

c.execute('select NameFrom,NameTo,count(*) from list group by NameFrom,NameTo')

lists=c.fetchall()
cx=sqlite3.connect('zl.db')
cu=cx.cursor()
cu.execute('create table sum (NameFrom string ,NameTo string,Sum Number)')         
cu.executemany('insert into  sum values(?,?,?)',lists)
cu.execute('create table copy (NameFrom string ,NameTo string,Sum Number)')         
cu.executemany('insert into  copy values(?,?,?)',lists)
cu.execute('create table zl (Name1 string ,Name2 string,Sum Number)') 
cu.execute('select sum.NameFrom,sum.NameTo,CASE  WHEN copy.Sum is NULL THEN sum.Sum ELSE sum.Sum+copy.Sum END from sum left outer join copy on sum.NameFrom=copy.NameTo and sum.NameTo=copy.NameFrom')
zlList=cu.fetchall()     
cu.executemany('insert into  zl values(?,?,?)',zlList)
cx.commit()
cx.close()
conn.commit()
conn.close()









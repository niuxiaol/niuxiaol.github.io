#!/usr/bin/python3


# -*- coding:utf-8 -*-

import requests,bs4

import re
import sqlite3
from urllib.parse import urljoin 

url="https://www.spinics.net/lists/alsa-devel/"
req=requests.get(url)
req.encoding="UTF-8"
#print(req.text)
soup=bs4.BeautifulSoup(req.text,"lxml")

        


values=[]
 
for a in soup.find_all("a"):
    result=re.search('^Re.*?',a.get_text())
    if result :
        s=a['href']
        Url = urljoin(url,s)
        req2=requests.get(Url)
        print(Url)            
        soup2=bs4.BeautifulSoup(req2.text,"lxml")
        sli=soup2.ul.find_all("li")
                       
        s1=re.findall(r"From: (.+?)<",sli[2].get_text())
        s2=re.findall(r"To: (.+?)<",sli[0].get_text())
        values.append(["".join(s1),"".join(s2),sli[1].get_text()])
    
cx=sqlite3.connect('my.db')
cu=cx.cursor()
cu.execute('create table list (NameFrom string ,NameTo string,href string)')         
cu.executemany('insert into  list values(?,?,?)',values)

cx.commit()
cx.close()




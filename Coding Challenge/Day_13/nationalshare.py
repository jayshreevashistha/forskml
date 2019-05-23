# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:44:39 2019

@author: computer
"""

from bs4 import BeautifulSoup  
import matplotlib.pyplot as plt
import requests

wiki = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")

right_table=soup.find('table', class_='wikitable')

A=[]
B=[]
C=[]

#for bdy in right_table.find_all("tr"):
for row in right_table.findAll('tr'):
    cells = row.find_all('td')
    if len(cells) ==7:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[4].text.strip())
        
import pandas as pd
from collections import OrderedDict

col_name = ["Rank","State/Territory","National Share"]
col_data = OrderedDict(zip(col_name,[A,B,C]))
df = pd.DataFrame(col_data)
data= df.sort_values('National Share', ascending=False)
data1= data.iloc[:6,]
print(data1)


labels = list(data1.iloc[:,1])
sizes = [9.37, 9.3, 7.33, 5.96,5.83,4.87]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','gold','lightcoral']
explode = (0.1, 0, 0, 0,0,0)  
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)

plt.axis('equal')
plt.show()
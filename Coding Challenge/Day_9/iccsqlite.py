# -*- coding: utf-8 -*-
"""
Created on Thu May 16 23:55:19 2019

@author: computer
"""


from bs4 import BeautifulSoup
import requests

wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

source = requests.get(wiki).text

soup = BeautifulSoup(source,"lxml")


right_table=soup.find('table', class_='table')


A=[]
B=[]
C=[]
D=[]
E=[]

for bdy in right_table.find_all("tbody"):
    for row in bdy.find_all("tr"):
        cells = row.find_all('td')
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["Position","Team","Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))
df = pd.DataFrame(col_data)


import os
import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'icc.db' )

c = conn.cursor()

#c.execute()
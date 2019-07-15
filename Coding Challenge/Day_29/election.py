
#print("Top 5 male baby name in 2017\n",df1[(df1["Sex"] == "M") & (df1["Year"] == 2017)].head(5))# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:53:05 2019

@author: computer
"""

import pandas as pd
import numpy as np
import matplotlib as plt

dataset = pd.read_csv('election.csv')

# Fetch the top parties of each state within each constituency with their vote %.
df = dataset[['State','Constituency','Party','%']]
df_sort = df.sort_values(by = '%',ascending = False)
df_final = df_sort.drop_duplicates(subset = 'Constituency')


#Visualize the top parties vote % in each constituency for Rajasthan.
df1 = dataset[['State','Constituency','Party','%']]
df1 = df1[(df1["State"]=="Rajasthan")]
df1 = df1.sort_values(by = '%',ascending = False)
df1 = df1.drop_duplicates(subset = 'Constituency')
df1['Party'].value_counts().plot.bar()


#Visualize the total seats gained by each party in each states.
seats = dataset[['State','Constituency','Party','%']]
seats1 = seats.sort_values( '%',ascending = False)
seats1 = seats.drop_duplicates(subset = 'Constituency')
seat_count = seats.groupby(['Party','State'])['Constituency'].count()

#Visualize the total seats won by the parties in the whole country
tseats = dataset[['State','Constituency','Party','%']]
sort4 = tseats.sort_values( '%',ascending = False)
sort4 = tseats.drop_duplicates(subset = 'Constituency')
sort4 = seats1.groupby(['Party'])['Constituency'].count()
sort4.plot.bar()



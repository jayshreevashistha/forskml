# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:05:13 2019

@author: computer
"""
"""
import os
import pandas as pd
path = os.getcwd()
os.chdir(path + "\\baby_names")
list1 = os.listdir(path + "\\baby_names")


df = pd.DataFrame()

for i in range(1880,2011):
    for x in list1:
        if x=="yob"+str(i)+".txt":
            text=open(x)
            print(i)
            df[i] = pd.Series(text.read().splitlines())
"""            
import pandas as pd
import os

path = os.getcwd()
os.chdir(path + "\\baby_names")
list1 = os.listdir(path + "\\baby_names")
df1=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
for i in range(1880,2018):
    filename="yob"+str(i)+".txt"
    df2 = pd.read_csv(filename,header=None)
    df2.columns = ['Name', 'Sex', 'Number']
    df2['Year']=i
    df2 = df2.sort_values(by=['Number'], ascending=False)
    df1=pd.concat([df1, df2])
    
print("Top 5 male baby name in 2017\n",df1[(df1["Sex"] == "M") & (df1["Year"] == 2017)].head(5))
print("Top 5 female baby name in 2017\n",df1[(df1["Sex"] == "F") & (df1["Year"] == 2017)].head(5))

df=df1.groupby(['Year', 'Sex'])['Number'].aggregate('sum').unstack()
df.plot()
    
         

            

   

  
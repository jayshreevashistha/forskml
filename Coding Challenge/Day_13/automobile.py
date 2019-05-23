# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:54:20 2019

@author: computer
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Automobile.csv")

series = df["make"].value_counts()

print (series.index[0:10])
print (series.values[0:10])

explode = (0.2,0,0,0,0,0,0,0,0,0)

plt.pie(series.values[0:10], explode = explode, labels=series.index[0:10], autopct='%2.2f%%')
plt.axis('equal')

plt.show()

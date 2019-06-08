# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:01:17 2019

@author: computer
"""


# Importing the libraries
import pandas as pd
from apyori import apriori
from collections import defaultdict
import matplotlib.pyplot as plt

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
dict1 = defaultdict(int)
transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
    
list1 = []
for item in transactions:
    for value in item:
        cleanedlist = [value for value in item if str(value)!='nan']
    list1.append(cleanedlist)

for item in list1:
    for value in item:
        dict1[value]+=1

# Training Apriori on the dataset
rules = apriori(list1, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")



import operator

print("Top 10 edibles:")
print(dict(sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)[:11]))
D=(dict(sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)[:11]))

#bar chart 

plt.bar(range(len(D)), list(D.values()), align='center')
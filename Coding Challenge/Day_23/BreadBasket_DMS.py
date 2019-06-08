# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:34:20 2019

@author: computer
"""

# Importing the libraries
import pandas as pd
import matplotlib as plt
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')

dataset= dataset.drop(['Date','Time'],axis=1)

#pie chart of top 15 selling items.
dataset['Item'].value_counts()[:16].plot.pie()

#intialize transaction
transaction=[]

#convert series to list
def convert_tolist(arg):
    transaction.append(list(arg))

#convert dataset to lists of lists
dataset.groupby(["Transaction"])["Item"].apply(convert_tolist)

# Training Apriori on the dataset
rules = apriori(transaction, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

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
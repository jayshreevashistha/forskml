# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:37:32 2019

@author: computer
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
# Importing the dataset
dataset = pd.read_csv('monster_com-job_sample.csv')
#for i in dataset:
    #dataset[i] = dataset[i].fillna(dataset[i].mode()[0])

# Filling out the nan values with 'Mising' keyword
dataset = dataset.replace(np.nan, 'Mising')

#make a list for organization column to find the pattern of location
l1 = []
for item in dataset['organization']:
    result=re.findall(r'^[A-Za-z]*\s?[[A-Za-z]*]?[\,]{1}?\s?[A-Z]{2}\s?[0-9]*',item)
    l1.append(result)
#get the list of index with loc in organization column
loc_ind=[]
for item in l1:
    if(item!=[]):
        loc_ind.append(l1.index(item)) 
#check for organization in the column location of list of index       
l2 = []
for item in loc_ind:
    result=re.findall(r'^[a-zA-Z&\-\.\/\s]{10,}',dataset['location'][item])
    l2.append(result)

     

"""
for line in dataset:
    columns=line.split()
    x=columns['location']
    y=columns['organization']
        if columns['organization']>columns['location']:
            columns['location']=y
            columns['organization']=x
"""
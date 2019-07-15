# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:26:53 2019

@author: computer
"""
"""
attr1_1 
Attractive
sinc1_1
Sincere
intel1_1
Intelligent
fun1_1
Fun
amb1_1
Ambitious
shar1_1
Has shared interests/hobbies
"""


import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Dating_Data.csv',encoding = "Windows 1252")

x= dataset['gender']
y = dataset.iloc[:,[69,70,71,72,73,74]]#,'sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1']


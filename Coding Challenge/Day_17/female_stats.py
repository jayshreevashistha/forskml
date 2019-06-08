# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:44:32 2019

@author: computer
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

dataset = pd.read_csv("Female_Stats.csv")

features = dataset.iloc[:, 1:3].values
labels = dataset.iloc[:, 0].values

features_m = dataset.iloc[:,1].values
features_f = dataset.iloc[:,2].values

import statsmodels.api as sm

features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)

print("When Father's Height is Held Constant then the average height increase by",regressor_OLS.params[1])

print("When Mother's Height is Held Constant then the average height increase by",regressor_OLS.params[2])
"""
import pandas as pd
import numpy as np

dataset=pd.read_csv("stats_females.csv")

features=dataset.iloc[:,1:]
labels=dataset.iloc[:,0]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(features_train,labels_train)

import statsmodels.formula.api as sm
features=np.append(arr=np.ones((214,1)).astype(int),values=features,axis=1)

features_opt=features[:,[0,1,2]]
regressor_OLS=sm.OLS(labels,features_opt).fit()
regressor_OLS.summary()

#When Father’s Height Is Held Constant, The Average Student Height Increases 
#By How Many Inches For Each One-Inch Increase In Mother’s Height.
print("When Father's Height is Held Constant then the average height increase by",regressor_OLS.params[1])

print("When Mother's Height is Held Constant then the average height increase by",regressor_OLS.params[2])


"""










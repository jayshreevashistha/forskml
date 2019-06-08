# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:00:17 2019

@author: computer
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#imports the CSV dataset using pandas

dataset = pd.read_csv('kc_house_data.csv')

for i in dataset:
    dataset[i] = dataset[i].fillna(dataset[i].mode()[0])

#prepare the data to train the model
features = dataset.iloc[:,[0,1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20] ].values  
labels = dataset.iloc[:,2 ].values 

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,1] = labelencoder.fit_transform(features[:, 1])




from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  

#train the algo
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features_train, labels_train)  


print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (regressor.score(features_test,labels_test)*100,2))





from sklearn.linear_model import Lasso
regressor_lasso = Lasso() 
regressor_lasso.fit(features_train, labels_train)
print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (regressor_lasso.score(features_test,labels_test)*100,2))




from sklearn.linear_model import Ridge
regressor_ridge =  Ridge()
regressor_ridge.fit(features_train, labels_train)
print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (regressor_ridge.score(features_test,labels_test)*100,2))

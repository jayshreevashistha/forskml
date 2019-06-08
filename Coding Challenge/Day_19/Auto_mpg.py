# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:30:36 2019

@author: computer
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 


dataset = pd.read_fwf('Auto_mpg.txt',names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"])

dataset["horsepower"]=dataset["horsepower"].replace('?','0')
features = dataset.iloc[:,1:8].values
labels = dataset.iloc[:,[0]].values


 
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20,random_state=0)   



# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  

#Training and making predictions
from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
 

Score_dt = regressor.score(features_test,labels_test)
print("Score_df:",Score_dt)

x=[6,215,100,2630,22.2,80,3]
x=np.array(x).reshape(1,-1)
print("mpg_df: ",regressor.predict(x))



from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test)  



Score_rf = regressor.score(features_test,labels_test)
print("Score_rf:",Score_rf)


x=[6,215,100,2630,22.2,80,3]
x=np.array(x).reshape(1,-1)
print("mpg_rf: ",regressor.predict(x))